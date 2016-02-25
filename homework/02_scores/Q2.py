# PROBLEM 2

# need sys for command line arguments
import sys

# need this to do calculations
import math

# define the scores dictionary
scores = {"Hagood":[80, 83, 77], "McFall":[100, 90, 95], "Bandstra":[75, 92, 94]}

# get the name that the user wants to know about
requested_name  = raw_input("Enter a student name: ")

# does the name exit in the text file?
if requested_name in scores :

    # name requested is in the class, user may proceed
    # print "the requested name is {0}, its value is {1} and is of {2}".format(requested_name, scores[requested_name],type(scores[requested_name]))

    # for floating point calculation and decimal result
    # requested_sum = math.fsum(scores[requested_name])

    # sum up the scores
    requested_sum = sum(scores[requested_name])
    # know the number of scores recorded
    requsted_scores_num = len(scores[requested_name])
    # find the average by dividing the sum by the number of scores
    requested_average =  requested_sum / requsted_scores_num

    print 'Student {0} has an average score of {1} ({2} scores found)'.format(requested_name, requested_average, requsted_scores_num)

else :

    print 'Student {0} is not in the class.'.format(requested_name)

sys.exit()
