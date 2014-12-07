from pygeocoder import Geocoder
import os 

with open('coordtest.txt') as f:
    content = f.readlines()

for lines in content:
    col = lines.split(',')
    lat = float(col[1])
    llong = float(col[2])
    try:
        results = Geocoder.reverse_geocode(lat, llong) 
    except:
        print 'not on land'

    col.append(results.formatted_address.replace('\r', '').replace('\n', ''))
    for c in col:
        c = c.rstrip(os.linesep)
        print '%s, ' % c,

# results = Geocoder.reverse_geocode(-22.0550,169.1780)
# print(results[0])
