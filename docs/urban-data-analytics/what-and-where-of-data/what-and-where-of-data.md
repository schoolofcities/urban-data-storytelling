---
title: "Introduction to urban data"
author: "Karen Chapple, Julia Greenberg, Jeff Allen"
---

<br>
<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
  <iframe 
    src="https://www.youtube.com/embed/a2o8OKAH2RE" 
    style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" 
    frameborder="0" 
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
    allowfullscreen>
  </iframe>
</div>
<br>


## Where does data come from?

In data analysis, understanding the type and origin of data is essential to choosing the right methods for analysis, limitations in the data, and interpreting results. The following categories outline common types of data sources that we often encounter. These sources vary in how and why they are collected.


| Data source type      | Description                                                                 | Examples                                       |
|-----------------------|------------------------------------|------------------------------------------------|
| *Designed/Survey*        | Data collected through surveys, experiments, or designed methods.           | Census data (historical or current), research surveys, opinion polls |
| *Administrative*         | Data from routine operations or official records. Often open or public when government-run. | City records (public housing locations, public transit data), tax records, healthcare data (historical and current), school enrollment data |
| *Crowdsourced*           | Data contributed by the public or community-driven platforms.                | OpenStreetMap (OSM), Wikipedia, social media data, 311 data, Google reviews |
| *Event-Driven/Real-Time* | Data generated from sensors, transactions, or interactions. Often continuous and time-sensitive. | Satellite data, mobile phone GPS, IoT sensors, e-commerce transactions, website clicks |
| *Derived data*           | Data created by transforming or calculating metrics from existing data or simulations. | Indices like low-income prevalence or social deprivation, environmental quality scores, simulated datasets for testing or model training |


Sometimes data can be a combination, for example, both the [United States Census Bureau](https://www.census.gov/about/what/admin-data.html) and [Statistics Canada](https://www.statcan.gc.ca/en/our-data/where/administrative-data) collect a combination of survey data and administrative data.

<br>

![Map of average household income in Toronto using data from Statistics Canada (2020)](img/toronto-income.png)




## Data availability

Data availability refers to how accessible data is and the conditions under which it can be used. Key categories include:

*Public / Open data* - Data that is freely accessible to anyone and can be reused without restrictions. Open data is often provided by governments, research institutions, and public organizations. It is typically non-sensitive and available in machine-readable formats. Examples include aggregated census data, municipal open data, and OpenStreetMap.

*Restricted data*
Data that is available but comes with limitations due to privacy, security, or legal concerns. This includes sensitive datasets such as health data, dis-aggregate census data, and government records with personal identifiers that are redacted or protected.

*Proprietary data* - Data that is owned by a specific entity (e.g., a corporation or private organization) and is not freely available. Access is typically granted through licenses, paid subscriptions, or agreements. For example, cell phone mobility data from [Spectus](https://docs.spectus.ai/) can be used to measure [post-pandemic downtown recovery trends](https://downtownrecovery.com/charts/trends), real estate data from [Costar](https://www.costar.com/home/demo?utm_source=google&utm_medium=cpc&utm_campaign=8362819905&utm_content=85421354763&utm_term=costar%20data&utm_campaign_id=7013p000002MUoNAAW&gad_source=1&gclid=Cj0KCQjwna6_BhCbARIsALId2Z2fd8KIEBhSXancChMwmCO0cA0j-R7r_1hNQu85JD7SXKO78atAMFAaAp-lEALw_wcB) can be used to assess vacancy rates or rent prices, and consumer data from [Data Axle](https://www.data-axle.com/) can be used to study [the impact of new housing on migration patterns](https://www.urbandisplacement.org/maps/housing-by-block/).

<br>

![Crowdsourced OpenStreetMap data in Vancouver](img/osm.png)


## Data sources for urban analysis

The table below lists a handful of websites where you can find publicly available data about cities, the environment, land use, transportation, Indigenous communities, housing and homelessness. This is a non-exhaustive list; there are many other great data sources available. Note that municipalities' open data portals typically contain information on all or most of these topics. 

| Topic | Data sources (Global/Other) | Data sources (Canada-specific) | Data sources (U.S.-specific) |
| --- | --- | ----------- | ----------- |
| Demographic |     | [\- Canadian census data](https://www12.statcan.gc.ca/census-recensement/index-eng.cfm) | \- [U.S. census data  <br>](https://www.census.gov/data.html) (this is a user-friendly census tool; some universities and institutions have licenses) |
| Municipal |     | \- Open data portals (e.g., [Toronto](https://open.toronto.ca/), [Montreal](https://donnees.montreal.ca/), or [Vancouver](https://opendata.vancouver.ca/pages/home/)) | \- Open data portals (e.g., [Boston](https://data.boston.gov/), [New York](https://opendata.cityofnewyork.us/), or [San Francisco](https://datasf.org/opendata/)) |
| Environment and health |     | \- [NASA’s Earth Science Data Systems (ESDS) Program](https://www.earthdata.nasa.gov/data/catalog)  <br>\- [The Canadian Urban Environmental Health Research Consortium](https://canue.ca/)  <br>\- [Natural Resources Canada](https://natural-resources.canada.ca/science-data/data-analysis)  <br>\- [Environment and Climate Change Canada](https://open.canada.ca/data/organization/ec) | \- [Center for Disease Control (CDC) PLACES data](https://www.cdc.gov/places/index.html)  <br>\- [U.S. Environmental Protection Agency  <br>](https://www.epa.gov/enviro/data-downloads) \- [U.S. Geological Survey  <br>](https://www.usgs.gov/products/data-and-tools/overview)\- [Elevation data for the entire U.S.](https://catalog.data.gov/dataset/1-9th-arc-second-digital-elevation-models-dems-usgs-national-map-3dep-downloadable-data-co)  <br>\- [U.C. Berkeley Earth Sciences & Map Library](https://geodata.lib.berkeley.edu/)  <br>\- [U.C. Berkeley Geospatial Innovation Facility](http://gif.berkeley.edu/resources/data.html) |
| Land use and built environment | \- [OpenStreetMap](https://www.openstreetmap.org/)  <br>\- [OSMNx](https://github.com/gboeing/osmnx) - tool for extracting Open Street Map data for anywhere in the world  <br>\- [Google Maps data access](https://developers.google.com/maps/apis-by-platform) | \- [Land cover of Canada](https://open.canada.ca/data/en/dataset/ee1580ab-a23d-4f86-a09b-79763677eb47)  <br>\- Municipal-level zoning maps (e.g., in [Toronto](https://map.toronto.ca/maps/map.jsp?app%3DZBL_CONSULT)) | \- [OSMNx-derived downloads for the U.S.](https://dataverse.harvard.edu/dataverse/osmnx-street-networks)  <br>\- [Building footprints for the entire U.S.  <br>](https://github.com/microsoft/USBuildingFootprints)\- [National Zoning Atlas](https://www.zoningatlas.org/)  <br>\- [U.C. Berkeley Geospatial Innovation Facility](http://gif.berkeley.edu/resources/data.html) |
| Transportation | [\- Transitland](https://www.transit.land/) | \- [Metrolinx Open Data for the Greater Toronto Area](https://www.metrolinx.com/en/about-us/open-data)  <br>\- [Canadian Urban Transit Association](https://cutaactu.ca/reports-resources/statistics/)  <br>\- [Mobilizing Justice Hub](https://hub.mobilizingjustice.ca/) | \- [National Transit Database  <br>](https://www.transit.dot.gov/ntd/ntd-data)\- [National Household Travel Survey  <br>](https://nhts.ornl.gov/)\- Bike share data (e.g. [from Bay Wheels in San Francisco](https://www.lyft.com/bikes/bay-wheels/system-data))  <br>\- Transportation crash/injury data (e.g. [MassDOT](https://apps.crashdata.dot.mass.gov/cdp/home), [California](https://tims.berkeley.edu/)) |
| Indigenous communities | \- [Native Land Digital](https://native-land.ca/) | \- [First Nations Data Centre](https://fnigc.ca/first-nations-data-centre/) |     |
| Housing and homelessness | \- [Airbnb data (Inside Airbnb)](https://insideairbnb.com/explore/) | \- [Housing - Statistics Canada](https://www.statcan.gc.ca/en/subjects-start/housing)  <br>\- [Housing data from Canada Mortgage and Housing Corporation](https://www.cmhc-schl.gc.ca/professionals/housing-markets-data-and-research/housing-data) | \- [U.S. Department of Housing and Urban Development  <br>](https://data.hud.gov/data_sets.html)\- [Federal Housing Finance Agency](https://www.fhfa.gov/data/hpi/datasets)  <br>\- [Zillow housing data  <br>](https://www.zillow.com/research/data/)\- [Urban Displacement data](https://www.urbandisplacement.org/) |
| Economy and commerce | \- [Yelp open data](https://www.yelp.com/dataset) |     | \- [U.S. Bureau of Labor Statistics](https://www.bls.gov/data/)  <br>\- [Longitudinal Employer-Household Dynamics (LEHD)  <br>](https://lehd.ces.census.gov/data/)\- [Federal Reserve Economic Data (FRED)  <br>](https://fred.stlouisfed.org/)\- [Annual Business Survey (ABS)](https://www.census.gov/programs-surveys/abs.html)  <br>\- [County Business Patterns](https://www.census.gov/programs-surveys/cbp.html) |
| Other | \- [Google Dataset Search  <br>](https://datasetsearch.research.google.com/)\- [ArcGIS Open Data Portal](https://hub.arcgis.com/search) | \- [ Open Government Canada (federal open data portal)](https://search.open.canada.ca/opendata/) | \- [U.S. Data.gov Open Data Portal](https://catalog.data.gov/dataset)  <br>\- [Harvard Dataverse](https://dataverse.harvard.edu/dataverse/harvard) |



[Web scraping](https://en.wikipedia.org/wiki/Web_scraping), or extracting information from the internet, is another method for creating datasets. Since the data do not already exist and must be created, this can be more time-intensive than using existing datasets. However, packages like [beautifulsoup](https://pypi.org/project/beautifulsoup4/) or [selenium](https://pypi.org/project/selenium/) in Python make this process easier.



## Data formats

Data format refers to how data is stored and structured. In practice, this is most relevant when loading and saving data. The data format you choose to use depends on the data's size, structure, use, how it is being stored, and whether it is spatial (has a geometry column) or not.

Some of the most common data formats for *non-spatial* data are:

- [CSV (comma separated values)](https://en.wikipedia.org/wiki/Comma-separated_values) `.csv`
- [Excel](https://www.exceldemy.com/learn-excel/files/) `.xlsx`
- [JSON (JavaScript Object Notation)](https://en.wikipedia.org/wiki/JSON) `.json`
- [XML (Extensible Markup Language)](https://en.wikipedia.org/wiki/XML) `.xml`

Some of the most common data formats for *spatial* data are (see *[Spatial data & GIS](../spatial-data-and-gis/spatial-data-and-gis.md)* for more information):

- [GeoJSON](https://en.wikipedia.org/wiki/GeoJSON) `.geojson`
- [GeoPackage](https://en.wikipedia.org/wiki/GeoPackage) `.gpkg`
- [Shapefile](https://en.wikipedia.org/wiki/Shapefile) `.shapfile`
- [Geodatabase](https://en.wikipedia.org/wiki/Geodatabase_(Esri)) `.gdb`

While the file formats above suffice for relatively small or simple datasets, very large or complex datasets require more efficient storage via formats like [Parquet](https://en.wikipedia.org/wiki/Apache_Parquet) (see [instructions for Python](https://arrow.apache.org/docs/python/parquet.html)). [Relational databases](https://en.wikipedia.org/wiki/Relational_database) are another commonly used data storage format for "big data" because they are more efficient, faster to query, more secure, and can be accessed by multiple users.



## Data types

It's important to make sure that each variable in your dataset is in the right format so the computer interprets it correctly. For example, if you load a `.csv` file with a column representing the population of a neighbourhood, you would want to make sure this variable is interpreted as a number and not a string of characters so you can easily use this column to calculate additional statistics (e.g. sum of population in all neighbourhoods, population density in each neighbourhood). 

See the table below for a list of common data types used in data analysis software.

| Data Type | Description                                                    | Example                               |
|---------------|--------------------------------------------------------------------|-------------------------------------------|
| Integer (int)   | Whole numbers without decimal points.                            | `5`, `-3`, `42`                          |
| Float          | Numbers with decimal points, representing real numbers.           | `3.14`, `-0.001`, `2.718`                |
| String (str)   | A sequence of characters, used for textual data.                   | `"Hello"`, `"Data analysis"`, `"123"`     |
| Boolean (bool) | Represents binary values: `True` or `False`.                        | `True`, `False`                          |
| List           | Ordered collection of items, can contain different data types.     | `[1, 2, 3]`, `["apple", "banana"]`        |
| Tuple          | Immutable sequence of items, like lists but cannot be modified.    | `(1, 2, 3)`, `("apple", "banana")`        |
| Dictionary (dict) | Collection of key-value pairs, often used for mapping.          | `{"country": "Alice", "age": 30}`            |
| DateTime       | Used for representing date and time.                               | `2025-04-09 14:32:00`, `2021-01-01`       |
| Set            | Unordered collection of unique items.                              | `{1, 2, 3}`, `{"apple", "banana"}`        |
| NoneType       | Represents the absence of a value, or null.                        | `None`                                   |

Different software (e.g. Excel, Python, R, QGIS, etc.) might have slightly different names for each of the above. For example, this page provides a nice summary of [data types in Python](https://www.geeksforgeeks.org/python-data-types/).



## Levels of measurement

While *data types* specify what kind of data a variable can hold, *levels of measurement* describe how data is structured and the relationships between different values. They refer to how we can classify and interpret the data in terms of its inherent ordering, spacing, and possible mathematical operations.

- *Nominal*: Categorical data with no inherent order (e.g., colors, countries, land-use types e.g. `Urban`, `Wetlands`, `Forest`, etc.).

- *Ordinal*: Data with a meaningful order, but unknown or not always equal differences between values (e.g., movie ratings like `Good`,`Okay`, or `Bad`, or levels of education e.g. `High School`, `Bachelors`, `Masters` ).

- *Interval*: Ordered data with equal intervals between values but no true zero (e.g., temperature in Celsius or Fahrenheit, datetime).

- *Ratio*: Ordered data with equal intervals and a true zero point, allowing for meaningful ratios (e.g., length, area, income).



## Software and tools

There are hundreds of software and tools for processing, analyzing, and visualizing data. 

When choosing which software to use to analyze or visualize data, one of the main considerations is whether the software is *open source* or *proprietary*. Open source software has its source code publicly available and can be modified by anyone on the internet. Proprietary software’s source code is not publicly available, is typically developed and updated by a closed group, and is licensed to users in exchange for payment. Read [this article](https://www.geeksforgeeks.org/difference-between-open-source-software-and-proprietary-software/) if you're interested in learning more about the difference between the two.

Spreadsheet software, like [Excel](https://www.microsoft.com/en-us/microsoft-365/excel), [Google Sheets](https://workspace.google.com/products/sheets/), and [LibreOffice calc](https://www.libreoffice.org/discover/calc/), can be great for viewing and exploring data and doing quick analyses. However, they can be very limited for serious data analysis. They struggle with large datasets, lack robust tools for cleaning and transforming complex data, have very limited options for spatial/geographic data, and make reproducibility nearly impossible. Plus, it's easy to introduce silent errors with formulas or copy-pasting. For anything beyond basic summaries or charts, scripting languages like `R` or `Python` are far more powerful, reliable, and scalable.

Geographic information systems (GIS) are tools and software specifically designed for analyzing, processing, and visualizing spatial data. There are desktop point-and-click software like [QGIS](https://qgis.org/) that are great for exploratory and smaller-scale analyses and visualization, and programming languages like `Python` have many libraries for working with spatial data.

In this course, other than common spreadsheet software, we will focus on *open source* software because it is free and available to everyone. Below is a list of some of the main open source programming languages, software, and tools that we recommend using for data analysis and mapping.

| Purpose | Software/Tools |
|--------------|------------|
| Analyzing and visualizing data | [Python](https://www.python.org/), [R](https://www.r-project.org/), [SQL](https://en.wikipedia.org/wiki/SQL, [QGIS](https://qgis.org/) (for spatial data)) |
| Making pretty graphics | [Inkscape](https://inkscape.org/), [GIMP](https://www.gimp.org/) |
| Web development | [HTML](https://en.wikipedia.org/wiki/HTML), [CSS](https://en.wikipedia.org/wiki/CSS), [Javascript](https://en.wikipedia.org/wiki/JavaScript) |
| Web-based maps and visualization | [D3](https://d3js.org/), [MapLibre](https://maplibre.org/), [Protomaps](https://docs.protomaps.com/pmtiles/) |
| Hosting / project management | [GitHub](https://github.com/) |


## Data analysis process

While is no set of specific step-by-step instructions for data analysis -- each project involves unique data sources, variables, methodologies, and outputs -- there is a general [framework](https://www.geeksforgeeks.org/six-steps-of-data-analysis-process/) that we recommend following:

1. *Define the problem or research question.* What question are you trying to answer with data? Is data analysis the best way to answer that question? Who is the audience for your data analysis, and what do they want to know?
2. *Collect data.* What kind of data do you need to answer your research question, and where can you find it? Does it exist? In what format?
3. *Clean data.* Make sure the data has appropriate variable names, does not have misspellings or other errors, and the variables are the correct data types. Get rid of any redundant or irrelevant data that you don't need, and determine a method for dealing with any missing values.
4. *Analyze data.* Start by exploring the data to understand its structure and any statistical patterns. Then perform your analysis -- for example, are you trying to uncover trends, or measure relationships among variables?
5. *Visualize data.* Create plots, maps, or other visual representations that illustrate the structure, trends, or relationships present in your data.
6. *Present data.* Clearly communicate your results to your intended audience. This could involve writing a report, or creating a presentation or interactive dashboard. Whatever gets your message across!

It is important to iterate through some of these steps and make updates as needed. For example, if step 5 (visualize your data) reveals that you have an imbalanced dataset, you may need to go back to step 3 or 4 to address this. And of course once you hit steps 5 and 6, you might discover something so interesting that you'll want to collect more data and repeat the process all over again! :)


## Getting help

Learning new software for data analysis or mapping can be confusing and frustrating. Luckily, there are a lot of great resources that can help!

The first place you should look when you're confused about how to do something is the *official documentation*. For example, if you're having trouble loading a CSV file in Python using the `pandas` package, take a look at [the documentation for `.read_csv`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html) on the pandas website. Or if you're not sure how to create a spatial buffer in QGIS, check out the [QGIS buffer operations page](https://qgis3-10-geoanalysis-un.readthedocs.io/en/latest/vector/buffer.html#:~:text=To%20create%20a%20buffer%2C%20click,specify%20the%20unit%20of%20measure).

If you're still stuck on a question, Google it! Chances are, someone else has dealt with a similar issue, and there is likely a community of people helping them out. For example, one of the most popular resources for coding is [Stack Overflow](https://stackoverflow.com/), a website where programmers ask and answer questions. Responses with the most votes are shown at the top, making it easy to find helpful code snippets and explanations that you can adapt for your own needs. The website is so widely used that Stack Overflow posts will usually show up towards the top when you Google search coding questions.

There are also websites like [W3Schools](https://www.w3schools.com/) and [GeeksforGeeks](https://www.geeksforgeeks.org/) that offer online courses and tutorials covering everything from sorting a list in Python to building complicated statistical models. These websites show up often as results for relevant Google searches.

And of course there are AI chatbots like [ChatGPT](https://chatgpt.com/). These tools can be extremely helpful for debugging code, writing code, or providing instructions for GIS. However, be careful and don't trust them blindly, as they are often wrong, and sometimes make up packages or functions that don't exist. Also, if you use chatbots for help, make sure you understand what they are telling you. Asking for guidance or hints about specific, discrete questions is much better than asking the chatbot to write an entire Python script for you.

The more you rely on chatbots, the less you will learn, and the less you will be able to do on your own. Learning data analysis or coding in particular can feel like an uphill battle, but if you start with a solid understanding of what you're doing, you'll be better equipped to prompt and efficiently use chatbots later on. Most importantly, you will have a stronger foundation of knowledge and will be able to tackle complicated problems in the future.