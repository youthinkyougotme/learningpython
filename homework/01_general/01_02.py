import sys

if len(sys.argv) < 2 :
    print "Incorrect usage"
    sys.exit()

for index in range(1,len(sys.argv)) :
    with open(sys.argv[index]) as file :
        for line in file :
            if "waldo" in line.lower() :
                print "Found Waldo in {0}".format(sys.argv[index])
                sys.exit()
