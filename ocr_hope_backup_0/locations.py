import re
import difflib

from lists import get_world_countries, get_us_states

verbose = False
world_countries = get_world_countries()
us_states = get_us_states()

# return a dictionary of states with cities from the provided file
def get_locations(file) :

    print '\nGetting locations...\n'

    states = dict()
    clean_state = ''
    section_titles = []
    loc_parsing_error_count = 0
    loc_parsing_success_count = 0
    states_not_found_count = 0
    empty_states_count = 0
    international_count = 0
    international_countries = []

    with open(file) as commencement_list :

        for line in commencement_list:

            line = line.rstrip()

            # skip empty lines
            if line != '' :

                section_title = re.findall('CANDIDATES FOR THE BACHELOR', line)

                # if the line isnt currently the section title
                if len(section_title) == 0 :

                    # add space between (period)(alpha) patterns
                    line = re.sub('\.([a-zA-Z])', r'. \1', line)

                    # extract the city and state from the student line
                    stud_parts = re.split('(\.\s)(\.\s)+', line)

                    # get the city and state, it is last in the list
                    # clean up the address, remove period at beginning of city
                    stud_addre = stud_parts[-1]

                    # split address into city and state
                    stud_addre = re.split(',|\.', stud_addre)

                    # check for two entries in student address for city and state
                    if len(stud_addre) == 2 :

                        # clean up city state, replace begin/ending spaces and lowercase
                        stud_city = stud_addre[0].lower()
                        stud_city = re.sub('\s', '', stud_city)

                        stud_state = stud_addre[1].lower()
                        stud_state = re.sub('\s', '', stud_state)

                        # if student state is empty
                        if stud_state == '' :
                            # increment the count to keep track of the number of empty states
                            empty_states_count = empty_states_count + 1

                            if verbose :
                                print 'empty state!\nstates not found: {0}'.format(empty_states_count)
                                raw_input('continue...')

                        else :
                            # the student state is not empty

                            # is the student state in the list of us states?
                            if stud_state in us_states :
                                # there is a match, the student state is passed as the clean state
                                clean_state = stud_state

                            # is the student state in the list of world countries?
                            elif stud_state in world_countries :

                                # there is a match, the student state is not passed as the clean state
                                # increment the count to keep track of the number of international students
                                international_count = international_count + 1
                                # save the international country to the list
                                international_countries.append(stud_state)

                                if verbose :
                                    print 'international country!\nInternational count: {0}'.format(international_count)
                                    raw_input('continue...')

                            else :
                                # if the stadent state is not in
                                # the us states list and not in the international countries list

                                # check for the closest match in the us states list
                                state_matches = difflib.get_close_matches(stud_state, us_states)

                                if verbose :
                                    print stud_state

                                # if the us state matches do not come up empty
                                if len(state_matches) != 0 :

                                    if verbose :
                                        print state_matches
                                        print 'suggested state above'
                                        raw_input('continue...')

                                    # pass the best match (index 0) as the clean state
                                    clean_state = state_matches[0]

                                else :
                                    # there were not matches for the student state
                                    # increment the count to keep track of the number of states not found
                                    states_not_found_count = states_not_found_count + 1
                                    # save the international country to the list
                                    international_countries.append(stud_state)

                                    if verbose :
                                        print 'no suggested matches!\nstates not found: {0}'.format(states_not_found_count)
                                        raw_input('continue...')

                        # if the clean state is no longer empty
                        # a clean state was found
                        if clean_state != '' :

                            # add state to states dictionary if not there already
                            if clean_state not in states :
                                states[stud_state] = dict()

                            # add city to corresponding state dictionary if not there already
                            if stud_city not in states[clean_state] :
                                states[clean_state][stud_city] = dict()
                                # set the count of the city to 1
                                states[clean_state][stud_city]["count"] = 1;
                            else :
                                # the city is already in the corresponding state dictionary
                                # set and increment the city count
                                current_count = states[clean_state][stud_city]["count"]
                                states[clean_state][stud_city]["count"] = current_count + 1

                            # Success count
                            loc_parsing_success_count = loc_parsing_success_count + 1

                        else :
                            # no clean state was found
                            if verbose :
                                print 'no clean state'
                                raw_input('continue...')

                    else :
                        # the address for the student does not have two elements
                        loc_parsing_error_count = loc_parsing_error_count + 1

                else :
                    # the current line is a section title
                    section_titles.append(section_title)

    print '\nDone getting cities and states...'
    print 'Location Parsing...'
    print 'Succeeded: {0}'.format(loc_parsing_success_count)
    print 'Errors: {0}'.format(loc_parsing_error_count)
    print 'International: {0}'.format(international_count)
    print 'States not found: {0}\n'.format(states_not_found_count)

    return states
