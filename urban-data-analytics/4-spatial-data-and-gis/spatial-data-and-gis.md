
# Spatial data & GIS

A lot of urban datasets are directly linked to specific places, e.g. addresses, streets, neighbourhoods, political or administrative boundaries, etc.

Data that include place-based information are often called *spatial*, *geographic*, or *geospatial* data.


## Spatial data

A spatial dataset is a combination of...

- attribute data (the what)
- location data and spatial dimensions (the where)

Spatial data, this combination of attribute and location data, can be organized and represented in a number of different formats.

For example, a city can be represented on a map via a single point with a label (e.g. based on latitude and longitude coordinates). Or a city can be represented as a polygon, based on on it's administrative boundary

Importantly, there are always uncertainty about the level of accuracy, precision, and resolution of spatial data. Spatial data are abstractions of reality, and thus have some loss of information when used for visualization and analysis. Any analysis can only be as good as the available data.

The two most common forms of spatial data are vector data and raster data.

![Examples of spatial data](img/spatial-data.svg)


### Vector data

Vector data uses geographic coordinates, or a series of coordinates, to create points, lines, and polygons representing real-world features.

e.g. in the map below (a screenshot of OpenStreetMap) lines are used to represent roads and rail, points for retail, polygons for parks and buildings, etc.

![Screenshot of OpenStreetMap](img/osm-college.png)

Spatial data can be stored as columns in traditional table-based formats (e.g. .csv), but there are also a wide range of data formats specific to spatial data. These are some of the most common:

- GeoJSON `.geojson`
- GeoPacakge `.gpkg`
- ShapeFile `.shapfile`
- GeoDataBase `.gdb`

Here is an example of a single point location of a city stored in a `.geojson` file. `.geojson` is a standardized data schema `.json` format for spatial data.

```json
{
  	"type": "FeatureCollection",
  	"features": [
		{
			"type": "Feature",
			"geometry": {
				"type": "Point",
				"coordinates": [-80.992, 46.490]
			},
			"properties": {
				"city_name": "Sudbury"
			}
		}
	]
}
```


### Raster data

Raster data represents space as a continuous grid with equal cell sizes. Each cell contains a value pertaining to the type of feature it represents. These values can be quantitative (e.g. elevation) or categorical (e.g. type of land use). Common examples of raster data include Digital Elevation Models (DEMs), satellite imagery, and scanned images like historical maps.

e.g. the map below shows a DEM for Toronto at two different scales.

![DEM of Toronto](img/dem-toronto.png)


## Geographic Information Systems (GIS)

We use Geographic Information Systems (GIS) to analyze, manipulate, and visualize spatial data.

Why is GIS useful?

- explore spatial patterns and relationships in data
- create maps for publications
- generate new data, either "by hand" or via spatial relationships from other data (e.g. through spatial queries)
- perform spatial analysis (i.e. statistical methods applied to spatial data)

GIS is often thought of as more than just a tool or piece of software. It can refer to all aspects of managing and analyzing digital spatially referenced data.

The power of GIS software and tools is the ability to work with data stored in different layers (e.g. a layer for roads, another for buildings, and so on) in conjunction with each other. These layers can be visualized and analyzed relative to each other based on their spatial relationships.

![Simple AI generated schematic of layers](img/layer-example.jpeg)

GIS software usually links to data stored elsewhere on a computer, rather than in a project file. If the source location of the data (i.e. which folder it's in) changes, then this will have to be updated in the GIS project. If data are edited in GIS, it will update the data in its source location.

The open-source QGIS and ESRI's ArcGIS are the two most used desktop GIS software. ESRI's suite of tools are often used by larger corporate and government organizations while QGIS is more used by small consultants and freelancers, non-profits, and academia. 

Many spatial data processing and analyses steps also have equivalents in `Python`, `R`, `SQL` and other programming languages via specific libraries

We'll be working with QGIS and Python, because they free and works across multiple operating systems, and are commonly used in different industries. But pretty much everything we'll show can be done in across different software options, the buttons and steps will just be a bit different.  Learning the core analytical and visualization concepts and ideas are much more important than exactly where to click or what specific functions to run.


## Working with spatial data in QGIS

Let's use QGIS to quickly view a few spatial dataset. When you open up QGIS, it should look something like this:

![QGIS screenshot without data](img/qgis-blank.png)

The buttons at the top are for . The *Browser* panel is used for finding and loading data on your computer or from external sources, each line and symbol is for a different data source. The *Layer* panel will list all the datasets that are loaded into your project. And the big white space will populate with data once it is loaded.


### Loading data

Let's begin by adding in a basemap. Basemaps are often used to provide geographic reference for other data that we load into QGIS.

We'll add a basemap of OpenStreetMap, a free crowd-sourced map of the world, available as XYZ raster tiles. To do this, go to *Layer* - *Data Source Manager* or simply click on the *Data Source Manager* button highlighted below. When you open the *Data Source Manager* you have options for a wide variety of data types to add to your map.

![Data source manager location in QGIS](img/data-source-manager-location.png)

![Adding an XYZ tile](img/data-source-manager-xyz.png)

Here is the URL to paste into QGIS for adding an OpenStreetMap basemap: `https://tile.openstreetmap.org/{z}/{x}/{y}.png`. 

When you click 'Add' it should be added to the map. You can use the navigation buttons or just scroll on your mouse to zoom to your city.

![QGIS with OpenStreetMap](img/qgis-openstreetmap.png)

Let's now add some vector data to the map. We've pre-downloaded two datasets from the [City of Toronto's Open Data Portal](https://open.toronto.ca/)
- City Wards (polygons)
- Library Locations (points)

These can be added via the *Data Source Manager - Vector*, or simply via drag-and-drop from the folder of where they are located on your computer.

![QGIS with Toronto data](img/qgis-toronto-data.png)


### Working with layers

The data added to the project will be listed in the *Layers* panel. The order of the layers determine the order of which they stack on top of each other on the map. In the example above, the libraries are listed at the top of the other two layers, and it thus appears on top of the other two layers on the map.

To change the layer order, you can drag individual layers to be above or below any other layer in the *Layers* panel.

Most vector data has associated attribute data, e.g. the number of a ward, the name of a library, etc. To view this data, right-click on a layer and then click on *Open Attribute Table*. 


### Styling data

When you load vector data like this into QGIS, the layers have default styling (e.g. colours, sizes, line-widths, etc.). 

There are tonnes of options in QGIS to change these initial styles. To do so, right-click on a layer, go to *Properties*, and then *Symbology*.

There are lots of options in here to change the colours, size, and symbols. 

For example, in the screenshot below, the sizes of the libraries and the line-widths of the wards are increased a bit, the wards are given a transparent fill, and the library symbols are converted to squares.

![QGIS with Toronto data](img/qgis-toronto-data-2.png)

Tip! you get extra options if you click on the sub-component of the symbol. e.g. in this example I clicked on `Simple Fill` to find additional styling options like pattern-based fill styles.

![QGIS symbology example](img/qgis-symbology-example.png)

We'll explore data-driven styling, where colours or other style options are based on data values, in a future tutorial.


### Saving a project

Saving a project



## Coordinate Reference Systems (CRS) and map projections

Longitude and latitude ...




For doing analysis and an urban scale, it is important that we choose a map projection that conserves area and distances in both X and Y directions (i.e. the space is not being distorted)

For example, these are two aerial images of Toronto, the left uses a local Mercator projection which does not distort data at a local scale, while the right is a 




### Changing projections and CRS in QGIS

You can change the project CRS in QGIS 
