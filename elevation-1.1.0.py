import json
import utm
import geog
import numpy as np
from math import *
#import geojson

d=2 # meters

with open('map2.geojson') as f:
    data = json.load(f)
lon_lat=[]
line_points=[]
i=0

#collecting coordinates of all the points on the line string.
# /adding these coordinates to the longitude and latitude list

for ty in data['features'][0]['geometry']['coordinates']:
    lon_lat.append(ty)
    i+=1
#print(lon_lat)

n=i
#print(n)

for i in range(n-1):
    #print(i)
    #slope of line
    #lon_lat is a list of (longitude,latitude)
    m=(lon_lat[1+i][1]-lon_lat[i][1])/(lon_lat[i+1][0]-lon_lat[i][0])
    #print(m)

    #tan inverse of slop to get angle and checking the quadrant of angle
    if lon_lat[i+1][0]-lon_lat[i][0]>0:
        angle=degrees(atan(m))
        #print(angle)
    else:
        angle=180+degrees(atan(m))
        if angle>360:
            angle=angle-360    
    #print(angle)
    dist=geog.distance(lon_lat[i],lon_lat[i+1])
    #print(dist)
    rang=np.arange(0,dist,1)
    #print(rang)
    t=i*100
    #print("----------------------------",t,"------------------------------------")
    line_points.append(lon_lat[i])
    #print("------------------------------",len(line_points),"-------------------------------------------")

    for l in range(t+1,t+100):
        line_points.append(geog.propagate(line_points[int(l-1)],angle,d))
        #print(l,"      ----",line_points[int(l-1)])
        #print(line_points[int(l-1)])
    
    #print(m,t)
    for l in range(t-1,t+99):
        print(line_points[l][1])
        #print(t)    