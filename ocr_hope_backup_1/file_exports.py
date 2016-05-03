import json

from decimal import *
getcontext().prec = 8

def export_tsv_ids_rates(county_ids_ratios, student_locations_us, tsv_export_path, tsv_file_name) :

    # count total students for rate calculation first
    total_count = 0
    for state in student_locations_us :
        for city in student_locations_us[state] :
            city_student_count = student_locations_us[state][city]["count"]
            total_count = total_count + city_student_count

    print total_count
    raw_input('total_count from cities')

    max_rate = float(0)
    rate_sum = float(0)
    counties_count = 0


    county_ids_count = {}
    # run through locations and collect cities count into county ids
    for state in student_locations_us :
        for city in student_locations_us[state] :

            if 'county_id' in student_locations_us[state][city] :

                county_id = student_locations_us[state][city]["county_id"]
                city_student_count = student_locations_us[state][city]["count"]

                if county_id in county_ids_count :
                    prev_count = county_ids_count[county_id]
                    county_ids_count[county_id] = prev_count + city_student_count

                else :
                    county_ids_count[county_id] = city_student_count

    print county_ids_count
    raw_input('county_ids_count')

    county_count = 0
    for county_id in county_ids_count :
        county_count = county_count + county_ids_count[county_id]
    print county_count
    raw_input('total from county count')

    # copy the county_ids_ratios dictionary for manipulation and value replacement
    student_county_ids_ratios = county_ids_ratios

    # run through county_ids_count and replace rates in student_county_ids_ratios
    for county_id in county_ids_count :

        student_count = county_ids_count[county_id]

        county_rate = float(student_count)/float(county_count)

        if county_id in student_county_ids_ratios :
            student_county_ids_ratios[county_id] = county_rate

        if county_rate > max_rate :
            max_rate = county_rate

            print county_id
            print student_count
            print total_count
            print county_rate
            raw_input('max_rate found')

        rate_sum = rate_sum + county_rate
        counties_count = counties_count + 1

    print student_county_ids_ratios
    raw_input('... student_county_ids_ratios')

    output = 'id' + '\t' + 'rate' + '\n'
    # run through student_county_ids_ratios and print out tsv file
    for county_id in student_county_ids_ratios :

        county_rate = student_county_ids_ratios[county_id]
        add_line = "{0}\t{1}\n".format(county_id, county_rate)
        output += add_line



    print '\n\nMax rate: {0}'.format(max_rate)
    print 'Rate sum: {0}'.format(rate_sum)
    print 'Number of counties : {0}'.format(counties_count)
    print 'Average rate: {0}'.format(float(rate_sum)/float(counties_count))

    file_full_path = tsv_export_path + tsv_file_name
    save_file = open(file_full_path, 'w')
    for line in output:
        save_file.write(line)

    print '\nCreated \'{0}\' file created in \'{1}\''.format(tsv_file_name, tsv_export_path)
