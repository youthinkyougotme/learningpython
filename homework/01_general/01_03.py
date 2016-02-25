import random
import sys

# are there enough arguments?
if (len(sys.argv) > 2) :

    # print "Some command line arguments are present, good."

    with open(sys.argv[1]) as students_file:

        # declare some variables for later use
        students_list = []
        num_students_requested = int(sys.argv[2])

        # loop through each line in the students file
        for student in students_file:
            # for each student name:

            # remove endline character from student name
            student = student.rstrip()

            # populate the students_list list with the students name
            students_list.append(student)

        # if the number of random students requested is less than the number of students in the file
        if ( int(sys.argv[2]) <= len(students_list) ) :

            # print "Number of students is {0} from file {1}".format(num_students_requested, sys.argv[1])

            # copy original list into new variable to deduct students picked from larger list
            # this method reduces loop size/time
            students_list_remaining = students_list

            for i in range(num_students_requested):

                # generate a random integer including 0 and up to the last index value of the student list
                index = random.randint(0, len(students_list_remaining)-1)

                # get the choosen student
                choosen_student = students_list_remaining[index]

                print "{0} was picked at random".format (choosen_student)

                # remove the choose student from the remaining students list
                students_list_remaining.remove(choosen_student)

        else :

            # uh oh, the user requested more random students than there are in the list
            print "there is not enought students in the file to pick {0} students".format(num_students_requested)

            # terminate the program
            sys.exit()

else :
    # there aren't enough arguments
    # terminate the program
    sys.exit('not enought arguments, (script) (text file path) (number of students requested)')
