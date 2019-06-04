import json
import numpy as np
from math import *
from geographiclib.geodesic import Geodesic
geod = Geodesic.WGS84  # define the WGS84 ellipsoid

geod.a, 1/geod.f
#geod.a gives equitorial radius and geod.f gives flattening of ellipsoid (f=0 means sphere)

with open('Patan Bhildi.geojson') as f:
    data = json.load(f)
lon_lat=[]
geos=[]
line_points_coordi=[]
rang=0
i=0
t=0

for ty in data['features'][0]['geometry']['coordinates']:
    lon_lat.append(ty)

n1=len(lon_lat)
print(n1)

for t in range(n1-1):
    l = geod.InverseLine(lon_lat[t][1],lon_lat[t][0],lon_lat[t+1][1], lon_lat[t+1][0])
    # l is a geodesic line.
    #l.s13 gives the distance between the 2 input coordinates i.e. coordinates in lon_lat
    #step_size is in metres
    step_size = 5; n = int(ceil(l.s13 / step_size))
    for i in range(n + 1):
        s = min(step_size * i, l.s13)
        #l.Position gives the coordinates of the point on the line at a distance 's'.
        g = l.Position(s, Geodesic.STANDARD | Geodesic.LONG_UNROLL)
        line_points_coordi.append([g['lat2'],g['lon2']])

poly = {
    'type': 'Polygon',
    'coordinates': [[longs,lats] for longs,lats in line_points_coordi]
}
geos.append(poly)

geometries = {
    'type': 'FeatureCollection',
    'features': geos,
}

geo_str = json.dumps(geometries) 
print(geo_str)