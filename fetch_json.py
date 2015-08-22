
from urllib2 import urlopen
import json
import pprint

with open("secrets.json") as f:
    secrets = json.loads(f.read())

url = "http://data.tmsapi.com/v1.1/sports/all/events/airings?lineupId=USA-TX42500-X&startDateTime=2015-08-22T02%3A00Z&endDateTime=2015-08-23T03%3A00z&liveOnly=true&imageAspectTV=16x9&api_key={0}".format(secrets["API_KEY"])
url = urlopen(url)
response = url.read()
charset = url.headers.getparam('charset')
data = json.loads(response.decode(charset))

for show in data:
    try:
        print show['program']['eventTitle']
    except KeyError, e:
        print 'No eventTitle here!', pprint.pprint(show)
print '{0} programs'.format(len(data))
