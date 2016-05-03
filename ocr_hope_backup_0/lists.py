import re

def get_world_countries() :

    world_countries = []

    with open('lists/world_countries.txt') as countries_file :
        for line in countries_file:
            line = re.sub('\s', '', line).lower()
            world_countries.append(line)

    return world_countries


def get_us_states() :

    us_states = []

    with open('lists/us_states.txt') as us_states_file :
        for line in us_states_file :
            line = re.sub('\s','',line)
            us_states.append(line.lower())

    return us_states



def get_us_counties(file) :

    us_states = get_us_states()
    us_states_counties_ids = {}
    joined_lines = ''

    with open(file) as us_counties_file :

        for line in us_counties_file :
            joined_lines = joined_lines + line

        joined_lines_parts = re.split('#', joined_lines)

        for entry in joined_lines_parts :

            entry_parts = re.split('\n', entry)

            index = 0
            current_state_name = ''
            for entry in entry_parts :

                if entry != '' :

                    if index == 0 :

                        id_county_pair = re.split('\t',entry)
                        current_state_name = id_county_pair[1].lower()
                        current_state_name = re.sub('\s', '', current_state_name)

                        us_states_counties_ids[current_state_name] = {}

                    if index >= 1 :
                        id_county_pair = re.split('\t',entry)
                        county_id = int(id_county_pair[0])
                        county_name = id_county_pair[1]

                        us_states_counties_ids[current_state_name][county_name] = county_id

                    index = index + 1

    return us_states_counties_ids
