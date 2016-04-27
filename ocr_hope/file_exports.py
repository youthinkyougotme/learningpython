import json

from decimal import *
getcontext().prec = 8

def export_tsv_ids_rates(county_ids_ratios, student_locations_us, tsv_export_path, tsv_file_name) :

    # count total students for rate calculation first
    total_count = 0
    for state in student_locations_us :
        for city in student_locations_us[state] :
            county_student_count = student_locations_us[state][city]["count"]
            total_count = total_count + county_student_count

    print total_count
    raw_input('total_count')

    max_rate = float(0)
    rate_sum = float(0)
    county_count = 0
    # copy the county_ids_ratios dictionary for manipulation and value replacement
    student_county_ids_ratios = county_ids_ratios
    # run through student locations and replace rates in student_county_ids_ratios
    for state in student_locations_us :
        for city in student_locations_us[state] :

            if 'county_id' in student_locations_us[state][city] :

                county_id = student_locations_us[state][city]["county_id"]
                county_student_count = student_locations_us[state][city]["count"]
                county_rate = float(county_student_count)/float(total_count)

                if county_id in student_county_ids_ratios :
                    student_county_ids_ratios[county_id] = county_rate

                if county_rate > max_rate :
                    max_rate = county_rate

                rate_sum = rate_sum + county_rate
                county_count = county_count + 1


    print student_county_ids_ratios
    raw_input('student_county_ids_ratios')

    output = 'id' + '\t' + 'rate' + '\n'
    # run through student_county_ids_ratios and print out tsv file
    for county_id in student_county_ids_ratios :

        county_rate = student_county_ids_ratios[county_id]
        add_line = "{0}\t{1}\n".format(county_id, county_rate)
        output += add_line



    print '\n\nMax rate: {0}'.format(max_rate)
    print 'Rate sum: {0}'.format(rate_sum)
    print 'County count: {0}'.format(county_count)
    print 'Average rate: {0}'.format(float(rate_sum)/float(county_rate))

    file_full_path = tsv_export_path + tsv_file_name
    save_file = open(file_full_path, 'w')
    for line in output:
        save_file.write(line)

    print '\nCreated \'{0}\' file created in \'{1}\''.format(tsv_file_name, tsv_export_path)
