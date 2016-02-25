import sys

if len(sys.argv) != 2 :
    sys.exit()

d = dict ()

with open(sys.argv[1]) as input:
    for line in input :
        line = line.rstrip()
        list = line.split()

        for w in list :
            if w in d :
                d[w] = d[w] + 1
            else :
                d[w] = 1

for k in sorted(d.keys()) :
    print "{0}: {1}".format(k, d[k])