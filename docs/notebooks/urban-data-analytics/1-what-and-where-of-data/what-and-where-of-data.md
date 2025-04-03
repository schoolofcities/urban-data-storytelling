# What and where of data

## Where does data come from?

Both the [United States Census Bureau](https://www.census.gov/about/what/admin-data.html) and [Statistics Canada](https://www.statcan.gc.ca/en/our-data/where/administrative-data) collect a combination of *survey* data and *administrative* data. Survey data, like the decennial census or American Community Survey in the United States, involves asking people for information about themselves or another topic. Administrative data, like tax records, are collected by governments or other entities for the purpose of running programs or providing services.

Another type of data that is often used in urban analyses comes from *[remote sensing](https://www.earthdata.nasa.gov/learn/earth-observation-data-basics/remote-sensing)*, which involves measuring the physical characteristics of an area from a distance ([USGS](https://www.usgs.gov/faqs/what-remote-sensing-and-what-it-used#:~:text=Remote%20sensing%20is%20the%20process,sense%22%20things%20about%20the%20Earth.)). Spatial data collected via remote sensing is often used in analyses of the built or natural environment (e.g., land cover classification or urban growth). One example of this type of data is the satellite imagery layer in Google Maps:

![Satellite imagery of Ottawa](img/satellite_imagery_ottawa.png)

Crowdsourced data, which is collected from the public - usually online or via social media or apps - often helps to fill information gaps left by official data sources. For example, [FixMyStreet](https://www.fixmystreet.com/) allows residents in the UK to report problems like graffiti or potholes in their neighborhood and sends the information directly to local authorities. [OpenStreetMap](https://www.openstreetmap.org/) is a popular crowdsourced mapping dataset with billions of data points representing buildings, streets, transit lines, and [much more](https://wiki.openstreetmap.org/wiki/Map_features).

![OpenStreetMap in Vancouver](img/osm.png)

[Web scraping](https://en.wikipedia.org/wiki/Web_scraping), or extracting information from the internet, is another method for creating datasets. Since the data do not already exist and must be created, this can be more time-intensive than using existing datasets. However, packages like [beautifulsoup](https://pypi.org/project/beautifulsoup4/) or [selenium](https://pypi.org/project/selenium/) in Python make this process easier.

## Data sources for urban analysis

The table below lists a handful of websites where you can find freely available data about cities, the environment, land use, transportation, Indigenous communities, housing and homelessness. This is a non-exhaustive list; there are many other great data sources available. Note that municipalities' open data portals typically contain information on all or most of these topics. For more information about census data specifically, see *[Canadian census data](../canadian-census-data/canadian-census-data.md)*.

| Topic | Data sources |
|--------------|------------|
| Cities | - Open data portals (e.g., [Toronto](https://open.toronto.ca/), [Montreal](https://donnees.montreal.ca/), & [Vancouver](https://opendata.vancouver.ca/pages/home/)) |
| Environment | - [NASA's Earth Science Data Systems (ESDS) Program](https://www.earthdata.nasa.gov/data/catalog)<br>- [The Canadian Urban Environmental Health Research Consortium](https://canue.ca/)<br>- [Natural Resources Canada](https://natural-resources.canada.ca/science-data/data-analysis)<br>- [Environment and Climate Change Canada](https://open.canada.ca/data/organization/ec) 
| Land use | - [OpenStreetMap](https://www.openstreetmap.org/)<br>- [Land cover of Canada](https://open.canada.ca/data/en/dataset/ee1580ab-a23d-4f86-a09b-79763677eb47)<br>- Municipal-level zoning maps (e.g., in [Toronto](https://map.toronto.ca/maps/map.jsp?app=ZBL_CONSULT)) |
| Transportation | - [Metrolinx Open Data for the Greater Toronto Area](https://www.metrolinx.com/en/about-us/open-data)<br>- [Canadian Urban Transit Association](https://cutaactu.ca/reports-resources/statistics/)<br>- [Mobilizing Justice Hub](https://hub.mobilizingjustice.ca/)<br>- [Transitland](https://www.transit.land/) |
| Indigenous communities | - [First Nations Data Centre](https://fnigc.ca/first-nations-data-centre/)<br>- [Native Land Digital](https://native-land.ca/) |
| Housing and homelessness | - [Housing - Statistics Canada](https://www.statcan.gc.ca/en/subjects-start/housing)<br>- [Housing data from Canada Mortgage and Housing Corporation](https://www.cmhc-schl.gc.ca/professionals/housing-markets-data-and-research/housing-data) |

In addition to free, open data like the datasets in the above table, there are also proprietary datasets that are useful for analyzing urban phenomena require payment to access. For example, cell phone mobility data from [Spectus](https://docs.spectus.ai/) can be used to measure [post-pandemic downtown recovery trends](https://downtownrecovery.com/charts/trends), real estate data from [Costar](https://www.costar.com/home/demo?utm_source=google&utm_medium=cpc&utm_campaign=8362819905&utm_content=85421354763&utm_term=costar%20data&utm_campaign_id=7013p000002MUoNAAW&gad_source=1&gclid=Cj0KCQjwna6_BhCbARIsALId2Z2fd8KIEBhSXancChMwmCO0cA0j-R7r_1hNQu85JD7SXKO78atAMFAaAp-lEALw_wcB) can be used to assess vacancy rates or rent prices, and consumer data from [Data Axle](https://www.data-axle.com/) can be used to study [the impact of new housing on migration patterns](https://www.urbandisplacement.org/maps/housing-by-block/).

## Data formats

Data format refers to how data is stored and structured. In practice, this is most relevant when loading and saving data. The data format you choose to use depends on the data's size, structure, use, how it is being stored, and whether it is spatial (has a geometry column) or not.

Some of the most common data formats for *non-spatial* data are:

- [CSV (comma separated values)](https://en.wikipedia.org/wiki/Comma-separated_values) `.csv`
- [JSON (JavaScript Object Notation)](https://en.wikipedia.org/wiki/JSON) `.json`
- [XML (Extensible Markup Language)](https://en.wikipedia.org/wiki/XML) `.xml`

Some of the most common data formats for *spatial* data are (see *[Spatial data & GIS](../spatial-data-and-gis/spatial-data-and-gis.md)* for more information):

- [GeoJSON](https://en.wikipedia.org/wiki/GeoJSON) `.geojson`
- [GeoPackage](https://en.wikipedia.org/wiki/GeoPackage) `.gpkg`
- [Shapefile](https://en.wikipedia.org/wiki/Shapefile) `.shapfile`
- [Geodatabase](https://en.wikipedia.org/wiki/Geodatabase_(Esri)) `.gdb`

While the file formats above suffice for relatively small or simple datasets, very large or complex datasets require more efficient storage via formats like [Parquet](https://en.wikipedia.org/wiki/Apache_Parquet) (see [instructions for Python](https://arrow.apache.org/docs/python/parquet.html)). [Relational databases](https://en.wikipedia.org/wiki/Relational_database) are another commonly used data storage format for "big data" because they are more efficient, faster to query, more secure, and can be accessed by multiple users.

## Data types

It's important to make sure that each variable in your dataset is in the right format so the computer interpets it correctly. For example, if you load a CSV file with a column representing the population of a census tract, you want to make sure this variable is interpreted as a number and not a string of characters. See the table below for a list of common data types, and see [this link](https://amplitude.com/blog/data-types) for a more detailed explanation of each one.

![Table of common data types ([source](https://amplitude.com/blog/data-types))](img/data_types.png)

When coding in Python, you'll also need to get acquainted with Python's built-in data types, some of which are explained [here](https://www.geeksforgeeks.org/python-data-types/) - but don't worry about this yet; we'll cover this in more detail later.

## Software and tools

When choosing which software to use to analyze or visualize data, one of the main considerations is whether the software is *open source* or *proprietary*. Open source software has its source code publicly available and can be modified by anyone on the internet. Proprietary software’s source code is not publicly available, is typically developed and updated by a closed group, and is licensed to users in exchange for payment. Read [this link](https://www.geeksforgeeks.org/difference-between-open-source-software-and-proprietary-software/) if you're interested in learning more about the difference between the two.

In this course, we will focus on *open source* software because it is free and available to everyone. Below is a list of some of the main open source programming languages, software, and tools that we recommend using for data analysis and mapping.

| Purpose | Software/Tools |
|--------------|------------|
| Mapping | [QGIS](https://qgis.org/), [Python](https://www.python.org/), [R](https://www.r-project.org/)
| Analyzing / visualizing data | [Python](https://www.python.org/), [R](https://www.r-project.org/), [SQL](https://en.wikipedia.org/wiki/SQL) |
| Graphic design / layouts | [Inkscape](https://inkscape.org/), [GIMP](https://www.gimp.org/) |
| Web development | [HTML](https://en.wikipedia.org/wiki/HTML), [CSS](https://en.wikipedia.org/wiki/CSS), [Javascript](https://en.wikipedia.org/wiki/JavaScript), [Svelte](https://svelte.dev/) |
| Web-based maps/visualization | [D3](https://d3js.org/), [MapLibre](https://maplibre.org/), [PMtiles](https://docs.protomaps.com/pmtiles/) |
| Hosting / project management | [GitHub](https://github.com/) |

## Data analysis process

While is no set of specific step-by-step instructions for data analysis -- each project involves unique data sources, variables, methodologies, and outputs -- there is a general [framework](https://www.geeksforgeeks.org/six-steps-of-data-analysis-process/) you should follow.

1. **Define the problem or research question.** What question are you trying to answer with data? Is data analysis the best way to answer that question? Who is the audience for your data analysis, and what do they want to know?
2. **Collect data.** What kind of data do you need to answer your research question, and where can you find it? Does it exist? In what format?
3. **Clean data.** Make sure the data has appropriate variable names, does not have misspellings or other errors, and the variables are the correct data types. Get rid of any redundant or irrelevant data that you don't need, and determine a method for dealing with any missing values.
4. **Analyze data.** Start by exploring the data to understand its structure and any statistical patterns. Then perform your analysis -- for example, are you trying to uncover trends, or measure the relationship among variables?
5. **Visualize data.** Create plots, maps, or other visual representations that illustrate the structure, trends, or relationships present in your data.
6. **Present data.** Clearly communicate your results to your intended audience. This could involve writing a report, or creating a presentation or interactive dashboard. Whatever gets your message across!

It is important to iterate through some of these steps and make updates as needed. For example, if step 5 (visualize your data) reveals that you have an imbalanced dataset, you may need to go back to step 3 or 4 to address this.

## Getting help

Learning new software for data analysis or mapping can be confusing and frustrating. Luckily, there are a lot of great resources that can help!

The first place you should look when you're confused about how to do something is the *official documentation*. For example, if you're having trouble loading a CSV file in Python using the `pandas` package, take a look at [this page](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html) on the pandas website. If you're not sure how to create a spatial buffer in QGIS, check out the [QGIS buffer operations page](https://qgis3-10-geoanalysis-un.readthedocs.io/en/latest/vector/buffer.html#:~:text=To%20create%20a%20buffer%2C%20click,specify%20the%20unit%20of%20measure).

If you're still stuck on a question, Google it! Chances are, someone else has dealt with a similar issue, and there is likely a community of people helping them out. For example, one of the most popular resources for coding is [Stack Overflow](https://stackoverflow.com/), a website where programmers ask and answer questions. Responses with the most votes are shown at the top, making it easy to find helpful code snippets and explanations that you can adapt for your own needs. The website is so widely used that Stack Overflow posts will usually show up towards the top when you Google search coding questions.

There are also websites like [W3Schools](https://www.w3schools.com/) and [GeeksforGeeks](https://www.geeksforgeeks.org/) that offer online courses and tutorials covering everything from sorting a list in Python to building complicated statistical models. These websites show up often as results for relevant Google searches.

Finally, a word of caution about using AI chatbots like [ChatGPT](https://chatgpt.com/) - while these chatbots can be extremely helpful for debugging code or providing instructions about how to do a spatial join in QGIS, *be careful*. They are often wrong, and sometimes make up packages or functions that don't exist. Also, if you use chatbots for coding help, make sure you understand what they are telling you. Asking for guidance or hints about specific, discrete questions is much better than asking the chatbot to write an entire Python script for you. The more you rely on the chatbots, the less you will learn, and the less you will be able to do on your own. Learning coding in particular can feel like an uphill battle, but if you start with a solid foundation and thorough understanding of how it works, you will feel much more confident in your ability to tackle more complicated problems later on.

Along the same lines, there are tools like [Jupyter AI](https://jupyter-ai.readthedocs.io/en/latest/) that offer AI assistance integrated into your coding environment. While these can be very useful and help you code more efficiently, remember that the more you rely on tools like this early on in your coding journey, the more dependent you will be on them and the less you will learn.