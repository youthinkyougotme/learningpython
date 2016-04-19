# --------- imports ---------
import re
import types
import json
import requests
import difflib

from lists import get_world_countries, get_us_states
from locations import get_locations
from googleapi import set_counties

verbose = False
world_countries = get_world_countries()
us_states = get_us_states()

# ------------------------
# --------- main ---------
# ------------------------

# locations is a dict of state dicts of city dicts
locations = get_locations('lists/2014.txt')

# print locations
for state in locations :

    state_total = 0
    print state
    # print locations[state]
    for city in locations[state] :
        count = locations[state][city]["count"]
        state_total = state_total + count

        print '     {0}: {1}'.format(city, count)

    print '          {0} total: {1}\n'.format(state,state_total)

set_counties(locations)

# loc = 'holland+mi'
# locCounty = getCounty(loc)
# print locCounty
