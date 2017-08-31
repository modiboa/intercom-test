import json
from math import sin, asin, cos, sqrt, atan2, radians

DUBLIN_LAT = 53.3393
DUBLIN_LON = -6.2576841

def haversine(lon1, lat1):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    lat2 = DUBLIN_LAT
    lon2 = DUBLIN_LON

    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    km = 6367 * c
    return km

with open('customer.json') as f:
    for line in f:
        customer = json.loads(line)
        print customer
        print haversine(float(customer['longitude']), float(customer['latitude']))