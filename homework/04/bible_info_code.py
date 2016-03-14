import parse_bible
from parse_bible import bible, abbreviations
import nltk
from nltk import word_tokenize


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
            if token != '.' or token != '!' or token != '?' :
                firstSentence.append(token)

        # check for 'Jesus' and 'Pharisees' in first sentence
        if 'Jesus' in firstSentence and 'Pharisees' in firstSentence :
            print "{0}:{1}".format(chapterIndex+1, verseIndex+1)
            print matthew[chapterIndex][verseIndex]

        verseIndex = verseIndex + 1

    # increment chapter index
    chapterIndex = chapterIndex + 1


raw_input('hault')

bible = dict()
books = ['hi', 'hola']
with open("kjv_edit.atv") as file :

    for line in file :

      line = line.rstrip()

      parts = line.split('@')
      book = parts[0]
      chapter = int(parts[1])
      print chapter
      number = int(parts[2])
      print number

      if chapter == 1 and number == 1 :
        print 'in if'
        print book

        books.append(book)

    print books

raw_input('haulted')


for x in sorted(bible.keys()):
  print abbreviations[x]
  print bible[x][0][-1]

raw_input('haulted')



print type(bible)
raw_input('haulted')

print type(bible['2Th'])
print bible['2Th']
raw_input('haulted')

print type(bible['2Th'][1])
print bible['2Th'][1]
raw_input('haulted')

print type(bible['2Th'][1][1])
print bible['2Th'][1][1]
raw_input('haulted')

# collection of books with minimum number of chapters
books_with_min_chaps = dict ()

# current minimum number
current_min = len(bible["Ge"])

# current book that has fewer, or equal, to minimum
current_book_with_min_chapters = "Ge"

#print bible['Hag']
#print bible['Jas']
#print bible['Phi']

for book in bible:

    print book

    current_number_of_chapters = len(bible[book])

    print "{0} : {1}".format(current_number_of_chapters, current_min)

    if current_number_of_chapters < current_min:
        print 'less than min'

        # update current minimum
        current_min = current_number_of_chapters

        # current_chapters = current_number_of_chapters
        # book_with_fewest_chapters = book

    elif current_number_of_chapters == current_min :
        print 'equal min'

    else :
        print 'greater than min'


# print "The book with fewest chapters is {0} with {1} chapters".format(book_with_fewest_chapters, current_chapters)
