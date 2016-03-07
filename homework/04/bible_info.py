import parse_bible
from parse_bible import bible

fewest_chapters = len(bible["Ge"])
book_with_fewest_chapters = "Ge"

for book in bible:
    number_of_chapters = len(bible[book])
    if number_of_chapters < fewest_chapters:
        fewest_chapters = number_of_chapters
        book_with_fewest_chapters = book

print "The book with fewest chapters is {0} with {1} chapters".format(book_with_fewest_chapters, fewest_chapters)

book = raw_input ("Enter the desired book: ")
book_chapters = bible[book]


chapter = int(raw_input("Enter the desired chapter [1 - {0}]: ".format(len(book_chapters))))

verse_number = int(raw_input("Enter the desired verse [1 - {0}]: ".format(len(book_chapters[chapter-1]))))

verse = bible[book][chapter-1][verse_number-1]

print "{0} {1}:{2} {3}".format(book, chapter, verse_number, verse)

found = False

for book in books:
    chapter_num = 1
    for chapter in bible[book]:
        verse_num = 1
        for verse in chapter:
            if word_to_find in verse and not found:
                print "First mention of {0} is in {1} {2}:{3}".format(word_to_find, book, chapter_num, verse_num)
                found = True

            verse_num = verse_num + 1

        chapter_num = chapter_num + 1
