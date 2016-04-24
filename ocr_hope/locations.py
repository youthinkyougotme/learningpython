import re
import difflib

def key_value_to_dictionary(this_key, this_value, this_dict) :

    # add state to states dictionary if not there already
    if this_key not in this_dict :
        this_dict[this_key] = dict()

    # add city to corresponding state dictionary if not there already
    if this_value not in this_dict[this_key] :
        this_dict[this_key][this_value] = dict()
        # set the count of the city to 1
        this_dict[this_key][this_value]["count"] = 1;
    else :
        # the city is already in the corresponding state dictionary
        # set and increment the city count
        current_count = this_dict[this_key][this_value]["count"]
        this_dict[this_key][this_value]["count"] = current_count + 1


# return a dictionary of states with cities from the provided file
def get_student_locations(text_file, us_states_list, world_countries_list) :

    us_states = us_states_list
    world_countries = world_countries_list

    student_locations_us = {}
    student_locations_world = {}
    student_locations_bad_states = {}
    student_locations_bad_cities = {}
    student_locations_errors_other = []

    with open(text_file) as students_list :

        for line in students_list :

            line = line.rstrip()

            if line != '' :

                section_title = re.findall('CANDIDATES FOR THE BACHELOR', line)

                if len(section_title) == 0 :

                    # add space between (period)(alpha) patterns
                    line = re.sub('\.([a-zA-Z])', r'. \1', line)

                    # extract the city and state from the student line
                    line_parts = re.split('(\.\s)(\.\s)+', line)

                    # get the city and state, it is last in the list
                    # clean up the address, remove period at beginning of city
                    student_city_state = line_parts[-1]

                    # split address into city and state
                    student_city_state = re.split(',|\.', student_city_state)

                    if len(student_city_state) == 2 :

                        # clean up city state, replace begin/ending spaces and lowercase
                        student_city = student_city_state[0].lower()
                        student_city = re.sub('\s', '', student_city)

                        student_state = student_city_state[1].lower()
                        student_state = re.sub('\s', '', student_state)


                        if student_city != '' :

                            if student_state == '' :

                                # if student state is empty
                                student_state = 'empty'
                                student_locations_bad_states[student_state] = student_city

                            if student_state != '' :
                                # the student state is not empty

                                # is the student state in the list of us states?
                                if student_state in us_states :
                                    # there is a direct match with the us_states list
                                    key_value_to_dictionary(student_state, student_city, student_locations_us)

                                elif student_state in world_countries :
                                    # there is a direct match with the us_states list
                                    key_value_to_dictionary(student_state, student_city, student_locations_world)

                                else :
                                    # if the stadent state is not in us or countries
                                    # check for the closest match in the us states list
                                    state_matches = difflib.get_close_matches(student_state, us_states)

                                    # if the us state matches do not come up empty
                                    if len(state_matches) != 0 :

                                        # pass the best match (index 0) as the clean state
                                        state_match = state_matches[0]

                                        # there is a corrected match with the us_states list
                                        key_value_to_dictionary(state_match, student_city, student_locations_us)

                                    else :
                                        # there were not matches for the student state
                                        student_locations_bad_states[student_state] = student_city
                        else :

                            if student_state != '' :
                                student_city = 'empty'

                                if student_state == '' :
                                    student_state = 'empty'

                            student_locations_bad_cities[student_city] = student_state

                    else :
                        student_locations_errors_other.append(student_city_state)

    return (student_locations_us, student_locations_world, student_locations_bad_states, student_locations_bad_cities, student_locations_errors_other)
