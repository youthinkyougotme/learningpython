import re
import json
import requests
import time
import random


def key_value_to_dictionary(this_key, this_value, this_dict) :

    # add state to states dictionary if not there already
    if this_key not in this_dict :
        this_dict[this_key] = dict()

    # add city to corresponding state dictionary if not there already
    if this_value not in this_dict[this_key] :
        this_dict[this_key][this_value] = dict()
        # set the count of the city to 1
        this_dict[this_key][this_value]["count"] = 1;
    else :
        # the city is already in the corresponding state dictionary
        # set and increment the city count
        current_count = this_dict[this_key][this_value]["count"]
        this_dict[this_key][this_value]["count"] = current_count + 1




offline_mode = False

# get the county name using google maps api
def get_county(city, state) :
    ## location variable
    # format: '<cityname>+<stateabbre>'
    # loc = 'holland+mi'

    loc = city + '+' + state
    print loc
    ## setup api get requests
    # format example:
    # http://maps.googleapis.com/maps/api/geocode/json?address=holland+mi
    api_url = 'http://maps.googleapis.com/maps/api/geocode/json?address='+loc

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
        print 'API response: ' + api_status

        if api_status == 'OK' :
            # extract long form address
            api_addr = api_data["results"][0]["formatted_address"]
            # print api_addr
            # print type(api_addr)

            address_components = api_data["results"][0]["address_components"]
            print address_components
            index = 0
            county_name_index = 1
            for component in address_components :
                print index
                print component
                area_types = address_components[index]["types"]

                if len(area_types) != 0 :
                    print area_types
                    print area_types[0]
                    if area_types[0] == 'administrative_area_level_2':
                        county_name_index = index
                        print 'count_name_index is: {0}'.format(county_name_index)
                index = index + 1

            print 'target address component index: {0}'.format(county_name_index)

            # extract county name
            api_county = api_data["results"][0]["address_components"][county_name_index]["long_name"]
            print 'county found: {0}'.format(api_county)
            # print type(api_county)

        return api_county

    else :
        #random_counties = {'Autauga': 1001, 'Lumpkin': 13187, 'Kearny': 20093}
        random_counties = {'Autauga': 1001, 'Lumpkin': 13187, 'Kearny': 20093, 'Tazewell': 51185, 'North Slope': 2185, 'Montague': 48337, 'Harris': 48201, 'Barber': 20007, 'Hopewell': 51670, 'Sanpete': 49039, 'Wilcox': 13315, 'Hickory': 29085, 'Mobile': 1097, 'Clatsop': 41007, 'Del Norte': 6015, 'Columbiana': 39029, 'Penobscot': 23019, 'Saunders': 31155, 'Corozal': 72047, 'Pondera': 30073, 'Deer Lodge': 30023, 'Milam': 48331, 'Stutsman': 38093, 'Starr': 48427, 'Coconino': 4005, 'Nacogdoches': 48347, 'Holt': 31089, 'Hot Springs': 56017, 'Ward': 48475, 'Ware': 13299, 'Mille Lacs': 27095, 'Poinsett': 5111, 'Jaluit': 68120, 'Deschutes': 41017, 'Rota': 69100, 'Clinton': 42035, 'Mingo': 54059, 'Morris': 48343, 'Echols': 13101, 'Marinette': 55075, 'Cooper': 29053, 'Swains Island': 60040, 'Cherokee': 48073, 'Bayfield': 55007, 'Wibaux': 30109, 'Indian River': 12061, 'Vega Baja': 72145, 'Cowlitz': 53015, 'Muscogee': 13215, 'Attala': 28007, 'Medina': 48325, 'Sangamon': 17167, 'Hanson': 46061, 'Mesa': 8077, 'Clifton Forge': 51560, 'Ngernmlengui': 70227, 'Wakulla': 12129, 'Alexander': 37003, 'Pike': 42103, 'Koror': 78150, 'De Soto': 22031, 'La Crosse': 55063, 'Sherburne': 27141, 'Payette': 16075, 'Charleston': 45019, 'Skagit': 53057, 'Muskogee': 40101, 'Craig': 51045, 'Copiah': 28029, 'Carroll': 51035, 'Oswego': 36075, 'Ailinglaplap': 68010, 'Gogebic': 26053, 'Lubbock': 48303, 'Sumter': 45085, 'Dutchess': 36027, 'DeKalb': 47041, 'Williams': 39171, 'Oscoda': 26135, 'Marengo': 1091, 'Le Flore': 40079, 'Cochran': 48079, 'Roscommon': 26143, 'Washoe': 32031, 'Macoupin': 17117, 'Caledonia': 50005, 'Bartholomew': 18005, 'Conecuh': 1035, 'Lynn': 48305, 'Wise': 51195, 'Dooly': 13093, 'Cape Girardeau': 29031, 'Whiteside': 17195, 'Benton': 53005, 'Luce': 26095, 'Bikini': 68070, 'Faulk': 46049, 'San Bernardino': 6071, 'Warrick': 18173, 'Bond': 17005, 'Galveston': 48167, 'Lewis and Clark': 30049, 'Lewis': 54041, 'Bulloch': 13031, 'Bullock': 1011, 'Garfield': 53023}

        api_county = random.choice(random_counties.keys())

        return api_county




def set_city_info(dictionary, state, city, state_county_names_ids, student_locations_bad_counties, student_locations_bad_cities) :


    # get and set county name according to the city and state provided
    county_name = get_county(city, state)

    # remove county and township words from county name
    county_name = re.sub('\sCounty','',county_name)
    county_name = re.sub('\sTownship','',county_name)

    if county_name in state_county_names_ids[state] :

        # there is a direct match with the us_states list
        key_value_to_dictionary(state, city, dictionary)

        # add the county name and id to the city in dicitonary
        dictionary[state][city]["county_name"] = county_name
        dictionary[state][city]["county_id"] = state_county_names_ids[state][county_name]

    elif county_name != '' and county_name not in state_county_names_ids[state] :
        bad_county = {}
        bad_county["city"] = city
        bad_county["state"] = state
        bad_county["county_name"] = county_name
        student_locations_bad_counties.append(bad_county)

    else :
        bad_city = {}
        bad_city["city"] = city
        bad_city["state"] = state
        student_locations_bad_cities.append(bad_city)
