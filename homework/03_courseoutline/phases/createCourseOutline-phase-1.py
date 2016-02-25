preamble = '''
  <html>
	<head>      
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css"/>
    </head>

    <body class="container">
		<table class="table table-striped">
'''

postscript = '''
		</table>
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
		
	print "<tr>"
	
	for header in columnHeaders:
		print "<th>{0}</th>".format(header)
	
	print "</tr>"

print postscript	
