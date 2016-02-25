import random
import sys

if (len(sys.argv) > 2) :

    with open(sys.argv[1]) as students_file:

        students_list = []
        num_students_requested = int(sys.argv[2])

        for student in students_file:
            student = student.rstrip()
            students_list.append(student)

        if ( int(sys.argv[2]) <= len(students_list) ) :

            students_list_remaining = students_list

            for i in range(num_students_requested):

                index = random.randint(0, len(students_list_remaining)-1)
                choosen_student = students_list_remaining[index]

                print "{0} was picked at random".format (choosen_student)

                students_list_remaining.remove(choosen_student)

        else :
            print "there is not enought students in the file to pick {0} students".format(num_students_requested)
            sys.exit()

else :
    sys.exit('not enought arguments, (script) (text file path) (number of students requested)')
