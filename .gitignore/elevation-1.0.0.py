import json
import utm
#import geojson

with open('map1.geojson') as f:
    data = json.load(f)

lon=[]
lat=[]
z_num=[]
z_let=[]
i=0

for ty in data['features']:
    lon.append(ty['geometry']['coordinates'][0])
    lat.append(ty['geometry']['coordinates'][1])
    z_num.append(0)
    z_let.append('0')
    #print(i)    
    lon[i],lat[i],z_num[i],z_let[i]=utm.from_latlon(lat[i],lon[i])
    i+=1
#lonres=resolution_of_lon
#latres=resolution_of_lat

print(lon)
print(lat)
print(z_num)
print(z_let)
