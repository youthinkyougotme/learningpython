scores = {"Bandstra": [75, 92, 94], "Hagood": [80,83,77], "McFall": [100,90,95]}

student = raw_input("Enter a student name: ")
student = student.rstrip()

while not student in scores:
    print "Student '{0}' does not exist.".format(student)
    student = raw_input("Please re-enter the student's name: ")
    student = student.rstrip()

total = sum(scores[student])
number = len(scores[student])
average = total / number

print "Student '{0}' has an average score of {1} ({2} scores total)".format(student, average, number)
