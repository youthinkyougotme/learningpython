from random import random
from nltk.stem import SnowballStemmer

sentiment = dict()

scores = {
  "positive": 1,
  "neutral": 0,
  "negative": -1,
  "weakneg": -1
}

multipliers = {
  "weaksubj": 1,
  "strongsubj": 2
}

with open("sentiment-dictionary.txt") as sentimentFile:
    for line in sentimentFile:
        line = line.rstrip()
        parts = line.split(" ")
        entry = dict()

        for part in parts:
            key = part.split("=")[0]
            value = part.split("=")[1]
            entry[key] = value

        pos = entry["pos1"]
        word = entry["word1"]

        polarity = entry["priorpolarity"]
        if polarity == "both":
              polarity = "positive" if random() < 0.5 else "negative"

        type = entry["type"]

        score = scores[polarity]
        multiplier = multipliers[type]

        if pos not in sentiment:
          pos_dict = {}
          sentiment[pos] = pos_dict
        else:
          pos_dict = sentiment[pos]

        pos_dict[word] = score * multiplier

def lookup_sentiment(word, part_of_speech):
    stemmer = SnowballStemmer("english")
    
    lowercase_word = word.lower()
    word_dict = sentiment[part_of_speech]
    if lowercase_word in word_dict:
        return word_dict[lowercase_word]
    else:
        anypos_dict = sentiment["anypos"]
        if lowercase_word in anypos_dict:
            return anypos_dict[lowercase_word]

    stemmed_word = stemmer.stem(lowercase_word)

    if stemmed_word in word_dict:
        return word_dict[stemmed_word]
    else:
        anypos_dict = sentiment["anypos"]
        if stemmed_word in anypos_dict:
            return anypos_dict[stemmed_word]
        
    return None    