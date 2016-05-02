##### GLOBAL VARIABLES ####
exports_root_path = 'lists/export/'
lists_root_path = 'lists/sources/'
ocr_lists_root_path = lists_root_path + 'ocr/'
html_files_path = 'html/files/'
us_states_file_path = lists_root_path + 'us_states.txt'
world_countries_file_path = lists_root_path + 'world_countries.txt'
county_ids_ratios_file_path = lists_root_path + 'us_county_ids_names.tsv'

global offline_mode
offline_mode = False

saved_google_city_state_county_responses = {}

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
