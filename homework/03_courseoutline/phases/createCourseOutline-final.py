import sys
import argparse

preamble = '''
  <html>
	<head>
		<link rel="stylesheet" href="./assets/bootstrap.min.css"/>
    </head>
    <style>
        .smc-html-cursor{display: none;}
        @media(min-width: 1200px){.container {width: 100%;}}
        table {font-size: 1em;}
        th {white-space: nowrap;}
    </style>
    <body class="container">
'''

postscript = '''
        <script src="./assets/jquery-2.2.0.min.js"></script>
        <script src="./assets/bootstrap.min.js"></script>
	</body>
  </html>
'''

parser = argparse.ArgumentParser(description='Create a web page version of an Excel-based course outline',epilog='Exactly one of the --include and --exclude options may be specified'
)
parser.add_argument('--include', help='A comma seperated list of column names to be included in the output')
parser.add_argument('--exclude', help='A comma seperated list of column names to be excluded from the output')

options = parser.parse_args()

if not options.include and not options.exclude :
    parser.print_help()
    sys.exit()

if options.include and options.exclude :
    print "Two arguments were include, that's bad."
    parser.print_help()
    sys.exit()

print preamble

with open("outline.txt") as outline:

    column = 0
    months = dict ()
    columnMap = dict()

    # get the column headers
    headerLine = outline.readline()
    columnHeaders = headerLine.rstrip().split("\t")
    # make the columnMap from the column headers
    while column < len(columnHeaders) :
        columnMap[columnHeaders[column]] = column
        column = column + 1

    ## print columnMap
    ## raw_input('printed columnMap')

    # check for included columns from the command
    if options.include :
        columnsToInclude = []
        columns = options.include.split(',')

        ## print columns
        ## raw_input('printed columns')

        for columnName in columns :

            columnName = columnName.rstrip()
            ## print columnName
            ## raw_input('printed columnName')

            if columnName not in columnMap :
                print 'Sorry, but the "{0}" column is not part of the outline. Columns available:'.format(columnName)
                print columnMap.keys()
                sys.exit()

            ## print columnMap[columnName]
            ## raw_input('printed columnMap[columnName]')

            columnsToInclude.append(columnMap[columnName])
            ## print columnsToInclude
            ## raw_input('printed columnsToInclude')

    else :
        columnsToInclude = range(0,len(columnMap))
        columns = options.exclude.split(',')

        ## print columns
        ## raw_input('printed columns')

        for columnName in columns :

            columnName = columnName.rstrip()
            ## print columnName
            ## raw_input('printed columnName')

            if columnName in columnMap :
                ## print columnMap[columnName]
                ## raw_input('printed columnMap[columnName]')

                columnsToInclude.remove(columnMap[columnName])
                ## print columnsToInclude
                ## raw_input('printed columnsToInclude')

            else :
                print 'FYI, The "{0}" column is not part of the outline.'.format(columnName)

    ## print "columnsToInclude are", columnsToInclude
    ## sys.exit()

    # for each line in the file
    for line in outline:

        # start the table row
        tableRow = "<tr>"
        # get the columns
        columns = line.split("\t")
        # make table cells for each column

        # set column number to iterate with
        columnNumber = 0
        ## print columnNumber
        ## raw_input('printed columnNumber')

        for column in columns:
            if columnNumber in columnsToInclude :
                tableRow = tableRow + "<td>{0}</td>".format(column)
                ## raw_input('printed row')
            columnNumber += 1
            ## print columnNumber
            ## raw_input('printed columnNumber')

        # close the table row
        tableRow = tableRow + "</tr>"

        # get the value of the date column
        dateColumnValue = columns[columnMap['Date']]
        # seperate date into month, day, year
        dateParts = dateColumnValue.split("/")
        # get the month as an int
        month = int(dateParts[0])

        if month in months:
            # add current table row to the corresponding month list
            months[month].append(tableRow)
        else:
            # add current table row to a new month list
            months[month] = [tableRow]

monthNames = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}

'''
At this point, the dictionary named months has one key for each month found in the file
with the value being a list of strings representing rows in the table.

Recall that the key values are integers representing the month number; the monthNames
dictionary above can be used to get the name of the month based on the numeric value
'''

'''
Add the code to print out the tabs after this comment.  The tabs should look like this
-------------------------------------------------------------------------
<ul class="nav nav-tabs">
  <li class="active"><a href="#January data-toggle="tab">January</a></li>
  <li><a href="#February data-toggle="tab">February</a></li>
  ...
</ul>
-------------------------------------------------------------------------
Note that only the first <li> contains the class="active" attribute; the
remainder do not.
'''

#  Print out the <ul> element that starts the list of tabs; note there aren't
#  any variables here; the contents are literally what is shown above
print '<ul class="nav nav-tabs">'

#  Set a variable named classAttribute to the string value class="active"
classAttribute = ' class="active"'

#  Start a for loop that iterates over the sorted keys from the months dictionary.
for month_num in sorted(months.keys()) :

    #  In the loop, print an <li> element, including the value of the classAttribute
    #  variable between the 'i' and the '>' for <li>, and placing the name of the month
    #  after the # and between the <a> and </a>

    print '<li{0}>'.format(classAttribute)
    print '<a href="#{0}" data-toggle="tab">{0}</a>'.format(monthNames[month_num])
    print '</li>'

    #  Also in the loop, set the variable classAttribute to be the empty string
    classAttribute = ''

#  After the loop, literally print out the </ul> ending tag
print '</ul>'



#  Now we print out the actual tab contents
#  The <div> below is wrapped around all of the tabs
print "<div class='tab-content'>"

activeAttribute = ' active'

'''
Write a loop here that iterates over the sorted keys in the months dictionary
For each key, it should print:
---------------------------------------------------------------------------------
  <div role="tabpanel" class="tab-pane active" id="January">  (replace id with the name of the month)
    <table class="table table-striped"
    <tr>
      <th>One for each value in the list named columnHeaders</th>
    </tr>

    Each value in the list of strings associated with the key

    </table>
  </div>
---------------------------------------------------------------------------------
Only the first <div> should have the 'active' value included in the " " for the class; the others should
only have the value 'tab-pane'
'''
for month_num in sorted(months.keys()) :
    print '<div role="tabpanel" class="tab-pane{0}" id="{1}">'.format(activeAttribute, monthNames[month_num])
    print '<table class="table table-striped">'

    print '<tr>'
    # set columnNumber value to increment with
    columnNumber = 0
    ## print columnNumber
    ## raw_input('printed columnNumber')

    for header in columnHeaders :
        if columnNumber in columnsToInclude :
            print '<th>{0}</th>'.format(header)
            ## raw_input('printed header')
        columnNumber += 1
        ## print columnNumber
        ## raw_input('printed columnNumber')
    print '</tr>'

    items = months[month_num]

    for item in items :
        print item

    print '</table>'
    print '</div>'

    activeAttribute = ''

#  This ends the div that wraps all of the tab pane content (don't change it!)
print "</div>"

print postscript
