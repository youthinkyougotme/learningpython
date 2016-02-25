scores = {}

with open("scores.txt") as score_file:
    for line in score_file:
        line = line.rstrip()
        parts = line.split(":")
	student_name = parts[0].strip()

        scores_as_strings = parts[1].split(",")
        scores_as_numbers = []
        for score in scores_as_strings:
            scores_as_numbers.append(int(score))

        scores[student_name] = scores_as_numbers
 
for key in scores.keys():
    print "{0}: {1}".format(key, scores[key])
