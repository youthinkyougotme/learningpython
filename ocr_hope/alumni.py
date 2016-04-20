# --------- imports ---------
import re
import types
import json
import requests
import difflib

from lists import get_world_countries, get_us_states, get_us_counties
from locations import get_locations
from googleapi import set_counties

verbose = False
world_countries = get_world_countries()
us_states = get_us_states()

# print locations
def print_locations() :
    for state in locations :

        state_total = 0
        print state
        # print locations[state]
        for city in locations[state] :
            count = locations[state][city]["count"]
            state_total = state_total + count

            print '     {0}: {1}'.format(city, count)

        print '          {0} total: {1}\n'.format(state,state_total)




# ------------------------
# --------- main ---------
# ------------------------

create_states_counties_ids = raw_input("Run get_us_counties, y or n? ")
if create_states_counties_ids == 'y' :
    # us_states_counties_ids is a dictionary of state dicts of country name keys and id values
    us_states_counties_ids = get_us_counties('lists/us_counties.tsv')
    # write the states counties ids dictionary to a text file
    json.dump(us_states_counties_ids, open("lists/us_states_counties_ids.json",'w'))

else :
    with open("lists/us_states_counties_ids.json") as json_file:
        us_states_counties_ids = json.load(json_file)

print '------------------\n'
print '------------------\n'
print us_states_counties_ids

create_locations = raw_input("Run get_locations and set_counties, y or n? ")
if create_locations == 'y' :
    # locations is a dictionary of state dicts of city dictionaries
    locations = get_locations('lists/2014.txt')
    # get the county for the city, state and add it to the city dictionary
    set_counties(locations)
    # write the locations dictionary to a text file
    json.dump(locations, open("lists/locations.json",'w'))

else :
    with open("lists/locations.json") as json_file:
        locations = json.load(json_file)

print '------------------\n'
print '------------------\n'
print locations


print '------------------\n'
print '------------------\n'
def set_county_ids() :

    # using locations dictionary & us_states_counties_ids dictionary

    for state in locations :

        print state

        for city in state :
            print city
            print locations[state][city]



set_county_ids()
