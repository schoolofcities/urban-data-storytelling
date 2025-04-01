# Maps & Visualizing Spatial Data

<br>

![](img/maps-mini-examples.png)

## Overview

Cartography

For research, for communication

Decisions, heirarchy

Reference (what is where, navigation) or thematic (show specific data, visualization for a story, etc.)

Static and interactive.

1. **selection** of data to include on the map
2. **generalization** of data to reduce complexity and clutter
3. how we want to **style** and **symbolize** our data
4. how to order and **layer data**
5. what other **map layout elements** to include (e.g. title, legend, north arrow), as well as how to design these to make a map easy to understand


This page will cover the basics of making maps and spatial data visualizations. The last part of this notebook shows an example in QGIS. If you are interested in creating specific types of maps, check out the following notebooks:
- Choropleth maps
- Proportional symbol maps
- Mapping point density


## Categories of maps


### Reference or thematic

Examples of reference maps 
- old and new

Maps - Google Maps, for example, is probably the most viewed map in human history now.

Reference maps are often used as *base maps* for thematic maps and visualizing spatial data.




Examples of thematic maps - geo-visualization - spatial data visualization

These types of maps can be super useful for exploratory data analysis during the research process. 



### Static or dynamic

Static (varying sizes)

Dynamic/interactive (dashboard or story)

Generally - start with static

Dynamic and interactive maps typically take more work to create as they include all the design thinking in a static map, plus additional thinking about motion and how a reader would interact with it.


## What's on the map?

Maps always abstractions of reality. It is impossible to show everything in the world on a piece of paper or a screen - nor would we want to, we usually want to focus our reader's attention on specific data, trend, or story. 

Making maps and spatial data visualizations therefore often involve various decisions on *selection* and *generalization* of spatial data to reduce visual clutter to focus on specific data points.


### Cartographic selection

Cartographic selection is about picking the most important things to draw on a map so it's not too crowded. Imagine drawing a treasure map — you’d likely want to show big landmarks like mountains or forests, but leave out tiny rocks or every individual tree. 

In practice, this can include deciding about whether or not to include a dataset at all when creating a map (e.g. in GIS or Python or other map-making software), or if we do include the dataset, if we want to filter it to only show certain features.

For example, you may want to include a dataset of public transit lines as a reference layer for a map of your city. However, you may not want to include every single transit route. An example of cartographic selection would be to only show major transit lines by pre-filtering the data by mode (e.g. only show metro/subway) or frequency (e.g. only show routes where a bus or train comes every 10 minutes or less). Now of course if the goal of your map and research is specifically about public transit, you may want to include all the routes. 

The process of selecting some, but not all of the data that you have available, reduces clutter on your maps and can make them easier to read. What data to include depends on your objectives, audience, and story.


### Cartographic generalization

Similar to selection is cartographic generalization, this is when mapmakers simplify real-world details to make maps clearer and less cluttered, especially at smaller scales. 

For example, a coastline with tons of tiny twists and inlets might get smoothed out—keeping the overall shape but removing unnecessary complexity. This helps the map stay readable without losing its key features. It’s like sketching a quick but accurate version of a photo instead of drawing every single pixel.

[SHORELINE EXAMPLE]

Another example would be that if you had a dataset of sports and recreation facilities in a city with data on the type of activity each is predominately used by (e.g. baseball, football, tennis, etc.). We can choose to have a different colour or symbol for each of these types, or generalize these to have them all look the same (e.g. the same shade of green). 


## Symbols and layer styling

Once we've decided what we want to include on our map, we have to decide how we want to style each layer. In some mapping tools, like QGIS, style options are often called *Symbology*

These are the common graphic styling options available for vector data layers. If you've worked with other design software, especially vector graphic software, many of these will be familiar.

Points:

- Symbol type (e.g. circle, square, etc.)
- Size
- Fill colour
- Stroke colour
- Stroke width
- Opacity

Lines:

- Width
- Colour
- Stroke style (e.g. solid, dashed, etc.)
- Opacity

Polygons:

- Fill colour
- Fill pattern (solid, hatching, etc.)
- Stroke colour
- Stroke width
- Stroke style (e.g. solid, dashed, etc.)
- Opacity

Note that there are other options as well, the above are just the most commonly used.


### Single-rule styling

Single-rule styling is when we want all features in a dataset to look the same, regardless of how they may different in terms of their attributes

In the example in [our notebook on introducing spatial data and GIS](../../urban-data-analytics/spatial-data-and-gis/spatial-data-and-gis.md), we created a simple map of Toronto where we had two vector datasets 1) ward administrative boundaries (polygons) and 2) public libraries (points). 

Each of these layers is styled via a single rule. For example, all libraries are blue squares, even though some libraries may be larger than others or have longer opening hours.

![Screenshot of QGIS with single-rule based styling for two layers](img/qgis-toronto-data-2.png)



### Data-defined styling

Visual variables often used for map data?






Style via data values
- categorical example - e.g. 
- numeric example - e.g. 
--- link to choropleth and prop symbol?





## Layers & Layouts: Putting it all together











