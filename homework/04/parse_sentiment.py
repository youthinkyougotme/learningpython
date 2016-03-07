from random import random

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
