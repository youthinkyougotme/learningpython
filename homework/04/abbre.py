abbreviations = dict()

with open("abbreviations.txt") as abbre_file :

    for line in abbre_file :
        book_abbr_name = line.rstrip().split(':')
        print book_abbr_name
        book_abbreviation = book_abbr_name[0].replace(" ", "")
        print book_abbreviation
        book_fullname = book_abbr_name[1].replace(" ", "")
        print book_fullname

        for each in book_abbr_name :
            abbreviations[book_abbreviation] = book_fullname

    print abbreviations
