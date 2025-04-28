import random
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, Polygon

# load and join the DA polygon and tabular data
da = gpd.read_file("data/toronto-da-2021.geojson")
dft = pd.read_csv("data/toronto-tenure-da-2021.csv")
dft.fillna(0, inplace=True)

dft["DAUID"] = dft["DAUID"].astype('str')
da = da.merge(dft, how='left', on='DAUID')

da["Total"] = da["Owner"] + da["Renter"]
da["Owner_no_mortgage"] = da["Owner"] - da["Owner_with_mortgage"]
da["Renter_not_in_subsidized_housing"] = da["Renter"] - da["Renter_in_subsidized_housing"]

# households per dot
d = 10
da["Owner_with_mortgage_dots"] = da["Owner_with_mortgage"] / d
da["Owner_no_mortgage_dots"] = da["Owner_no_mortgage"] / d
da["Renter_in_subsidized_housing_dots"] = da["Renter_in_subsidized_housing"] / d
da["Renter_not_in_subsidized_housing_dots"] = da["Renter_not_in_subsidized_housing"] / d

# grab residential land use data
lu = gpd.read_file("data/toronto-land-use-2022-sp.shp")
res_classes = ["MixedUse", "Neighbourhoods", "ApartmentNeighbourhoods"]
res = lu[lu['Class_name'].isin(res_classes)]

# intersect with the DA layer
gdf = gpd.overlay(da, res, how='intersection').dissolve(by = "DAUID")

# function for placing a random point in a polygon
def gen_dot(polygon):
    while True:
        pt = Point(random.uniform(polygon.bounds[0], polygon.bounds[2]), random.uniform(polygon.bounds[1], polygon.bounds[3]))
        if (polygon.contains(pt)==True):
            points = [pt.x,pt.y]
            break
    return points

variables = [
    "Owner_with_mortgage", 
    "Owner_no_mortgage", 
    "Renter_not_in_subsidized_housing", 
    "Renter_in_subsidized_housing"
]

# loop over each row and variable, generating X dots
output = []
for index, row in gdf.iterrows():
    for var in variables:
        n = round(row[var + "_dots"])
        i = 0
        while i < n:
            dot = gen_dot(row["geometry"])
            output.append([var,dot[0],dot[1]])
            i += 1
            
# converting the output to a geodataframe
dots = pd.DataFrame(output, columns = ["type","x","y"])
geometry = [Point(xy) for xy in zip(dots['x'], dots['y'])]
dots = gpd.GeoDataFrame(dots, geometry=geometry)
dots = dots[["type","geometry"]].set_crs('epsg:4326')
dots.to_file("data/dots.geojson", driver="GeoJSON")