##### MODULES #####

import os
import re
import types
import json
import requests
import difflib
from decimal import *
getcontext().prec = 8


##### IMPORTS #####

# get the needed functions to create the necessary lists for ocr analysis
from global_var_and_func import offline_mode, exports_root_path, lists_root_path, ocr_lists_root_path, html_files_path, us_states_file_path, world_countries_file_path, county_ids_ratios_file_path

from lists import get_list_from_line_file, get_county_ids_ratios
from locations import get_student_locations
from stats import run_stats
from tsv_export import prepare_tsv_dictionary, export_tsv_ids_rates


##### MAIN #####

def create_lists() :

    print 'Creating the lists and dictionaries:\nus_states, world_countries, us_county_ids_ratios, and state_county_names_ids...\n'


    global us_states
    us_states = get_list_from_line_file(us_states_file_path)
    print '\nCreated us_states [list] from \'{0}\''.format(us_states_file_path)

    print_request = raw_input('Print us_states? y or n? ')
    if print_request == 'y' :
        print json.dumps(us_states, indent=4)


    global world_countries
    world_countries = get_list_from_line_file(world_countries_file_path)
    print '\n\nCreated world_countries [list] from \'{0}\''.format(world_countries_file_path)

    print_request = raw_input('Print world_countries? y or n? ')
    if print_request == 'y' :
        print json.dumps(world_countries, indent=4)


    global county_ids_ratios
    global state_county_names_ids
    county_ids_ratios, state_county_names_ids = get_county_ids_ratios(county_ids_ratios_file_path)
    print '\n\nCreating county_ids_ratios [dict] and state_county_names_ids [dict] from \'{0}\''.format(county_ids_ratios_file_path)

    print_request = raw_input('Print county_ids_ratios? y or n? ')
    if print_request == 'y' :
        print json.dumps(county_ids_ratios, indent=4)

    print_request = raw_input('\nPrint state_county_names_ids? y or n? ')
    if print_request == 'y' :
        print json.dumps(state_county_names_ids, indent=4) + '\n'


def main(exports_root_path, main_run_index) :
    ocr_files = os.listdir(ocr_lists_root_path)
    print '\nAvailable OCR text files:'
    i = 0
    for file in ocr_files :
        print '{0}: {1}'.format(i, file)
        i = i + 1

    ocr_file_index = ''
    while ocr_file_index == '' :
        ocr_file_index = raw_input('\nWhich file would you like to run the analysis on?: ')

    ocr_file_index = int(ocr_file_index)
    ocr_text_file = ocr_files[ocr_file_index]

    year = re.sub('\.txt', '', ocr_text_file)

    student_list_text_file_path = ocr_lists_root_path + ocr_text_file
    print 'Text file path: \'{0}\''.format(student_list_text_file_path)

    exports_root_path = exports_root_path + year + '/'
    print 'Export files to: \'{0}\''.format(exports_root_path)

    raw_input('\nContinue if the above paths are correct...\n')

    try:
        os.makedirs(exports_root_path)
        raw_input('Directory created: \'{0}\'\nContinue...'.format(exports_root_path))
    except OSError:
        if not os.path.isdir(exports_root_path):
            raise



    # run a new city state analysis with google api call?
    run_new = ''
    while run_new == '' :
        run_new = print_request = raw_input('\nRe-run entire analysis? y or n? ')

    # run a new analysis
    if run_new == 'y':

        def run_new_analysis(main_run_index) :

            raw_input('\nFile to be parsed: ' + student_list_text_file_path)

            global student_locations_us
            global student_locations_world
            global student_locations_bad_states
            global student_locations_bad_cities
            global student_locations_errors_other
            global student_locations_bad_counties
            global commencement_line_count

            student_locations_us, student_locations_world, student_locations_bad_states, student_locations_bad_cities, student_locations_errors_other, student_locations_bad_counties, commencement_line_count = get_student_locations(student_list_text_file_path, us_states, world_countries, state_county_names_ids, main_run_index)

            print 'Created student_locations_us [dict], student_locations_world [dict], student_locations_bad_states [dict], student_locations_bad_cities [dict], and student_locations_errors_other [list]'

            save_request = raw_input('\nSave commencement_line_count: {0}, y or n? '.format(commencement_line_count))
            if save_request != 'n' :
                commencement_line_count = str(commencement_line_count)
                path = exports_root_path + 'commencement_line_count.txt'
                with open(path, 'w') as save_file:
                    save_file.write(commencement_line_count)

            # student_locations_us
            print_request = raw_input('\nPrint student_locations_us, y or n? ')
            if print_request != 'n' :
                print json.dumps(student_locations_us, indent=4)

            save_request = raw_input('\nSave student_locations_us, y or n? ')
            if save_request != 'n' :
                path = exports_root_path + 'student_locations_us.json'
                json.dump(student_locations_us, open(path,'w'), sort_keys=True)


            # student_locations_world
            print_request = raw_input('\nPrint student_locations_world, y or n? ')
            if print_request != 'n' :
                print json.dumps(student_locations_world, indent=4)

            save_request = raw_input('\nSave student_locations_world, y or n? ')
            if save_request != 'n' :
                path = exports_root_path + 'student_locations_world.json'
                json.dump(student_locations_world, open(path,'w'), sort_keys=True)


            # student_locations_bad_states
            print_request = raw_input('\nPrint student_locations_bad_states, y or n? ')
            if print_request != 'n' :
                print json.dumps(student_locations_bad_states, indent=4)

            save_request = raw_input('\nSave student_locations_bad_states, y or n? ')
            if save_request != 'n' :
                path = exports_root_path + 'student_locations_bad_states.json'
                json.dump(student_locations_bad_states, open(path,'w'), sort_keys=True)


            # student_locations_bad_cities
            print_request = raw_input('\nPrint student_locations_bad_cities, y or n? ')
            if print_request != 'n' :
                print json.dumps(student_locations_bad_cities, indent=4)

            save_request = raw_input('\nSave student_locations_bad_cities, y or n? ')
            if save_request != 'n' :
                path = exports_root_path + 'student_locations_bad_cities.json'
                json.dump(student_locations_bad_cities, open(path,'w'), sort_keys=True)


            # student_locations_errors_other
            print_request = raw_input('\nPrint student_locations_errors_other, y or n? ')
            if print_request != 'n' :
                print json.dumps(student_locations_errors_other, indent=4)

            save_request = raw_input('\nSave student_locations_errors_other, y or n? ')
            if save_request != 'n' :
                path = exports_root_path + 'student_locations_errors_other.json'
                json.dump(student_locations_errors_other, open(path,'w'), sort_keys=True)


            # student_locations_bad_counties
            print_request = raw_input('\nPrint student_locations_bad_counties, y or n? ')
            if print_request != 'n' :
                print json.dumps(student_locations_bad_counties, indent=4)

            save_request = raw_input('\nSave student_locations_bad_counties, y or n? ')
            if save_request != 'n' :
                path = exports_root_path + 'student_locations_bad_counties.json'
                json.dump(student_locations_bad_counties, open(path,'w'), sort_keys=True)

        run_new_analysis(main_run_index)

    # already ran the analysis, use the files saved from a previous run
    else :

        raw_input('Loading dictionaries and lists from json files...')

        def load_data_from_files() :

            path = exports_root_path + 'commencement_line_count.txt'
            with open(path) as file :
                for line in file :
                    if line != '' :
                        global commencement_line_count
                        commencement_line_count = line


            path = exports_root_path + 'student_locations_us.json'
            with open(path) as json_file:
                student_locations_us = json.load(json_file)


            path = exports_root_path + 'student_locations_world.json'
            with open(path) as json_file:
                student_locations_world = json.load(json_file)


            path = exports_root_path + 'student_locations_bad_states.json'
            with open(path) as json_file:
                student_locations_bad_states = json.load(json_file)


            path = exports_root_path + 'student_locations_bad_cities.json'
            with open(path) as json_file:
                student_locations_bad_cities = json.load(json_file)


            path = exports_root_path + 'student_locations_errors_other.json'
            with open(path) as json_file:
                student_locations_errors_other = json.load(json_file)


            path = exports_root_path + 'student_locations_bad_counties.json'
            with open(path) as json_file:
                student_locations_bad_counties = json.load(json_file)

        load_data_from_files()



        def print_data_from_loaded_files() :

            # commencement_line_count
            print_request = raw_input('\nPrint commencement_line_count, y or n? ')
            if print_request != 'n' :
                print json.dumps(commencement_line_count, indent=4)


            # student_locations_us
            print_request = raw_input('\nPrint student_locations_us, y or n? ')
            if print_request != 'n' :
                print json.dumps(student_locations_us, indent=4)


            # student_locations_world
            print_request = raw_input('\nPrint student_locations_world, y or n? ')
            if print_request != 'n' :
                print json.dumps(student_locations_world, indent=4)


            # student_locations_bad_states
            print_request = raw_input('\nPrint student_locations_bad_states, y or n? ')
            if print_request != 'n' :
                print json.dumps(student_locations_bad_states, indent=4)


            # student_locations_bad_cities
            print_request = raw_input('\nPrint student_locations_bad_cities, y or n? ')
            if print_request != 'n' :
                print json.dumps(student_locations_bad_cities, indent=4)


            # student_locations_errors_other
            print_request = raw_input('\nPrint student_locations_errors_other, y or n? ')
            if print_request != 'n' :
                print json.dumps(student_locations_errors_other, indent=4)


            # student_locations_bad_counties
            print_request = raw_input('\nPrint student_locations_bad_counties, y or n? ')
            if print_request != 'n' :
                print json.dumps(student_locations_bad_counties, indent=4)


        print_data_from_loaded_files()


    run_stats(commencement_line_count, student_locations_us, student_locations_world, student_locations_bad_states, student_locations_bad_cities, student_locations_errors_other, student_locations_bad_counties)

    tsv_file_name = 'students_by_county_' + year + '.tsv'
    tsv_export_path = html_files_path

    student_county_ids_ratios, tsv_file_stats = prepare_tsv_dictionary(county_ids_ratios, student_locations_us)

    export_tsv_ids_rates(student_county_ids_ratios, tsv_export_path, tsv_file_name, tsv_file_stats)


# let the user know that google api calls will be not actually be made
# counties will be randomly assigned from a set of predefined list
if offline_mode == True :
    raw_input('\nOffline Mode: On\n')
run_main = raw_input('Welcome. Let\'s do this.\n')

# Run the main program
main_run_index = 0
run_main = 'y'
while run_main == 'y' :

    if main_run_index == 0 :
        create_lists()

    main(exports_root_path, main_run_index)

    run_main = raw_input('Want to run the program again, y or n ? ')

    main_run_index = main_run_index + 1

print '\nSee you later.'
