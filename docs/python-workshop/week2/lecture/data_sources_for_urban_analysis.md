# Reference: Data Sources for Urban Analysis

Urban data can come from many different organizations, platforms, and levels of government. The sources below are useful starting points when looking for data about cities, demographics, transportation, housing, land use, the environment, and related topics.

This is **not an exhaustive list**. Municipal open-data portals often contain datasets across several of these categories, and many other sources may be available for a particular city or research question.

Not all urban data is provided as a ready-to-use CSV or spreadsheet. Data may instead come as Excel files, JSON responses, APIs, geographic files, databases, or other formats. In many cases, these sources can still be converted into a tabular structure for analysis with pandas.

## Demographic data

Useful sources include:

- [Statistics Canada Census of Population](https://www12.statcan.gc.ca/census-recensement/index-eng.cfm)
- [United States Census Bureau](https://www.census.gov/)

These sources provide information such as population, age, income, housing, immigration, education, employment, and household characteristics.

## Municipal open data

Many municipal governments publish public datasets through open-data portals. Examples include:

### Canada

- [Toronto Open Data](https://open.toronto.ca/)
- [Montréal Open Data](https://donnees.montreal.ca/)
- [Vancouver Open Data](https://opendata.vancouver.ca/)

### United States

- [Boston Open Data](https://data.boston.gov/)
- [NYC Open Data](https://opendata.cityofnewyork.us/)
- [DataSF](https://datasf.org/)

Municipal portals may include data on public facilities, permits, transportation, trees, parks, budgets, service requests, planning, housing, public safety, and other city operations.

## Environment and health

Potential sources include:

- [NASA Earthdata](https://www.earthdata.nasa.gov/)
- [Canadian Urban Environmental Health Research Consortium](https://canue.ca/)
- [Natural Resources Canada](https://natural-resources.canada.ca/)
- [Environment and Climate Change Canada Open Data](https://open.canada.ca/en/open-data)
- [CDC PLACES](https://www.cdc.gov/places/)
- [United States Environmental Protection Agency](https://www.epa.gov/)
- [United States Geological Survey](https://www.usgs.gov/)

These sources may provide environmental exposure, land cover, climate, elevation, pollution, health, and satellite data.

## Land use and the built environment

Useful sources and tools include:

- [OpenStreetMap](https://www.openstreetmap.org/)
- [OSMnx](https://github.com/gboeing/osmnx)
- [Google Maps Platform](https://developers.google.com/maps)
- [Land Cover of Canada](https://open.canada.ca/data/en/dataset)
- municipal zoning and planning datasets, often available through local open-data portals
- [National Zoning Atlas](https://www.zoningatlas.org/)

OpenStreetMap and OSMnx can be used to obtain information about streets, buildings, amenities, transit stops, parks, and other features of the built environment.

## Transportation

Potential sources include:

- [Transitland](https://www.transit.land/)
- [Metrolinx Open Data](https://www.metrolinx.com/en/about-us/open-data)
- [Canadian Urban Transit Association](https://cutaactu.ca/)
- [Mobilizing Justice](https://mobilizingjustice.ca/)
- [United States National Transit Database](https://www.transit.dot.gov/ntd)
- [United States National Household Travel Survey](https://nhts.ornl.gov/)

Transit agencies and municipal portals may also publish schedules, routes, ridership, bike-share trips, traffic counts, collision records, and real-time vehicle information.

## Indigenous communities

Sources include:

- [Native Land Digital](https://native-land.ca/)
- [First Nations Information Governance Centre](https://fnigc.ca/)

When using data concerning Indigenous communities, pay particular attention to data governance, community ownership, consent, interpretation, and appropriate use.

## Housing and homelessness

Useful sources include:

- [Inside Airbnb](https://insideairbnb.com/)
- [Statistics Canada housing data](https://www.statcan.gc.ca/en/subjects-start/housing)
- [Canada Mortgage and Housing Corporation](https://www.cmhc-schl.gc.ca/)
- [United States Department of Housing and Urban Development](https://data.hud.gov/)
- [Federal Housing Finance Agency](https://www.fhfa.gov/data)
- [Zillow Research Data](https://www.zillow.com/research/data/)
- [Urban Displacement Project](https://www.urbandisplacement.org/)

These sources may include information on rents, home prices, housing supply, vacancies, homelessness, short-term rentals, affordability, and displacement.

## Economy and commerce

Potential sources include:

- [Yelp Open Dataset](https://business.yelp.com/data/resources/open-dataset/)
- [United States Bureau of Labor Statistics](https://www.bls.gov/)
- [Longitudinal Employer-Household Dynamics](https://lehd.ces.census.gov/)
- [Federal Reserve Economic Data](https://fred.stlouisfed.org/)
- [United States Annual Business Survey](https://www.census.gov/programs-surveys/abs.html)
- [United States County Business Patterns](https://www.census.gov/programs-surveys/cbp.html)

These sources can support analysis of employment, businesses, industries, commuting, commercial activity, and local economic conditions.

## General data-search tools

When you do not know which organization holds the data, start with:

- [Google Dataset Search](https://datasetsearch.research.google.com/)
- [ArcGIS Hub](https://hub.arcgis.com/)
- [Open Government Canada](https://search.open.canada.ca/opendata/)
- [Data.gov](https://data.gov/)
- [Harvard Dataverse](https://dataverse.harvard.edu/)

Web scraping can also be used to turn information published on websites into a dataset. However, it is usually more time-consuming than downloading an existing dataset and may involve technical, legal, or ethical restrictions.

## Before using a dataset

Finding a dataset is only the first step. Before beginning an analysis, ask:

- Who created or collected the data?
- Why was it collected?
- What does each row represent?
- What geographic area and time period does it cover?
- Which people, places, or events may be missing?
- How are important variables defined?
- Is the data current?
- Are there restrictions on how it can be used?
- Is it tabular already, or will it need to be converted?

## Further reference

This list is adapted from the **Data sources for urban analysis** section of the School of Cities textbook:

[Introduction to urban data: Data sources for urban analysis](https://schoolofcities.github.io/urban-data-storytelling/urban-data-analytics/what-and-where-of-data/what-and-where-of-data.html#data-sources-for-urban-analysis)

Refer to the full page for additional links and broader discussion of urban data, data formats, software, and the data-analysis process.
