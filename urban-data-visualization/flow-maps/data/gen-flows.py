# this script uses a simple gravity model to simulate flows between two sets of points
# currently application is census dissemination areas to hospitals in calgary

# could probably do this in geopandas, but I just felt like doing it a 'vanilla' sort of way

import json
import csv
import math

def distance_km(x1, y1, x2, y2):
    # Convert x and y to radians
    lon1, lat1, lon2, lat2 = map(math.radians, [x1, y1, x2, y2])
    # Compute the distance using Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    km = 6367 * c
    return km

def impedence(distance, beta):
    return math.exp(beta * distance)


beta = -0.25

with open('hospital-locations.geojson') as f:
    hp = json.load(f)

with open('da-2021-centroids.geojson') as f:
    da = json.load(f)
    
    
output = []

for da in da["features"]:
    
    dauid = da["properties"]["name"]
    population = int(da["properties"]["population"]) / 10
    
    da_x = da["geometry"]["coordinates"][0]
    da_y = da["geometry"]["coordinates"][1]    
    
    da_hospital = []
    
    trip_sums = 0
        
    for hospital in hp["features"]:
        hospital_id = hospital["properties"]["id"]
        hospital_x = hospital["geometry"]["coordinates"][0]
        hospital_y = hospital["geometry"]["coordinates"][1]  
        d = distance_km(da_x, da_y, hospital_x, hospital_y)
        da_hospital.append([hospital_id, d, impedence(d, beta)])
        trip_sums = trip_sums + impedence(d, beta)
    
    
    for row in da_hospital:
        
        output.append([dauid, row[0], round(population * row[2] / trip_sums, 0)])    
    
with open("od-flows.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["dauid","hospital_id","trips"])
    for row in output:
        writer.writerow(row)
        
