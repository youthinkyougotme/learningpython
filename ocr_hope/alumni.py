import re
import types
import json
import requests
import urllib2

## location variable
# format: '<cityname>+<stateabbre>'
loc = 'holland+mi';

## setup api get requests
# format example:
# http://maps.googleapis.com/maps/api/geocode/json?address=holland+mi
apiurl = 'http://maps.googleapis.com/maps/api/geocode/json?address='+loc

# capture get request response

print '--------------'
print '1\n'

apiresp = requests.get(apiurl)
# print apiresp.json()


print '--------------'
print '2\n'

apidata = json.loads(apiresp.text)
print apidata


print '--------------'
print '3\n'

response = urllib2.urlopen(apiurl)
html = response.read()
print html
