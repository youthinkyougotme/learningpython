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

parser = argparse.ArgumentParser(description='Create a web page version of an Excel-based course outline', epilog='Exactly one of the --include and --exclude options may be specified')
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

    headerLine = outline.readline()
    columnHeaders = headerLine.rstrip().split("\t")
    while column < len(columnHeaders) :
        columnMap[columnHeaders[column]] = column
        column = column + 1

    if options.include :

        columnsToInclude = []
        columns = options.include.split(',')

        for columnName in columns :
            columnName = columnName.rstrip()
            if columnName not in columnMap :
                print 'Sorry, but the "{0}" column is not part of the outline. Columns available:'.format(columnName)
                print columnMap.keys()
                sys.exit()
            columnsToInclude.append(columnMap[columnName])

    else :

        columnsToInclude = range(0,len(columnMap))
        columns = options.exclude.split(',')

        for columnName in columns :
            columnName = columnName.rstrip()
            if columnName in columnMap :
                columnsToInclude.remove(columnMap[columnName])

    for line in outline:

        tableRow = "<tr>"
        columns = line.split("\t")
        columnNumber = 0

        for column in columns:
            if columnNumber in columnsToInclude :
                tableRow = tableRow + "<td>{0}</td>".format(column)
            columnNumber += 1
        tableRow = tableRow + "</tr>"

        dateColumnValue = columns[columnMap['Date']]
        dateParts = dateColumnValue.split("/")
        month = int(dateParts[0])

        if month in months:
            months[month].append(tableRow)
        else:
            months[month] = [tableRow]



print '<ul class="nav nav-tabs">'
classAttribute = ' class="active"'
for month_num in sorted(months.keys()) :
    print '<li{0}>'.format(classAttribute)
    print '<a href="#{0}" data-toggle="tab">{0}</a>'.format(monthNames[month_num])
    print '</li>'
    classAttribute = ''
print '</ul>'

print "<div class='tab-content'>"
activeAttribute = ' active'
for month_num in sorted(months.keys()) :
    print '<div role="tabpanel" class="tab-pane{0}" id="{1}">'.format(activeAttribute, monthNames[month_num])
    print '<table class="table table-striped">'

    print '<tr>'
    columnNumber = 0
    for header in columnHeaders :
        if columnNumber in columnsToInclude :
            print '<th>{0}</th>'.format(header)
        columnNumber += 1
    print '</tr>'

    items = months[month_num]
    for item in items :
        print item

    print '</table>'
    print '</div>'

    activeAttribute = ''
print "</div>"

print postscript
