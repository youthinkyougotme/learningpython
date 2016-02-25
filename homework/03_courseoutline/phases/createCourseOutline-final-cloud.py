preamble = '''
  <html>
	<head>
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous"/>
    </head>
    <style>.smc-html-cursor{display: none;}</style>
    <body class="container">
'''

postscript = '''
        <script src="https://code.jquery.com/jquery-2.2.0.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"
            integrity="sha384-0mSbJDEHialfmuBBQP6A4Qrprq5OVfW37PRR3j5ELqxss1yVqOtnepnHVP9aJ7xS"
            crossorigin="anonymous">
        </script>
	</body>
  </html>
'''

print preamble

with open("outline.txt") as outline:
    headerLine = outline.readline()

    column = 0
    columnMap = dict()

    columnHeaders = headerLine.split("\t")

    while column < len(columnHeaders):
        columnMap[columnHeaders[column]] = column
        column = column + 1

    months = dict ()

    for line in outline:
        tableRow = "<tr>"
        columns = line.split("\t")

        for column in columns:
            tableRow = tableRow + "<td>{0}</td>".format(column)

        tableRow = tableRow + "</tr>"

        dateColumnValue = columns[columnMap['Date']]

        dateParts = dateColumnValue.split("/")
        month = int(dateParts[0])

        if month in months:
            months[month].append(tableRow)
        else:
            months[month] = [tableRow]

monthNames = {
    1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
    9: 'September', 10: 'October', 11: 'November', 12: 'December'
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


    items = months[month_num]

    for item in items :
        print item

    print '</table>'
    print '</div>'

    activeAttribute = ''

#  This ends the div that wraps all of the tab pane content (don't change it!)
print "</div>"

print postscript
