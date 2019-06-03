import json
import utm
import numpy as np
#import geojson

with open('map2.geojson') as f:
    data = json.load(f)

lon=[]
lat=[]
ele=[]
z_num=[]
z_let=[]
i=0

#collecting coordinates of all the points on the line string.
# /adding these coordinates to the longitude and latitude list

for ty in data['features'][0]['geometry']['coordinates']:
    lon.append(ty[0])
    lat.append(ty[1])
    ele.append(ty[2])
    z_num.append(0)
    z_let.append('0')    
    lon[i],lat[i],z_num[i],z_let[i]=utm.from_latlon(lat[i],lon[i])
    i+=1
print(lon)
n=i-1
i=0

#coordinates on lines
for i in range(n):
    lat_on_line=[lat[i]]
    lon_on_line=[lon[i]]
    m=(lat[i+1]-lat[i])/(lon[i+1]-lon[i])
    #a,b=lat[i],lat[i+1]
    #c,d=lon[i],lon[i+1]
    rang=np.arange(0,lat[i+1]+1.0-lat[i],1)
    l=1

    for l in rang:
        lon_on_line.append(lon[i]+l)
        lat_on_line.append(lat[i]+(m*l))

print(lon_on_line)

#lonres=resolution_of_lon
#latres=resolution_of_lat

print(lon)
print(lat)
print(z_num)
print(z_let)
