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

##### GLOBAL VARIABLES ####

list_root_path = 'lists/sources/'
student_list_path = list_root_path + '2014.txt'
us_states_file_path = list_root_path + 'us_states.txt'
world_countries_file_path = list_root_path + 'world_countries.txt'
county_ids_ratios_file_path = list_root_path + 'us_county_ids_names.tsv'


##### MAIN #####

raw_input('Welcome.')
print 'Creating the list variables: us_states, world_countries, us_county_ids_ratios...\n'

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

county_ids_ratios = get_county_ids_ratios(county_ids_ratios_file_path)
print '\nCreated county_ids_ratios [dict] from \'{0}\'\n'.format(county_ids_ratios_file_path)
print_request = raw_input('Print county_ids_ratios? y or n? ')
if print_request == 'y' :
    print county_ids_ratios

raw_input('\n\nFile to be parsed: ' + student_list_path)

student_locations_us, student_locations_world, student_locations_bad_states, student_locations_bad_cities, student_locations_errors_other = get_student_locations(student_list_path, us_states, world_countries)

print 'Created student_locations_us [dict], student_locations_world [dict], student_locations_bad_states [dict], student_locations_bad_cities [dict], and student_locations_errors_other [list]'

print_request = raw_input('\nPrint student_locations_us? y or n? ')
if print_request == 'y' :
    print student_locations_us

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

run_stats(student_locations_us, student_locations_world, student_locations_bad_states, student_locations_bad_cities, student_locations_errors_other)
