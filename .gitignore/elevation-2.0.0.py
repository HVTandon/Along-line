import json
import utm
import geog
import numpy as np
from math import *

def dx(distance, m):
    return sqrt(distance/(m**2+1))

def dy(distance, m):
    return m*dx(distance, m)

with open('map2.geojson') as f:
    data = json.load(f)
lon_lat=[]
lon_lat_utm=[]
line_points_utm=[]
line_points_coordi=[]
rang=0
i=0
distance=1
z_num=0
z_letter='A'
diff=0.0
#new_point_coordi=[0,0]

for ty in data['features'][0]['geometry']['coordinates']:
    lon_lat.append(ty)
    lon_lat_utm.append(utm.from_latlon(lon_lat[i][1],lon_lat[i][0]))
    i+=1
z_num=int(lon_lat_utm[0][2])
z_letter=lon_lat_utm[0][3]
n=i
#print(n)
l=0
line_points_utm.append([lon_lat_utm[0][0],lon_lat_utm[0][1]])
#line_points_coordi.append(lon_lat[0])
#new_point_coordi=lon_lat[0]
#print(lon_lat_utm,"\n")

for i in range(n-1):
    #print("---------------------------------   ",i,"    --------------------------------")
    #m=(lon_lat[i+1][1]-lon_lat[i][1])/(lon_lat[i+1][0]-lon_lat[i][0])
    #if lon_lat[i+1][0]-lon_lat[i][0]>0:
    #    line_points_utm.append(line_points_utm[i][0]+dx(distance,m), line_points_utm[i][1]+dy(distance,m))
    #else:
    #    line_points_utm.append(line_points_utm[i][0]-dx(distance,m), line_points_utm[i][1]-dy(distance,m)) # going the other way
    dist=geog.distance(lon_lat[i],lon_lat[i+1])
    #print(dist)
    new_point_coordi=lon_lat[i]
    #print(new_point_coordi)
    #print(lon_lat[0],"--------------",lon_lat[1])
    flag=True

    while flag==True:
        if geog.distance(lon_lat[i+1],new_point_coordi) > distance/2:
            #print(new_point_coordi,lon_lat[i+1])
            #print(geog.distance(new_point_coordi,lon_lat[i+1]),"---------   ",l)
            l+=1
            #print(l)
            m=(lon_lat_utm[i+1][1]-line_points_utm[int(l-1)][1])/(lon_lat_utm[i+1][0]-line_points_utm[int(l-1)][0])
            if lon_lat_utm[i+1][0]-lon_lat_utm[i][0]>0:
                new_point=[line_points_utm[int(l-1)][0]+dx(distance,m), line_points_utm[int(l-1)][1]+dy(distance,m)]
            else:
                new_point=[line_points_utm[int(l-1)][0]-dx(distance,m), line_points_utm[int(l-1)][1]-dy(distance,m)] # going the other way
                #print(diff)
            line_points_utm.append(new_point)
            #print(line_points_utm[int(l)][0],line_points_utm[int(l)][1], z_num, z_letter)
            new_point_coordi=utm.to_latlon(line_points_utm[int(l)][0], line_points_utm[int(l)][1], z_num, z_letter)
            new_point_coordi=[new_point_coordi[1],new_point_coordi[0]]
            #print(new_point)
            line_points_coordi.append(new_point_coordi)
            #diff=geog.distance(line_points_coordi[0],new_point_coordi)-(l-1)*distance
            #print(l,"--------------*",diff,"-----------------*",geog.distance(line_points_coordi[0],new_point_coordi))
        else :
            flag=False 
    rang+=dist
l=0
#print(geog.distance(line_points_coordi[0],new_point_coordi))
#print(len(line_points_utm))
for l in range(0,len(line_points_coordi)):
    print(line_points_coordi[l][0])
