import re
import json
import requests
import time
import random

# get the county name using google maps api
def get_county(city, state) :
    ## location variable
    # format: '<cityname>+<stateabbre>'
    # loc = 'holland+mi'

    loc = city + '+' + state

    ## setup api get requests
    # format example:
    # http://maps.googleapis.com/maps/api/geocode/json?address=holland+mi
    api_url = 'http://maps.googleapis.com/maps/api/geocode/json?address='+loc

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

        # extract county name
        api_county = api_data["results"][0]["address_components"][1]["short_name"]
        # print api_county
        # print type(api_county)

    else :
        #random_counties = {'Autauga': 1001}
        random_counties = {'Autauga': 1001, 'Lumpkin': 13187, 'Kearny': 20093, 'Tazewell': 51185, 'North Slope': 2185, 'Montague': 48337, 'Harris': 48201, 'Barber': 20007, 'Hopewell': 51670, 'Sanpete': 49039, 'Wilcox': 13315, 'Hickory': 29085, 'Mobile': 1097, 'Clatsop': 41007, 'Del Norte': 6015, 'Columbiana': 39029, 'Penobscot': 23019, 'Saunders': 31155, 'Corozal': 72047, 'Pondera': 30073, 'Deer Lodge': 30023, 'Milam': 48331, 'Stutsman': 38093, 'Starr': 48427, 'Coconino': 4005, 'Nacogdoches': 48347, 'Holt': 31089, 'Hot Springs': 56017, 'Ward': 48475, 'Ware': 13299, 'Mille Lacs': 27095, 'Poinsett': 5111, 'Jaluit': 68120, 'Deschutes': 41017, 'Rota': 69100, 'Clinton': 42035, 'Mingo': 54059, 'Morris': 48343, 'Echols': 13101, 'Marinette': 55075, 'Cooper': 29053, 'Swains Island': 60040, 'Cherokee': 48073, 'Bayfield': 55007, 'Wibaux': 30109, 'Indian River': 12061, 'Vega Baja': 72145, 'Cowlitz': 53015, 'Muscogee': 13215, 'Attala': 28007, 'Medina': 48325, 'Sangamon': 17167, 'Hanson': 46061, 'Mesa': 8077, 'Clifton Forge': 51560, 'Ngernmlengui': 70227, 'Wakulla': 12129, 'Alexander': 37003, 'Pike': 42103, 'Koror': 78150, 'De Soto': 22031, 'La Crosse': 55063, 'Sherburne': 27141, 'Payette': 16075, 'Charleston': 45019, 'Skagit': 53057, 'Muskogee': 40101, 'Craig': 51045, 'Copiah': 28029, 'Carroll': 51035, 'Oswego': 36075, 'Ailinglaplap': 68010, 'Gogebic': 26053, 'Lubbock': 48303, 'Sumter': 45085, 'Dutchess': 36027, 'DeKalb': 47041, 'Williams': 39171, 'Oscoda': 26135, 'Marengo': 1091, 'Le Flore': 40079, 'Cochran': 48079, 'Roscommon': 26143, 'Washoe': 32031, 'Macoupin': 17117, 'Caledonia': 50005, 'Bartholomew': 18005, 'Conecuh': 1035, 'Lynn': 48305, 'Wise': 51195, 'Dooly': 13093, 'Cape Girardeau': 29031, 'Whiteside': 17195, 'Benton': 53005, 'Luce': 26095, 'Bikini': 68070, 'Faulk': 46049, 'San Bernardino': 6071, 'Warrick': 18173, 'Bond': 17005, 'Galveston': 48167, 'Lewis and Clark': 30049, 'Lewis': 54041, 'Bulloch': 13031, 'Bullock': 1011, 'Garfield': 53023}

        api_county = random.choice(random_counties.keys())

    return api_county
