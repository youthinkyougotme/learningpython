# PROBLEM 4

# need sys for command line arguments
import sys

# need this to do calculations
import math

# check that there is at least one command line argument
if len(sys.argv) == 2 :

    # open the text file
    with open(sys.argv[1]) as class_file :

        # create and empty dictionary
        scores = dict()

        # loop through the text file
        for line in class_file :

            # for each line

            # remove endline characters & split the line into to list items at the ":"
            class_name_scores = line.rstrip().split(':')
            ## print "the current class list scores value is {0} and is of {1}".format(class_name_scores, type(class_name_scores))

            # assign the name, found in index 0, to a variable in all lowercase
            name = class_name_scores[0].lower()
            ## print "the current name value is {0} and is of {1}".format(name, type(name))

            # assign the scores, found in index 1, to a variable after removing the spaces and splitting them via a comma
            name_scores = class_name_scores[1].replace(" ", "").split(',')
            ## print "the current scores value is {0} and is of {1}".format(scores, type(scores))

            # loop through the scores
            for score in name_scores :

                # for each score

                # get the current index integer value that the loop is on
                index = name_scores.index(score)
                ## print "the current index value is {0} and is of {1}".format(index, type(index))

                # convert the score of type string into an integer type, save it to itself
                score = int(score)
                ## print "the current score value is {0} and is of {1}".format(score, type(score))

                # override the old score string value with the score integer value in the scores list
                name_scores[index] = score
                ## print "the current scores value is {0} and is of {1}".format(scores, type(scores))

                ## raw_input('hit enter to continue')

            # assign the the current scores integers list as the value to name key in the dictionary
            scores[name] = name_scores
            ## print "the current class grades value is {0} and is of {1}".format(scores, type(scores))

        ## raw_input('hit enter to continue')
        ## print "the current class grades value is {0} and is of {1}".format(scores, type(scores))

        # get the name that the user wants to know about
        requested_name  = raw_input("Enter a student name: ").lower()

        # check if the requested name is in the scores dictionary before proceeding
        while requested_name not in scores :

            # student not found
            print 'Student {0} is not in the class.'.format(requested_name.capitalize())
            # re-enter the name
            requested_name  = raw_input("Please re-enter a students name: ").lower()

        else :
            # name requested is in the class, user may proceed

            # for floating point calculation and decimal result
            # requested_sum = math.fsum(scores[requested_name])

            # sum up the scores
            requested_sum = sum(scores[requested_name])
            # know the number of scores recorded
            requsted_scores_num = len(scores[requested_name])
            # find the average by dividing the sum by the number of scores
            requested_average =  requested_sum / requsted_scores_num

            print 'Student {0} has an average score of {1} ({2} scores found)'.format(requested_name.capitalize(), requested_average, requsted_scores_num)

else :
    print "Error! Either you have too many command line arguments or"
    print "Provide just one command line argument of the text file containing the course data.\nTry again."

sys.exit()
