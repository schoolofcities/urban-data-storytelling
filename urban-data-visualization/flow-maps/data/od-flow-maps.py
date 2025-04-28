import pandas as pd
import geopandas as gpd
from shapely.geometry import LineString
import matplotlib.pyplot as plt

od = pd.read_csv("data/od-flows.csv")

da = gpd.read_file("data/da-2021-centroids.geojson")
da_poly = gpd.read_file("data/da-2021-polygons.geojson")
hp = gpd.read_file("data/hospital-locations.geojson")

da['dauid'] = da['name'].astype('int64')

odm = od.merge(
    da, 
    how='left', 
    on = "dauid"
).merge(
    hp, 
    how='left', 
    left_on='hospital_id',
    right_on='id'
)

odm = gpd.GeoDataFrame(
    {
        'dauid': odm['dauid'],
        'hospital_id': odm['hospital_id'],
        'trips': odm['trips'],
        'geometry': odm.apply(
            lambda x: LineString([x['geometry_x'], x['geometry_y']]), axis=1
        )
    }
).set_crs(epsg="4326")

odm.to_file("data/od-flow-lines.geojson", driver="GeoJSON")



# 5 colours on one map

colour_mapping = {
    0: "#DC4633",  
    1: "#8DBF2E",
    2: "#F1C500",
    3: "#00A189",
    4: "#6FC7EA",
}
odm["colour"] = odm["hospital_id"].map(colour_mapping)

odm["opacity"] = odm["trips"] / 250
odm['opacity'] = odm['opacity'].clip(upper=1)

fig, ax = plt.subplots(figsize=(7,7), facecolor='black')

da_poly.plot(
    ax = ax,
    edgecolor = '#484848',
    linewidth = 2,
    color = "Black"
)
da_poly.plot(
    ax = ax,
    edgecolor = '#2B2B2B',
    linewidth = 0.5,
    color = "Black"
)

for hospital in [0,1,2,3,4]:
    odp = odm[odm["hospital_id"] == hospital]
    odp.plot(
        ax=ax, 
        linewidth=1, 
        alpha=odp["opacity"], 
        color=odp['colour'], 
        zorder = 1
    )
    
for hospital in [0,1,2,3,4]:
    odp = odm[odm["hospital_id"] == hospital]
    odp.plot(
        ax=ax, 
        linewidth=2, 
        alpha=odp["opacity"] / 3, 
        color=odp['colour'], 
        zorder = 2
    )
    
hp.plot(
    ax = ax,
    color = 'White',
    markersize = 40,
    zorder = 3
)

ax.set_title(
    'Travel to Hospitals in Calgary', 
    fontsize=10,
    loc = "left"
).set_color('LightGray')

ax.set_axis_off()

fig.savefig('images/calgary-hospital-map-all-python-export.png')



# 5 small multiple plots

fig, ax = plt.subplots(ncols=5, nrows=1, figsize=(22.5,7.5), facecolor='black')

for hospital in [0,1,2,3,4]:
    
    # data layers
    
    odp = odm[odm["hospital_id"] == hospital]
    da_poly.plot(
        ax = ax[hospital],
        edgecolor = '#484848',
        linewidth = 2,
        color = "Black"
    )
    da_poly.plot(
        ax = ax[hospital],
        edgecolor = '#2B2B2B',
        linewidth = 0.5,
        color = "Black"
    )
    odp.plot(
        ax=ax[hospital], 
        linewidth=1, 
        alpha=odp["opacity"], 
        color=odp['colour'], 
        zorder = 1
    )
    hp[hp["id"] == hospital].plot(
        ax = ax[hospital],
        color = 'White',
        markersize = 10,
        zorder = 3
    ).set_axis_off()
    
    # titles
    
    ax[hospital].set_title(
        hp.loc[hospital, 'facility_name'], 
        fontsize=8,
        loc='center'
    ).set_color('White')
    
fig.suptitle(
    'Travel to Hospitals in Calgary', 
    fontsize=13
).set_color('White')

fig.tight_layout(rect=[0, 0.03, 1, 0.95])
fig.subplots_adjust(top=0.9, bottom=0.1)

fig.savefig('images/calgary-hospital-map-multipes-python-export.png')



