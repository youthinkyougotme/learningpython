import re
from decimal import *
getcontext().prec = 8

# function to create list from line seperated file
def get_list_from_line_file(file) :

    output_list = []

    with open(file) as file :

        for line in file :
            line = re.sub('\s','',line)
            output_list.append(line.lower())

    return output_list



def get_county_ids_ratios(file) :

    joined_lines = ''
    county_ids_ratios = {}
    state_county_names_ids = {}

    with open(file) as county_ids_names_file :

        for line in county_ids_names_file :

            line = line.rstrip()

            if line != '#' :

                line_parts = re.split('\t', line)
                county_id = int(line_parts[0])
                county_name = line_parts[1]

                if county_id % 1000 == 0 :
                    state = county_name
                    state = re.sub('\s','',state)
                    state = state.lower()
                    state_county_names_ids[state] = {}

                if county_id % 1000 != 0 :
                    county_ids_ratios[county_id] = float(0)

                    state_county_names_ids[state][county_name] = county_id


    return (county_ids_ratios, state_county_names_ids)


def create_json_file(dictionary, file_path) :

    json.dump(dictionary, open(file_path,'w'), sort_keys=True)
