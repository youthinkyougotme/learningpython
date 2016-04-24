# --------- imports ---------
import re
import types
import json
import requests
import difflib
from decimal import *
getcontext().prec = 8


verbose = False
us_states_file_path = 'lists/sources/us_states.txt'
world_countries_file_path = 'lists/sources/world_countries.txt'
county_ids_ratios_file_path = 'lists/sources/us_county_ids_names.tsv'
##### IMPORTS #####

# get the needed functions to create the necessary lists for ocr analysis
from lists import get_list_from_line_file, get_county_ids_ratios, create_json_file

from locations import get_locations
from googleapi import set_counties


##### MAIN #####


input_run_lists = raw_input('Welcome.')

print 'Creating the list variables: us_states, world_countries, us_county_ids_ratios...'

us_states = get_list_from_line_file(us_states_file_path)
print 'Created us_states [list] from \'{0}\'\n'.format(us_states_file_path)

world_countries = get_list_from_line_file(world_countries_file_path)
print 'Created world_countries [list] from \'{0}\'\n'.format(world_countries_file_path)

county_ids_ratios = get_county_ids_ratios(county_ids_ratios_file_path)
print 'Created county_ids_ratios list'


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

create_states_counties_ids = raw_input("Run get_us_counties_ids, y or n? ").rstrip()
if create_states_counties_ids == 'y' :
    # us_states_counties_ids is a dictionary of state dicts of country name keys and id values
    us_states_counties_ids = get_us_counties('lists/us_counties.tsv')
    # write the states counties ids dictionary to a text file
    json.dump(us_states_counties_ids, open("lists/us_states_counties_ids.json",'w'), sort_keys=True)

else :
    with open("lists/us_states_counties_ids.json") as json_file:
        us_states_counties_ids = json.load(json_file)

print '------------------\n'
print '------------------\n'
print us_states_counties_ids

create_locations = raw_input("Run get_locations and set_counties, y or n? ").rstrip()
if create_locations == 'y' :
    # locations is a dictionary of state dicts of city dictionaries
    locations = get_locations('lists/2014.txt')
    # get the county for the city, state and add it to the city dictionary
    set_counties(locations)
    # write the locations dictionary to a text file
    json.dump(locations, open("lists/locations.json",'w'), sort_keys=True)

else :
    with open("lists/locations.json") as json_file:
        locations = json.load(json_file)

raw_input('gotcha, here we go...')

print '------------------'
print '------------------\n'
print locations
raw_input('printed locations...')

print '------------------'
print '------------------\n'



def set_county_ids() :

    county_populations = {}

    total_errors = 0
    state_not_in_state_count = 0
    county_not_in_state_count = 0
    county_in_state_count = 0
    # using locations dictionary & us_states_counties_ids dictionary


    for state in locations :

        state_name = state.encode('UTF-8')
        print state_name

        # print type(state)
        # raw_input('printed state...')

        # print locations[state]
        # print type(locations[state])
        # raw_input('printed locations[state]...')

        for city in locations[state] :
            print city
            # print type(city)
            # raw_input('printed city...')

            # print locations[state][city]
            # print type(locations[state][city])
            # raw_input('printed locations[state][city]...')

            county_name = locations[state][city]["county_name"].encode('UTF-8')
            county_count = locations[state][city]["count"]

            print county_name
            print county_count
            print '\n'

            # print type(locations[state][city]["county_name"])
            # raw_input('printed locations[state][city]["county_name"]...')


            if state_name in us_states_counties_ids :
                print 'state in us_states_counties_ids'
                print us_states_counties_ids[state_name]

                if county_name in us_states_counties_ids[state_name] :
                    print '{0} county in state'.format(county_name)

                    county_id = us_states_counties_ids[state_name][county_name]
                    print county_id

                    locations[state_name][city]["county_id"] = county_id

                    if county_name not in county_populations :
                        county_populations[county_id] = 0

                    # print county_populations
                    county_in_state_count = county_in_state_count + 1

                else :
                    locations[state_name][city]["county_id"] = 'none'

                    print '{0} county not found in state'.format(county_name)
                    county_not_in_state_count = county_not_in_state_count + 1
            else :
                print 'state not in us_states_counties_ids'
                state_not_in_state_count = state_not_in_state_count + 1


            #raw_input('in us_states_counties_ids?')

    total_errors = county_not_in_state_count + state_not_in_state_count
    print 'success: {0}'.format(county_in_state_count)
    print 'errors: {0}'.format(total_errors)

    return county_populations

raw_input('run set_county_ids()...')
county_populations = set_county_ids()
print county_populations
raw_input('ran set_county_ids()...')



print '------------------'
print '------------------\n'

print locations["michigan"]

print '------------------'
print '------------------\n'


for state in locations :

    for city in locations[state] :

        city_stuff = county_id = locations[state][city]
        print city_stuff
        county_id = locations[state][city]["county_id"]

        if county_id != 'none' :

            print county_id
            county_count = locations[state][city]["count"]
            print county_count

            current_count = county_populations[county_id]
            print current_count
            county_populations[county_id] = current_count + county_count
            print county_populations[county_id]
            print county_populations

    # raw_input('did it work?')

total_county_id_count = 0
for entry in county_populations :
    count = county_populations[entry]
    print count
    total_county_id_count = total_county_id_count + count
    print 'running total: {0}\n'.format(total_county_id_count)

print '\nfinal county total: {0}'.format(total_county_id_count)


output = 'id' + '\t' + 'rate' + '\n'
max_ratio = float(0)

for item in county_populations :
    id_number = item
    id_count = county_populations[item]

    # print type(id_count)
    # print type(total_county_id_count)

    ratio = float(id_count)/float(total_county_id_count)
    # print type(ratio)
    # print ratio

    #raw_input('hault')

    if ratio > max_ratio :
        max_ratio = ratio

    save = "{0}\t{1}\n".format(id_number, ratio)
    print save
    output+=save

print 'max ratio: {0}'.format(max_ratio)
save_file = open('lists/students_by_county.tsv', 'w')
for each in output:
    save_file.write(each)
