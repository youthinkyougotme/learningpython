import re
import types

output = ['First,Middle,Last,City,State,Washington,Page\n']

with open('senate.txt') as file :

    for line in file :

        # remove newline character
        line = line.rstrip()

        # remove asterisk
        line = re.sub('\*', '', line)

        # remove double quotes
        line = re.sub('"', '', line)

        # remove weird artifacts
        line = re.sub('^[1\-]+', '', line)
        line = re.sub('^t+', '', line)

        # replace ... with single space
        line = re.sub('\.\.+', ' ', line)

        # replace ./s with single space
        line = re.sub('\.\s', ' ', line)

        # add space after ave
        line = re.sub('ave\s', 'ave  ', line)

        # add space after street
        line = re.sub('street\s', 'street  ', line)

        # add space before street number
        nums = re.findall('[0-9]{2,4}', line)
        if nums :
            line = re.sub(nums[0], ' ' + nums[0], line)

        # add space after state abbreviation
        abbrev = re.findall('.{2,},\s[A-Za-z]{2,3}\s',line)
        if abbrev :
            line = re.sub(abbrev[0], abbrev[0] + ' ', line)

        # add space after two letter spaced state abbreviation
        space_abbrev = re.findall('\s[A-Za-z]{1}\s[A-Za-z]{1}\s',line)

        if space_abbrev :
            abbrev =  ' ' + re.sub('\s', '', space_abbrev[0]) + ' '
            line = re.sub(space_abbrev[0], abbrev, line)

        # split line into parts based off of double spaces
        # in most cases splits the line into 4 parts: name, home address, washington residence, and page
        line_parts = re.split('\s\s+', line)

        clean_line_parts = []

        # check size of parts
        if len(line_parts) == 3 :

            third_item = line_parts[2]

            alphas = re.findall('[a-zA-Z]',third_item)

            if alphas :
                line_parts.append('-')
            else :
                line_parts.append(third_item)
                line_parts[2] = '-'


        if len(line_parts) > 3 :

            # has four columns

            # indexes
            name = 0
            home = 1
            wres = 2
            page = 3

            count = 0

            # general individual parts clean up
            for part in line_parts :

                # remove space at beginning of part
                part = re.sub('^\s+', '', part)

                if count == 0 :
                    name_parts = re.split(',\s', part)

                    name_last = name_parts[0]

                    name_first_mid = name_parts[1]
                    name_first_mid_parts = re.split('\s', name_first_mid)

                    if len(name_first_mid_parts) == 2 :
                        name_first = name_first_mid_parts[0]
                        name_mid = name_first_mid_parts[1]
                    else :
                        name_first = name_first_mid_parts[0]
                        name_mid = '-'

                if count == 1 :
                    home_parts = re.split(',\s', part)

                    if len(home_parts) > 1 :
                        city = home_parts[0]
                        state = home_parts[1]
                    else :
                        city = home_parts[0]
                        state = '-'

                if count == 3 :

                    # remove punctuation
                    content = re.findall('[0-9A-Fa-f]',part)
                    if content :

                        pg_number = ''

                        for num in content :
                            pg_number += num

                        part = pg_number

                clean_line_parts.append(part)
                count += 1;

            clean_line_parts[wres] = re.sub('\.\s', '', clean_line_parts[wres]);

            name_last = re.sub('\s', '', name_last)
            name_last = re.sub('^\.11', '', name_last)
            name_last = re.sub('^II', 'II ', name_last)

            print "First: {0}\nMid: {1}\nLast: {2}\nCity: {3}\nStat: {4}\nWRes: {5}\nPage: {6}".format(name_first, name_mid, name_last,city,state,clean_line_parts[wres],clean_line_parts[page] + '\n\n')

            save = name_first + "," + name_mid + "," + name_last + "," + city + "," + state  + "," + clean_line_parts[wres] + "," + clean_line_parts[page] + "\n"

            output.append(save)

    ## end for line in file

## end with

save_file = open('senate.csv', 'w')
for each in output:
    save_file.write(each)
