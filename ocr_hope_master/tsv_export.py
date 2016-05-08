import json
from decimal import *
getcontext().prec = 8

def prepare_tsv_dictionary(county_ids_ratios, student_locations_us) :

    # count total students for rate calculation first
    total_count = 0
    for state in student_locations_us :
        for city in student_locations_us[state] :
            city_student_count = student_locations_us[state][city]["count"]
            total_count = total_count + city_student_count

    print 'Total student count from student locations: {0}'.format(total_count)

    max_rate = float(0)
    rate_sum = float(0)
    number_of_counties_count = 0

    # setup an empty dicitonary to keep the county ids as keys and their total count as values
    county_ids_count = {}

    # run through locations and collect cities count into county ids
    for state in student_locations_us :
        for city in student_locations_us[state] :

            # if there is a county_id, just to make sure
            if 'county_id' in student_locations_us[state][city] :

                # get the county id and count values
                county_id = student_locations_us[state][city]["county_id"]
                city_student_count = student_locations_us[state][city]["count"]

                # check if the county_id is already present in the dictionary
                if county_id in county_ids_count :
                    prev_count = county_ids_count[county_id]
                    county_ids_count[county_id] = prev_count + city_student_count

                # add the county id and count to the dicitonary
                else :
                    county_ids_count[county_id] = city_student_count

    # total count of students from county_ids_count dicitonary
    total_county_count = 0
    for county_id in county_ids_count :
        total_county_count = total_county_count + county_ids_count[county_id]
    print 'Total student count from county ids count dictionary: {0}'.format(total_county_count)

    # pause for a sec, check integrity of both lists
    raw_input('...compare the totals\n')

    # copy the county_ids_ratios dictionary (0.0 as rates) for manipulation and value replacement
    student_county_ids_ratios = county_ids_ratios

    # run through county_ids_count and replace rates in student_county_ids_ratios
    for county_id in county_ids_count :

        # get the count from the dictionary
        single_county_count = county_ids_count[county_id]

        # set the county rate
        county_rate = float(single_county_count)/float(total_county_count)

        # check to see if the county_id is in the final dictionary of ids and rates
        if county_id in student_county_ids_ratios :
            # replace the 0.0 rates for the county id with the new rate value
            student_county_ids_ratios[county_id] = county_rate

        # check for the max rate
        if county_rate > max_rate :
            max_rate = county_rate
            # print 'New max_rate found:'
            # print 'County ID: {0}'.format(county_id)
            # print 'County Count: {0}'.format(single_county_count)
            # print 'Total County Count: {0}'.format(total_county_count)
            # print 'County Rate: {0}\n'.format(county_rate)

        # checking loop and integrity of data with some math
        rate_sum = rate_sum + county_rate
        number_of_counties_count = number_of_counties_count + 1

    tsv_file_stats = ''
    tsv_file_stats = tsv_file_stats + '\nTSV File stats:\n'
    tsv_file_stats = tsv_file_stats + 'Max rate: {0:.5f}\n'.format(max_rate)
    tsv_file_stats = tsv_file_stats + 'Rate sum: {0}\n'.format(rate_sum)
    tsv_file_stats = tsv_file_stats + 'Number of counties : {0}\n'.format(number_of_counties_count)
    tsv_file_stats = tsv_file_stats + 'Average rate: {0:.5f}\n'.format(float(rate_sum)/float(number_of_counties_count))

    return (student_county_ids_ratios, tsv_file_stats)


def export_tsv_ids_rates(student_county_ids_ratios, tsv_export_path, tsv_file_name, tsv_file_stats) :

    # setup the first line of the output
    output = 'id' + '\t' + 'rate' + '\n'

    # run through student_county_ids_ratios and print out tsv file
    for county_id in student_county_ids_ratios :
        # get the rate value
        county_rate = student_county_ids_ratios[county_id]
        # prep the new line
        add_line = "{0}\t{1}\n".format(county_id, county_rate)
        # add the new line to the output variable
        output += add_line

    # setup the file parameters
    file_full_path = tsv_export_path + tsv_file_name
    save_file = open(file_full_path, 'w')

    # save the output variable to the file
    for line in output:
        save_file.write(line)

    # show the success
    print '\nCreated \'{0}\' file created in \'{1}\''.format(tsv_file_name, tsv_export_path)
    # show stats of tsv file
    print tsv_file_stats
