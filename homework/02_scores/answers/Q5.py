import sys

if len(sys.argv) != 3:
    print "You must pass two arguments to this program"
    sys.exit ()

low = int(sys.argv[1])
high = int(sys.argv[2])

numbers = range(low, high+1)

total = sum(numbers)

print "The sum of the integers from {0} to {1} is {2}".format(low, high, total)
