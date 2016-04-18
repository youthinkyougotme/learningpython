# --------- imports ---------

import re
import types
import json
import requests
import difflib


verbose = False


official_us_states = [
    'Alaska',
    'Alabama',
    'Arkansas',
    'American Samoa',
    'Arizona',
    'California',
    'Colorado',
    'Connecticut',
    'District of Columbia',
    'Delaware',
    'Florida',
    'Georgia',
    'Guam',
    'Hawaii',
    'Iowa',
    'Idaho',
    'Illinois',
    'Indiana',
    'Kansas',
    'Kentucky',
    'Louisiana',
    'Massachusetts',
    'Maryland',
    'Maine',
    'Michigan',
    'Minnesota',
    'Missouri',
    'Northern Mariana Islands',
    'Mississippi',
    'Montana',
    'National',
    'North Carolina',
    'North Dakota',
    'Nebraska',
    'New Hampshire',
    'New Jersey',
    'New Mexico',
    'Nevada',
    'New York',
    'Ohio',
    'Oklahoma',
    'Oregon',
    'Pennsylvania',
    'Puerto Rico',
    'Rhode Island',
    'South Carolina',
    'South Dakota',
    'Tennessee',
    'Texas',
    'Utah',
    'Virginia',
    'Virgin Islands',
    'Vermont',
    'Washington',
    'Wisconsin',
    'West Virginia',
    'Wyoming'
]
i = 0
us_states = []
for state in official_us_states:
    state = re.sub('\s','',state)
    us_states.append(state.lower())
    i = i + 1
print us_states



# --------- function definitions ---------

# return a diction of the city, state in the file
def getLocations(file) :
    clean_state = ''
    error_count = 0
    success_count = 0
    states_not_found = 0
    states = dict()

    print '\nGetting cities and states'
    with open(file) as graduates :

        for line in graduates:

            line = line.rstrip()

            # skip empty lines
            if line != '' :

                # print line

                section_title = re.findall('CANDIDATES FOR THE BACHELOR', line)
                # print section_title

                if len(section_title) == 0 :

                    # add space between (period)(alpha) patterns
                    line = re.sub('\.([a-zA-Z])', r'. \1', line)
                    # print line

                    # extract the city and state from the student line
                    stud_parts = re.split('(\.\s)(\.\s)+', line)
                    # print stud_parts

                    # get the city and state, it is last in the list
                    # clean up the address, remove period at beginning of city
                    stud_addre = stud_parts[-1]
                    # print stud_addre

                    # split address into city and state
                    stud_addre = re.split(',|\.', stud_addre)
                    # print stud_addre

                    if len(stud_addre) == 2 :

                        # clean up city state, replace begin/ending spaces and lowercase
                        stud_city = stud_addre[0].lower()
                        stud_city = re.sub('\s', '', stud_city)

                        stud_state = stud_addre[1].lower()
                        stud_state = re.sub('\s', '', stud_state)

                        #print stud_city
                        #print stud_state

                        # if student state matches states list, good!, proceed
                        if stud_state == '' :
                            states_not_found = states_not_found + 1

                            if verbose :
                                print 'empty state!\nstates not found: {0}'.format(states_not_found)
                                raw_input('continue...')


                        elif stud_state in us_states :
                            print stud_state
                            # raw_input('match found')

                            clean_state = stud_state


                        else :
                            state_matches = difflib.get_close_matches(stud_state, us_states)

                            if verbose :
                                print stud_state

                            if len(state_matches) != 0 :

                                if verbose :
                                    print state_matches
                                    print 'suggested state above'
                                    raw_input('continue...')

                                clean_state = state_matches[0]

                            else :
                                states_not_found = states_not_found + 1

                                if verbose :
                                    print 'no suggested matches!\nstates not found: {0}'.format(states_not_found)
                                    raw_input('continue...')

                        if clean_state != '' :
                            print stud_state
                            print clean_state

                            if verbose :
                                print stud_state
                                print clean_state
                            #raw_input('results, continue...')


                            # add state to states dictionary if not there already
                            if clean_state not in states :
                                states[stud_state] = dict()

                            if verbose :
                                print states[clean_state]

                            print stud_city
                            if stud_city not in states[clean_state] :
                                #print states[clean_state]
                                states[clean_state][stud_city] = dict()
                                states[clean_state][stud_city]["count"] = 1;
                            else :
                                current_count = states[clean_state][stud_city]["count"]
                                states[clean_state][stud_city]["count"] = current_count + 1

                            # print states[clean_state]
                            # raw_input('continue...')

                            success_count = success_count + 1
                            #print 'Success! {0}'.format(success_count)


                        else :
                            if verbose :
                                print 'no clean state'
                                raw_input('continue...')

                    else :

                        error_count = error_count + 1
                        #print 'error! {0}'.format(error_count)

    print '\nDone getting cities and states...'
    print 'States not found: {0}'.format(states_not_found)
    print 'Succeeded: {0}'.format(success_count)
    print 'Errors: {0}'.format(error_count)

    return states


# get the county name using google maps api
def getCounty(loc) :
    ## location variable
    # format: '<cityname>+<stateabbre>'
    # loc = 'holland+mi';

    ## setup api get requests
    # format example:
    # http://maps.googleapis.com/maps/api/geocode/json?address=holland+mi
    api_url = 'http://maps.googleapis.com/maps/api/geocode/json?address='+loc

    # capture entire get request response
    api_resp = requests.get(api_url)

    # see the status of the response
    # print api_resp.status_code
    # see the json data
    # print api_resp.json()

    # convert the response to json python handable code
    api_data = json.loads(api_resp.text)

    # check status code
    api_status = api_data["status"]
    print 'API response: ' + api_status

    # extract long form address
    api_addr = api_data["results"][0]["formatted_address"]
    # print api_addr
    # print type(api_addr)

    # extract county name
    api_county = api_data["results"][0]["address_components"][1]["short_name"]
    # print api_county
    # print type(api_county)

    return api_county


def setCounty() :

    for state in states :

        if state != '' :

            print '\n' + state
            # print states[state]

            if state in us_states :

                for city in states[state] :
                    city = re.sub('\s', '', city)
                    state = re.sub('\s', '', state)
                    loc = '{0}+{1}'.format(city,state)
                    print loc

                    county_name = getCounty(loc)
                    print county_name
                    county_name = re.sub('\sCounty','',county_name)
                    county_name = re.sub('\sCounty','',county_name)
                    print county_name
                    states[state][city]["county_name"] = county_name
                    print states[state]

            else :
                print 'fix: international location'

        else :
            print 'error: blank state'

# --------- main ---------

states = getLocations('2014.txt')

# print states

# setCounty()

for state in states :
    print state
    # print states[state]
    for city in states[state] :
        count = states[state][city]["count"]
        print '     {0}: {1}'.format(city, count)



# loc = 'holland+mi'
# locCounty = getCounty(loc)
# print locCounty
