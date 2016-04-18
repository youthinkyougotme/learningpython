# --------- imports ---------

import re
import types
import json
import requests

us_states = {
        'alaska': '',
        'alabama': '',
        'arkansas': '',
        'american samoa': '',
        'arizona': '',
        'california': '',
        'colorado': '',
        'connecticut': '',
        'district of columbia': '',
        'delaware': '',
        'florida': '',
        'georgia': '',
        'guam': '',
        'hawaii': '',
        'iowa': '',
        'idaho': '',
        'illinois': '',
        'indiana': '',
        'kansas': '',
        'kentucky': '',
        'louisiana': '',
        'massachusetts': '',
        'maryland': '',
        'maine': '',
        'michigan': '',
        'minnesota': '',
        'missouri': '',
        'northern mariana islands': '',
        'nississippi': '',
        'nontana': '',
        'national': '',
        'north carolina': '',
        'north dakota': '',
        'nebraska': '',
        'new hampshire': '',
        'new jersey': '',
        'new mexico': '',
        'nevada': '',
        'new york': '',
        'ohio': '',
        'oklahoma': '',
        'oregon': '',
        'pennsylvania': '',
        'puerto rico': '',
        'rhode island': '',
        'south carolina': '',
        'south dakota': '',
        'tennessee': '',
        'texas': '',
        'utah': '',
        'virginia': '',
        'virgin islands': '',
        'vermont': '',
        'washington': '',
        'wisconsin': '',
        'west virginia': '',
        'wyoming': '',
}
# --------- function definitions ---------

# return a diction of the city, state in the file
def getLocations(file) :
    error_count = 0
    success_count = 0
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
                        stud_city = stud_addre[0].lower().strip()
                        stud_state = stud_addre[1].lower().strip()
                        #print stud_city
                        #print stud_state

                        # add state to states dictionary if not there already
                        if stud_state not in states :
                            states[stud_state] = dict()


                        if stud_city not in states[stud_state] :
                            #print states[stud_state]
                            states[stud_state][stud_city] = dict()
                            states[stud_state][stud_city]["count"] = 1;
                        else :
                            current_count = states[stud_state][stud_city]["count"]
                            states[stud_state][stud_city]["count"] = current_count + 1

                        # print states[stud_state]
                        # raw_input('continue...')

                        success_count = success_count + 1
                        #print 'Success! {0}'.format(success_count)

                    else :

                        error_count = error_count + 1
                        #print 'error! {0}'.format(error_count)

    print '\nDone getting cities and states'
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

print states

setCounty()

# for state in states :
#
#     print state
#     # print states[state]
#
#     for city in states[state] :
#         count = states[state][city]["count"]
#         print '     {0}: {1}'.format(city, count)



loc = 'holland+mi'
locCounty = getCounty(loc)
print locCounty
