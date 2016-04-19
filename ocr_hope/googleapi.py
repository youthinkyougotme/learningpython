import re
import json
import requests

# get the county name using google maps api
def google_it(loc) :
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




def set_counties(states) :

    for state in states :

        for city in states[state] :

            # remove spaces from city and state elements
            city = re.sub('\s', '', city)
            state = re.sub('\s', '', state)

            # create location variable to pass to google api
            loc = '{0}+{1}'.format(city,state)

            # look up the locaiton using google maps api
            county_name = google_it(loc)

            # remove county and township words from county name
            county_name = re.sub('\sCounty','',county_name)
            county_name = re.sub('\sTownship','',county_name)

            # add the county name to the city dicitonary
            states[state][city]["county_name"] = county_name
