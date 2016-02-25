scores = {"Bandstra": [75, 92, 94], "Hagood": [80,83,77], "McFall": [100,90,95]}

for key in scores.keys():
    print key, ": ", scores[key]

print "\n\n"

#  Another way
for key in scores.keys():
    print "{0}: {1}".format(key, scores[key])
