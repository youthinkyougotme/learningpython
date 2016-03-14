6.	Write a program that will print out the chapter and verse number and verse contents for any verse in the book of Matthew (abbreviation Mat) where the word Jesus and the word Pharisees appear in the first sentence of the verse.

Assume that the parse_bible and parse_sentiment modules are available to you if needed.  You can use the sent_tokenize and word_tokenize functions from the nltk.tokenize module to help you break up the verses into sentences and words.

The in operator can test whether or not a string exists in a list; this should be helpful.

Here’s what the output should look like
15:1
Then came to Jesus scribes and Pharisees, which were of Jerusalem, saying,
16:6
Then Jesus said unto them, Take heed and beware of the leaven of the Pharisees and of the Sadducees.
22:41
While the Pharisees were gathered together, Jesus asked them,

Replace this paragraph with your answer to question 6

# get matthew book, type: list of chapters
matthew = bible['Mat']

chapterIndex = 0
for chapter in matthew :

    # get verses, type: list
    verses = matthew[chapterIndex]

    verseIndex = 0
    # for each verse
    for verse in verses :

        # clear first sentence variable
        firstSentence = []

        # tokenize verse, type: list
        verseTokens = word_tokenize(verse)

        # get first sentece, type: list
        for token in verseTokens :

            # add words to first sentence
            # check for common sentence ending punctuation
            if token != '.' or token != '!' or token != '?'
                firstSentence.append(token)

        # check for 'Jesus' and 'Pharisees' in first sentence
        if 'Jesus' in firstSentence and 'Pharisees' in firstSentence :
            print "{0}:{1}".format(chapterIndex+1, verseIndex+1)
            print matthew[chapterIndex][verseIndex]

        verseIndex = verseIndex + 1

    # increment chapter index
    chapterIndex = chapterIndex + 1
