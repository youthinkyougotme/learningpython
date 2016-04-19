import re

def get_world_countries() :

    world_countries = []

    with open('lists/world_countries.txt') as countries_file :
        for line in countries_file:
            line = re.sub('\s', '', line).lower()
            world_countries.append(line)

    return world_countries


def get_us_states() :

    us_states =[]

    with open('lists/us_states.txt') as us_states_file :
        for line in us_states_file :
            line = re.sub('\s','',line)
            us_states.append(line.lower())

    return us_states
