# PROBLEM 1

# need sys for command line arguments
import sys

# define the scores dictionary
scores = {"Hagood":[80, 83, 77], "McFall":[100, 90, 95], "Bandstra":[75, 92, 94]}

# print out the dictionary keys and value in sorted order
for grade in sorted(scores) :

    # "name": "[score, score, score]"
    print "{0}: {1}".format(grade, scores[grade])

sys.exit()
