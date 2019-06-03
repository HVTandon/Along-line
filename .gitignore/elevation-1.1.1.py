import json
import utm
import geog
import numpy as np
from math import *

def pointy(lon__lat, radian, distance):
    a=utm.from_latlon(lon__lat[1],lon__lat[0])
    #print(a)
    #print(utm.to_latlon[lon__lat[0]+ cos(radian)*distance, lon__lat[1]+ sin(radian)*distance])
    easting=a[0]+ cos(radian)*distance
    northing=a[1]+ sin(radian)*distance
    b=utm.to_latlon(easting,northing,a[2],a[3])
    return [b[1],b[0]]
#import geojson

d=2 # meters

with open('map2.geojson') as f:
    data = json.load(f)
lon_lat=[]
line_points=[]
i=0
rang=0

#collecting coordinates of all the points on the line string.
# /adding these coordinates to the longitude and latitude list

for ty in data['features'][0]['geometry']['coordinates']:
    lon_lat.append(ty)
    i+=1
print(lon_lat)

n=i
i=0
#print(n)

for i in range(n-1):
    line_points.append(lon_lat[i])
    #print(i)
    #slope of line
    #lon_lat is a list of (longitude,latitude)
    a=utm.from_latlon(lon_lat[i+1][1],lon_lat[i+1][0])
    b=utm.from_latlon(lon_lat[i][1],lon_lat[i][0])
    m=(a[1]-b[1])/a[0]-b[0]
    print(m)

    #tan inverse of slop to get angle and checking the quadrant of angle
    if a[0]-b[0]>0:
        angle=atan(m)
        #print(angle)
    else:
        angle=np.pi+atan(m)
        if angle>2*np.pi:
            angle=angle-2*np.pi    
    print(angle)
    dist=geog.distance(lon_lat[i],lon_lat[i+1])
    #print(dist)
    #print(rang)

    for l in np.arange(rang+1,rang+dist+1):
        #m= (latitude2 - latitude1)/(longitude2 - longitude1)
        a=utm.from_latlon(lon_lat[i+1][1],lon_lat[i+1][0])
        b=utm.from_latlon(line_points[int(l-1)][1],line_points[int(l-1)][0])
        m=(a[1]-b[1])/(a[0]-b[0])
        if a[0]-b[0]>0:
            angle=atan(m)
        else:
            angle=np.pi+atan(m)
            if angle>=(2*np.pi):
                angle=angle-(2*np.pi)
        print(l,"-----",m,"----",angle)  
        line_points.append(pointy(line_points[int(l-1)],angle,d))
    #print(len(line_points))
        #print(l,"      ----",line_points[int(l-1)])
        #print(line_points[int(l-1)])
    #print(l)
    rang=rang+int(dist)
    #print(rang)
    #print(m,t)
#for l in range(len(line_points)):
#    print(line_points[l][0])
    #print(l)    