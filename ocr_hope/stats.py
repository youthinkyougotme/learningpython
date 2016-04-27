
def get_child_key_count(dictionary) :
    dictionary_count =

    for parent_key in dictionary :

        for child_key in dictionary[parent_key] :

            current_count = dictionary[parent_key][child_key]["count"]
            dictionary_count = current_count + dictionary_count

    return dictionary_count


def run_stats(commencement_line_count, student_locations_us, student_locations_world, student_locations_bad_states, student_locations_bad_cities, student_locations_errors_other, student_locations_bad_counties) :

    print '\n\nRunning Stats...\n'

    student_list_total = commencement_line_count
    print 'Total student lines read from student list file: {0}'.format(student_list_total)

    student_locations_bad_counties_count = len(student_locations_bad_counties)
    print 'County errors: {0}'.format(student_locations_bad_counties_count)

    student_locations_us_count = get_child_key_count(student_locations_us)
    print 'Number of successfully parsed city, state & county, id pairs: {0}'.format(student_locations_us_count)

    captured_percentage = float(student_locations_us_count)/float(student_list_total)
    print 'Captured percentage: {0}%\n'.format(captured_percentage*100)


    student_locations_world_count = get_child_key_count(student_locations_world)
    print 'International hometowns: {0}\n'.format(student_locations_world_count)

    student_locations_bad_states_count = get_child_key_count(student_locations_bad_states)
    print 'No \'state\' found instances: {0}'.format(student_locations_bad_states_count)

    student_locations_errors_other_count = len(student_locations_errors_other)
    print 'Other errors: {0}'.format(student_locations_errors_other_count)

    total_error_count = student_locations_bad_states_count + student_locations_errors_other_count
    # print 'Total errors: {0}'.format(total_error_count)

    error_percentage = float(total_error_count)/float(student_list_total)
    print 'Error percentage: {0}%\n'.format(error_percentage*100)

    print ''
