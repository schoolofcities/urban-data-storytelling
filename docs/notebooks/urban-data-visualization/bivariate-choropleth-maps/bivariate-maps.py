import math
import pandas as pd
import geopandas as gpd
import mapclassify
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# loading data and merging

gdf = gpd.read_file("data/dissemination-area-winnipeg-2016.geojson")
dfm = pd.read_csv("data/can-marg-manitoba-2016.csv")
dfb = pd.read_csv("data/can-bics-winnipeg.csv")

gdf = gdf.merge(dfb, how='left', on='dauid').merge(dfm, how='left', on='dauid')

csd = gpd.read_file("data/csd-winnipeg-2016.geojson")
osm_streets = gpd.read_file("data/streets-osm-winnipeg.geojson")
osm_rivers = gpd.read_file("data/river-osm-winnipeg.geojson")

# classifying data

gdf['x_group'] = gdf[['CBICS_cont']].apply(mapclassify.Quantiles.make(rolling=True, k = 3))
gdf['y_group'] = gdf[['material_resources_DA16']].apply(mapclassify.Quantiles.make(rolling=True, k = 3))
gdf['xy_group'] = gdf['x_group'].astype(str) + "-" + gdf['y_group'].astype(str)

# linking classes to colours

color_mapping = {
    "0-2": "#f73593", 
    "0-1": "#f78fb6",
    "0-0": "#f7fcf5", 
    "1-2": "#a53593",
    "1-1": "#a58fb6", 
    "1-0": "#a5e8cd", 
    "2-2": "#403593",
    "2-1": "#408fa7",
    "2-0": "#40dba7" 
}

# plotting

fig, ax = plt.subplots(figsize=(7,7))

# Winnipeg border
csd.plot(
    edgecolor = "#c2c2c2",
    linewidth = 4.2,
    ax = ax
);

# bivariate data
gdf.plot(
    column = "xy_group",
    categorical = True,
    edgecolor = "white",
    linewidth = 0.2,
    ax = ax,
    color=gdf["xy_group"].map(color_mapping),
).set_axis_off();

# Winnipeg streets
osm_rivers.plot(
    color = "#c2c2c2",
    linewidth = 0,
    ax = ax
);

# Winnipeg streets
osm_streets.plot(
    color = "#5e5e5e",
    linewidth = 0.25,
    ax = ax
);

# custom legend
legend_elements = []
for key, value in color_mapping.items():
    legend_elements.append(Patch(facecolor=value, edgecolor='gray', label=""))
ax.legend(
    handles=legend_elements, 
    loc='lower right', 
    fontsize= 12, 
    ncol=3, 
    handletextpad=0.1, 
    labelspacing = 0.1, 
    columnspacing = 0.1
)
ax.text(0.55, 0.1, 'Material\nDeprivation', transform=ax.transAxes, fontsize=10,
        verticalalignment='top')
ax.text(0.75, 0.01, 'Quality of Cycling\nInfrastructure', transform=ax.transAxes, fontsize=10,
        verticalalignment='top')

# save
fig.savefig('images/winnipeg-bivariate-map-python-export-test.svg')
