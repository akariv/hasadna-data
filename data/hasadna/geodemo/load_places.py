# -*- coding: utf-8 -*-
import json
import urllib2
import sys

LAT = [ 32.039658 + i*0.0058042 for i in range(11) ]
LON = [ 34.746323 + i*0.0037422 for i in range(11) ]

results = {}
for lat in LAT:
  for lon in LON:
    res = urllib2.urlopen("https://maps.googleapis.com/maps/api/place/search/json?location=%f,%f&radius=500&sensor=false&key=AIzaSyAwwAQHYJ29SkL3Ipi9JO-15mR5OXNIUl0" % (lat,lon) ).read()
    res = json.loads(res)
    try:
      for r in res["results"]:
	if "establishment" not in r["types"]:
	  continue
	results[r["id"]] = { "slug": r["id"],
	                     "lat" : r["geometry"]["location"]["lat"],
		             "lng" : r["geometry"]["location"]["lng"],
		             "name": r["name"] }
    except:
      pass

print json.dumps(results)
print json.dumps(results.values())
file('out.json','w').write(json.dumps(results.values(),indent=2))
