##### MODULES #####

import re
import types
import json
import requests
import difflib
from decimal import *
getcontext().prec = 8


##### IMPORTS #####

# get the needed functions to create the necessary lists for ocr analysis
from lists import get_list_from_line_file, get_county_ids_ratios
from locations import get_student_locations
from stats import run_stats
from file_exports import export_tsv_ids_rates

##### GLOBAL VARIABLES ####

list_root_path = 'lists/sources/'
student_list_path = list_root_path + '2014.txt'
us_states_file_path = list_root_path + 'us_states.txt'
world_countries_file_path = list_root_path + 'world_countries.txt'
county_ids_ratios_file_path = list_root_path + 'us_county_ids_names.tsv'


##### MAIN #####

raw_input('Welcome.')
print 'Creating the list variables: us_states, world_countries, us_county_ids_ratios...'

us_states = get_list_from_line_file(us_states_file_path)
print '\nCreated us_states [list] from \'{0}\'\n'.format(us_states_file_path)
print_request = raw_input('Print us_states? y or n? ')
if print_request == 'y' :
    print us_states

world_countries = get_list_from_line_file(world_countries_file_path)
print '\nCreated world_countries [list] from \'{0}\'\n'.format(world_countries_file_path)
print_request = raw_input('Print world_countries? y or n? ')
if print_request == 'y' :
    print world_countries

county_ids_ratios, state_county_names_ids = get_county_ids_ratios(county_ids_ratios_file_path)
print '\nCreating county_ids_ratios [dict] and state_county_names_ids [dict] from \'{0}\'\n'.format(county_ids_ratios_file_path)

print_request = raw_input('Print county_ids_ratios? y or n? ')
if print_request == 'y' :
    print county_ids_ratios

print_request = raw_input('Print state_county_names_ids? y or n? ')
if print_request == 'y' :
    print state_county_names_ids

raw_input('\n\nFile to be parsed: ' + student_list_path)

student_locations_us, student_locations_world, student_locations_bad_states, student_locations_bad_cities, student_locations_errors_other, student_locations_bad_counties, commencement_line_count = get_student_locations(student_list_path, us_states, world_countries, state_county_names_ids)

print 'Created student_locations_us [dict], student_locations_world [dict], student_locations_bad_states [dict], student_locations_bad_cities [dict], and student_locations_errors_other [list]'

print_request = raw_input('\nPrint student_locations_us? y or n? ')
if print_request == 'y' :
    print student_locations_us

save_request = raw_input('\nSave student_locations_us? y or n? ')
if save_request == 'y' :
    json.dump(student_locations_us, open("lists/export/student_locations_us.json",'w'), sort_keys=True)

print_request = raw_input('\nPrint student_locations_world? y or n? ')
if print_request == 'y' :
    print student_locations_world

print_request = raw_input('\nPrint student_locations_bad_states? y or n? ')
if print_request == 'y' :
    print student_locations_bad_states

print_request = raw_input('\nPrint student_locations_bad_cities? y or n? ')
if print_request == 'y' :
    print student_locations_bad_cities

print_request = raw_input('\nPrint student_locations_errors_other? y or n? ')
if print_request == 'y' :
    print student_locations_errors_other

print_request = raw_input('\nPrint student_locations_bad_counties? y or n? ')
if print_request == 'y' :
    print student_locations_bad_counties

run_stats(commencement_line_count, student_locations_us, student_locations_world, student_locations_bad_states, student_locations_bad_cities, student_locations_errors_other, student_locations_bad_counties)


export_tsv_ids_rates(county_ids_ratios, student_locations_us, 'html/files/', 'students_by_county.tsv')
