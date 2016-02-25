# PROBLEM 5

# need sys for command line arguments
import sys

# need this to do calculations
import math

# check that there is at two command line arguments
if len(sys.argv) == 3 :

    # get the command line arguments, convert them from strings to integers
    first_int = int(sys.argv[1])
    second_int = int(sys.argv[2])

    # assume that first integer is the smaller of the two,
    # but just in case...
    if first_int > second_int :
        smaller_val = second_int
        larger_val = first_int
    else :
        smaller_val = first_int
        larger_val = second_int

    # show the range of integers
    integers_range = range(smaller_val, larger_val + 1, 1)
    # print integers_range

    # sum the range of integers
    total = sum(integers_range)
    # print total

    print "The sum of the integers from {0} to {1} is {2}".format(smaller_val, larger_val, total)

else :
    print "Error! The number of command line arguments is incorrect."

sys.exit()
