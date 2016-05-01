import re
import difflib
import time

from global_var_and_func import offline_mode, key_value_to_dictionary
from googleapi import set_city_info


# return a dictionary of states with cities from the provided file
def get_student_locations(student_list_text_file_path, us_states, world_countries, state_county_names_ids, main_run_index) :

    # variables for google api call parameters
    api_call_count = 0
    api_call_interval = 10
    api_call_wait_time = 1.75

    # dictionaries and lists to be populated
    student_locations_us = {}
    student_locations_world = {}
    student_locations_bad_states = {}
    student_locations_bad_cities = []
    student_locations_errors_other = []
    student_locations_bad_counties = []

    # to keep track of the line count
    commencement_line_count = 0

    with open(student_list_text_file_path) as students_list :

        for line in students_list :

            line = line.rstrip()

            # skip the line if it is empty
            if line != '' :

                # sniff out whether the line is a title line
                section_title = re.findall('CANDIDATES FOR THE BACHELOR', line)

                # if the line is not a title line
                if len(section_title) == 0 :

                    # keep track of the number of lines read
                    commencement_line_count = commencement_line_count + 1

                    # add space between (period)(alpha) patterns
                    line = re.sub('\.([a-zA-Z])', r'. \1', line)

                    # extract the city and state from the student line
                    line_parts = re.split('(\.\s)(\.\s)+', line)

                    # get the city and state, it is last in the list
                    # clean up the address, remove period at beginning of city
                    student_city_state = line_parts[-1]

                    # split address into city and state
                    student_city_state = re.split(',|\.', student_city_state)

                    # most likely parsed right if the student city state is two elements long
                    if len(student_city_state) == 2 :

                        # clean up city state
                        # replace begin/ending spaces and lowercase

                        student_city = student_city_state[0].lower()
                        student_city = re.sub('\s', '', student_city)

                        student_state = student_city_state[1].lower()
                        student_state = re.sub('\s', '', student_state)

                        # check if there is a city element
                        if student_city != '' :


                            # if there is city and an empty state
                            # not fit for a google api call
                            if student_state == '' :

                                # add the city and 'empty' state to the bad_states dictionary
                                student_state = "empty"
                                key_value_to_dictionary(student_state, student_city, student_locations_bad_states)


                            # if there is city and a state
                            if student_state != '' :
                                # the student state is not empty

                                # is the student state is already in the list of us states?
                                if student_state in us_states :

                                    # not offline_mode is actually calling the google api and thus a wait time is needed
                                    if not offline_mode :
                                        # check if a certain number of calls have been made and then wait
                                        if api_call_count % api_call_interval == 0 :
                                            print "Give Google a break, wait {0} secs...".format(api_call_wait_time)
                                            time.sleep(api_call_wait_time)


                                    # there is a valid state, and a non empty city field
                                    # pass the two along to the google api
                                    # depending on the response, add the state city pair to the appropriate dict or list
                                    set_city_info(student_locations_us, student_state, student_city, state_county_names_ids, student_locations_bad_counties, student_locations_bad_cities, main_run_index)

                                    # an api call was made, increment the count
                                    api_call_count = api_call_count + 1


                                # is the student state in the list of world countries?
                                # if so, it is not fit for a google api call
                                elif student_state in world_countries :

                                    # there is a direct match of the student state
                                    # with an entry of the world country list, so add it to that dict
                                    key_value_to_dictionary(student_state, student_city, student_locations_world)


                                # the student state doesnt match a state or country in the respective lists
                                else :

                                    # check for the closest match in the us states list
                                    state_matches = difflib.get_close_matches(student_state, us_states)

                                    # if the us state matches do not come up empty
                                    if len(state_matches) != 0 :

                                        # pass the best match (index 0) as the clean state
                                        student_state_match = state_matches[0]

                                        # not offline_mode is actually calling the google api and thus a wait time is needed
                                        if not offline_mode :
                                            # check if a certain number of calls have been made and then wait
                                            if api_call_count % api_call_interval == 0 :
                                                print "Give Google a break, wait {0} secs...".format(api_call_wait_time)
                                                time.sleep(api_call_wait_time)

                                        # there is a valid state, and a non empty city field
                                        # pass the two along to the google api
                                        # depending on the response, add the state city pair to the appropriate dict or list
                                        set_city_info(student_locations_us, student_state_match, student_city, state_county_names_ids, student_locations_bad_counties, student_locations_bad_cities, main_run_index)

                                        # an api call was made, increment the count
                                        api_call_count = api_call_count + 1

                                    # there were no matches for the student state in the us states list
                                    # not fit for a google api call
                                    else :
                                        # add the erronous state to the appropriate dictionary
                                        key_value_to_dictionary(student_state, student_city, student_locations_bad_states)

                        # if student city is empty
                        # not fit for a google api call
                        else :

                            if student_state != '' :
                                student_city = 'empty'

                                if student_state == '' :
                                    student_state = 'empty'

                            # add empty city to this dict
                            student_locations_bad_cities[student_city] = student_state


                        # print the number of api counts thus far
                        print '\nGoogle API calls: {0}\n'.format(api_call_count)

                    # uh oh, the city state address has more than two elements, lets keep track of it
                    # not fit for a google api call
                    else :
                        # add this type of error to a specific list
                        student_locations_errors_other.append(student_city_state)


    return (student_locations_us, student_locations_world, student_locations_bad_states, student_locations_bad_cities, student_locations_errors_other, student_locations_bad_counties, commencement_line_count)
