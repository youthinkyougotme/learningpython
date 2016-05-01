import re
import json
import requests
import time
import random

from global_var_and_func import offline_mode, key_value_to_dictionary


# get the county name using google maps api
def get_county(city, state) :
    ## location variable
    # format: '<cityname>+<state>'
    # loc = 'holland+michigan'

    loc = city + '+' + state
    print '\nGoogle API locaiton lookup: {0}'.format(loc)
    ## setup api get requests
    # format example:
    # http://maps.googleapis.com/maps/api/geocode/json?address=holland+mi
    api_url = 'http://maps.googleapis.com/maps/api/geocode/json?address='+loc

    # if not offline_mode, actually going out to look up the city state pair county
    if not offline_mode :

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
        print 'API call response: {0}'.format(api_status)

        # if there is an api response
        if api_status == 'OK' :

            # extract long form address
            # api_addr = api_data["results"][0]["formatted_address"]
            # print api_addr
            # print type(api_addr)

            # get the address components, contains levels from city > township > county > state > country > zip
            address_components = api_data["results"][0]["address_components"]
            print 'Location API address components:\n{0}'.format(address_components)


            # set the default index value where the county is typically found
            county_name_index = 1
            # set index value, use it to loop through the address_components list
            list_index = 0
            # for each compoenet of the address_components
            for component in address_components :

                # print address component index and its value
                print '\nAt index: {0}'.format(list_index)
                print component

                # get the level of government that the address component is associated with (state, city, county, etc)
                address_component_types = address_components[list_index]["types"]

                # make sure the component type is not empty
                if len(address_component_types) != 0 :

                    # print the component types
                    print 'Component types: {0}'.format(address_component_types)

                    # position zero of the component type is most distinct and descriptive
                    component_type_first = address_component_types[0]
                    print 'Component type[0]: {0}'.format(component_type_first)

                    # check if the current address component is the county level of goverment, i.e. the county
                    if component_type_first == 'administrative_area_level_2':

                        # save the index value as the index value where the county name is found
                        county_name_index = list_index
                        # print 'The index value of the county address component is: {0}'.format(county_name_index)

                # end of loop, increment the index value
                list_index = list_index + 1

            print 'The address component index of interest: {0}'.format(county_name_index)

            # extract the county name from the address components
            api_county = api_data["results"][0]["address_components"][county_name_index]["long_name"]

            print 'Google API says that the county of {0}, {1} is: {2}'.format(city, state, api_county)
            # print type(api_county)

        # return the county name given from the google api call
        return api_county

    # in offline_mode, so just fake the county results via a randomization of the following counties
    else :
        #random_counties = {'Autauga': 1001, 'Lumpkin': 13187, 'Kearny': 20093}
        random_counties = {'Autauga': 1001, 'Lumpkin': 13187, 'Kearny': 20093, 'Tazewell': 51185, 'North Slope': 2185, 'Montague': 48337, 'Harris': 48201, 'Barber': 20007, 'Hopewell': 51670, 'Sanpete': 49039, 'Wilcox': 13315, 'Hickory': 29085, 'Mobile': 1097, 'Clatsop': 41007, 'Del Norte': 6015, 'Columbiana': 39029, 'Penobscot': 23019, 'Saunders': 31155, 'Corozal': 72047, 'Pondera': 30073, 'Deer Lodge': 30023, 'Milam': 48331, 'Stutsman': 38093, 'Starr': 48427, 'Coconino': 4005, 'Nacogdoches': 48347, 'Holt': 31089, 'Hot Springs': 56017, 'Ward': 48475, 'Ware': 13299, 'Mille Lacs': 27095, 'Poinsett': 5111, 'Jaluit': 68120, 'Deschutes': 41017, 'Rota': 69100, 'Clinton': 42035, 'Mingo': 54059, 'Morris': 48343, 'Echols': 13101, 'Marinette': 55075, 'Cooper': 29053, 'Swains Island': 60040, 'Cherokee': 48073, 'Bayfield': 55007, 'Wibaux': 30109, 'Indian River': 12061, 'Vega Baja': 72145, 'Cowlitz': 53015, 'Muscogee': 13215, 'Attala': 28007, 'Medina': 48325, 'Sangamon': 17167, 'Hanson': 46061, 'Mesa': 8077, 'Clifton Forge': 51560, 'Ngernmlengui': 70227, 'Wakulla': 12129, 'Alexander': 37003, 'Pike': 42103, 'Koror': 78150, 'De Soto': 22031, 'La Crosse': 55063, 'Sherburne': 27141, 'Payette': 16075, 'Charleston': 45019, 'Skagit': 53057, 'Muskogee': 40101, 'Craig': 51045, 'Copiah': 28029, 'Carroll': 51035, 'Oswego': 36075, 'Ailinglaplap': 68010, 'Gogebic': 26053, 'Lubbock': 48303, 'Sumter': 45085, 'Dutchess': 36027, 'DeKalb': 47041, 'Williams': 39171, 'Oscoda': 26135, 'Marengo': 1091, 'Le Flore': 40079, 'Cochran': 48079, 'Roscommon': 26143, 'Washoe': 32031, 'Macoupin': 17117, 'Caledonia': 50005, 'Bartholomew': 18005, 'Conecuh': 1035, 'Lynn': 48305, 'Wise': 51195, 'Dooly': 13093, 'Cape Girardeau': 29031, 'Whiteside': 17195, 'Benton': 53005, 'Luce': 26095, 'Bikini': 68070, 'Faulk': 46049, 'San Bernardino': 6071, 'Warrick': 18173, 'Bond': 17005, 'Galveston': 48167, 'Lewis and Clark': 30049, 'Lewis': 54041, 'Bulloch': 13031, 'Bullock': 1011, 'Garfield': 53023}

        # randomize the result
        api_county = random.choice(random_counties.keys())

        # return the county name given from the google api call
        return api_county



# take the state as parent, the city as child, the
def set_city_info(dictionary, state, city, state_county_names_ids, student_locations_bad_counties, student_locations_bad_cities, main_run_index) :

    print 'Main runs: {0}'.format(main_run_index)

    # get and set county name according to the city and state provided
    county_name = get_county(city, state)

    # remove county and possible township words from full county name
    county_name = re.sub('\sCounty','',county_name)
    # county_name = re.sub('\sTownship','',county_name)


    # if the county_name is not empty
    if county_name != '' :


        # if the county name is in the dictionary of acceptable state : counties key value pairs
        if county_name in state_county_names_ids[state] :
            # there is a direct match of the county name key within the state parent key

            # add the city, state passed into the function to the passed dictionary
            key_value_to_dictionary(state, city, dictionary)

            # add the county name and id to the city in that dicitonary
            dictionary[state][city]["county_name"] = county_name
            dictionary[state][city]["county_id"] = state_county_names_ids[state][county_name]


        #  if the county name is not in the dictionary of acceptable state : counties key value pairs
        elif county_name not in state_county_names_ids[state] :
            bad_county = {}
            bad_county["city"] = city
            bad_county["state"] = state
            bad_county["county_name"] = county_name
            student_locations_bad_counties.append(bad_county)


        # anything else, log into this list, a possible bad city state combination was given
        else :
            bad_city = {}
            bad_city["city"] = city
            bad_city["state"] = state
            student_locations_bad_cities.append(bad_city)


    # if the county name is empty, a possible bad city state combination was given
    else :
        county_name = 'empty'
        bad_county = {}
        bad_county["city"] = city
        bad_county["state"] = state
        bad_county["county_name"] = county_name
        student_locations_bad_counties.append(bad_county)
