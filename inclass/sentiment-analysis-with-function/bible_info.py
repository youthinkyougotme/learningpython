import parse_bible
from parse_bible import bible, books
import parse_sentiment
from parse_sentiment import sentiment, lookup_sentiment

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import pos_tag

partsOfSpeech = {
"JJ": "adj",
"JJR": "adj",
"JJS": "adj",
"NN": "noun",
"NNS": "noun",
"NNP": "noun",
"NNPS": "noun",
"PRP": "noun",
"PRPS": "noun",
"PRP$": "noun",
"RB": "adverb",
"WRB": "adverb",
"RBR": "adverb",
"RBS": "adverb",
"VB": "verb",
"VBD": "verb",
"VBG": "verb",
"VBN": "verb",
"VBP": "verb",
"VBZ": "verb"
}

book = raw_input ("Enter the desired book: ")
book_chapters = bible[book]

chapter = int(raw_input("Enter the desired chapter [1 - {0}]: ".format(len(book_chapters))))

verse_number = int(raw_input("Enter the desired verse [1 - {0}]: ".format(len(book_chapters[chapter-1]))))

verse = bible[book][chapter-1][verse_number-1]

sentences = sent_tokenize (verse)

for sentence in sentences:
    words = word_tokenize(sentence)
    tagged_words = pos_tag (words)

    word_index = 0
    
    for word, pos in tagged_words:
        print word, ":",

        if pos in partsOfSpeech:
            sentiment_dict_pos = partsOfSpeech[pos]
            value = lookup_sentiment(word,sentiment_dict_pos)
            if value != None:
                if word_index > 0 and words[word_index-1] == "not":
                    value = value * -1

                print value
            else:
                print "I don't know anything about this word"
        word_index = word_index + 1
            