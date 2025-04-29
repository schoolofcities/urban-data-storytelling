---
title: "Measuring the city: metrics and indicators"
author: "Karen Chapple, Julia Greenberg, Jeff Allen"
---

This page covers 1) common metrics and indicators used in urban analysis, 2) spatial units and measures of aggregation often used for urban analysis, and 3) limitations and biases for working with urban datasets to keep in mind when working with urban data.



## Common metrics and indicators for urban analyses

The table below lists examples of variables/metrics that are used in urban analyses, grouped by topic.

| Topic | Common metrics |
|--------------|------------|
| People / socioeconomics | - Population density (e.g., population per square kilometer)<br>- Median income<br>- Race/ethnicity<br>- [Displacement risk](https://www.urbandisplacement.org/maps/california-estimated-displacement-risk-model/)<br>- [Social vulnerability index](https://www.atsdr.cdc.gov/place-health/php/svi/svi-interactive-map.html)<br>- Population change<br>- Inequality metrics (e.g., Gini index - [US](https://www.census.gov/topics/income-poverty/income-inequality/about/metrics/gini-index.html) & [Canada](https://data.worldbank.org/indicator/SI.POV.GINI?locations=CA))<br>- Crime rate<br>- Education level (e.g., % with bachelor’s degree, master’s degree)<br>- [Dissimilarity index](https://www.censusscope.org/about_dissimilarity.html) of racial segregation<br>- Voting patterns (e.g., in [Toronto](https://schoolofcities.github.io/place-and-politics-toronto)) |
| Housing | - % owners/renters<br>- Median rent & home value<br>- Vacancy rate<br>- Cost burden<br>- Core housing need<br>- Number of units built or permits issued (e.g., [Canadian ADU analysis](https://schoolofcities.github.io/gentle-density/adu-development-in-canadian-cities); [market-rate housing in the Bay Area](https://www.urbandisplacement.org/blog/does-new-market-rate-housing-displace-low-income-people/)) |
| Land use | - [Walk score](https://www.walkscore.com/)<br>- [Entropy index for land use mix](https://www.geographyrealm.com/calculating-land-use-mix-with-gis/)<br>- [Change in land cover (or forest)](https://schoolofcities.github.io/historical-land-cover-toronto/)<br>- Zoning (e.g., [zoning policy changes](https://schoolofcities.github.io/gentle-density/toronto-rooming-houses); [residential zoning in Canadian cities](https://schoolofcities.github.io/yellowbelt-canadian-cities-2022/)) |
| Economics / employment | Job density (e.g., [Longitudinal Employer-Household Dynamics](https://lehd.ces.census.gov/) in the US; [Canadian Employer-Employee Dynamics Database](https://www23.statcan.gc.ca/imdb/p2SV.pl?Function=getSurvey&SDDS=5228) in Canada)<br>- Commuting patterns<br>- [Venture capital investment by city](https://schoolofcities.github.io/venture-capital-canada/)<br>- [Sales by sector downtown](https://docs.google.com/presentation/d/1hXiIEZ7L5KxM7x11Xdwf_JDRgLxap5kB/edit?slide=id.p20#slide=id.p20)<br>- Downtown recovery post-pandemic (e.g., [trends](https://downtownrecovery.com/charts/canada_trends); [Urban Activity Atlas](https://schoolofcities.github.io/urban-activity-atlas/)) |
| Transportation | - Commute mode (e.g., % of people by census tract who commute via public transit vs car)<br>- Public transit accessibility (e.g., "walkshed" around transit stations; [% of population within given distance of rail station](https://schoolofcities.github.io/rail-transit-and-population-density/); [population near individual transit stations](https://schoolofcities.github.io/tod-toronto-1996-to-2021/))<br>- [E-bike trip distance](https://schoolofcities.github.io/bike-share-toronto/efit-analysis)<br>- [Bike share trips in Toronto](https://schoolofcities.github.io/bike-share-toronto/trips-062024)<br>- [Traffic violations](https://schoolofcities.github.io/king-street-toronto/traffic-violations) |
| Environment | - [Emissions/air pollution](https://schoolofcities.github.io/air-pollution-and-premature-mortality))<br>- Urban heat (e.g., [heat exposure in Toronto](https://schoolofcities.github.io/heat-vulnerability-toronto/))<br>- [Greenness](https://nasa-eej.projects.earthengine.app/view/wherethegrassgrowsgreener))<br>- Park access (e.g., distance to nearest park)<br>- Flood maps (e.g., [Toronto](https://schoolofcities.github.io/flood-data-equity/); [FEMA](https://hazards-fema.maps.arcgis.com/apps/webappviewer/index.html?id=8b0adb51996444d4879338b5529aa9cd); [Canada](https://natural-resources.canada.ca/science-data/science-research/flood-mapping))<br>- [Tree canopy coverage](https://schoolofcities.github.io/trees-toronto/dot-map) |
| Health | - Life expectancy<br>- Prevalence of chronic diseases (e.g., diabetes, asthma) |





## Common spatial units and measures of aggregation

Urban data is often linked to specific places. This is often called *spatial* or *geographic* data.

When analyzing spatial data, our analysis is often at the level of specific *spatial units* or *unit of aggregations*.  Sometimes our data is directly collected at these units, while sometimes it is useful to aggregate large datasets to these units to help analyses and visualizations. 

When working with urban data, it's essential to consider how geographic boundaries are defined. Standard units like census tracts or zip codes may not reflect actual community identities and are subject to change over time. 

Below are spatial units and types of encoding that are often used for collecting and analyzing urban data. 

In our notebook on [spatial data and GIS](notebooks/urban-data-analytics/spatial-data-and-gis/spatial-data-and-gis.md), we go into details on how different spatial data is structured, and how we can begin to view, explore, and analyze different data in GIS.


### Administrative or political boundaries

Political boundaries that delineate jurisdictions for different levels of government, from national down to local levels. Countries, provinces or states, counties, municipalities, electoral districts or city wards, and within cities, neighbourhood planning areas, are all examples of commonly used spatial units. 

![Federal electoral district in Saskatoon](img/saskatoon.jpg)


### Census geographies

National censuses aggregate data to a variety of spatial units ranging in size, many are the same as administrative and political boundaries, as well as many smaller-geography boundaries that are super useful for urban- and neighbourhood-scale maps and analyses. Census tracts (usually in the range of 2,500 and 8,000 persons) and Dissemination Areas (400 to 700 persons) are two scales that are often used. Check out ([Statistics Canada documentation](https://www12.statcan.gc.ca/census-recensement/2021/geo/sip-pis/boundary-limites/index2021-eng.cfm?year=21), [U.S. Census documentation](https://www.census.gov/geographies/mapping-files/time-series/geo/cartographic-boundary.html)) or see our notebook on [Canadian census data](../canadian-census-data/canadian-census-data.md) for more information.

![Common census boundaries in Toronto](img/census-boundaries-legend-eg.png)


### Grids

A grid is repetitive tesselation spread across the surface of a map. Grids are used in spatial analysis when existing boundaries are unavailable, unsuitable, or when evenly sized, uniform areas are required. [Geohashes](https://www.ibm.com/docs/en/streams/4.3.0?topic=334-geohashes), which uniquely identify specific regions according to their latitude and longitude everywhere on Earth, are one type of commonly used grid. 

![Geohashes in Québec City ([source](https://geohash.softeng.co/f2m677))](img/geohash.png)

Grids do not have to be 4-sided. Triangular and hexagonal grids are often used for some studies. Hexagon's are often recommended since they are the regular polygon with the most sides (i.e. can closest represent a circle), that can tesselate without any gaps.

![Screenshot of a map showing density of activity in Glasgow](img/glasgow.png)


### Streets

While streets are often added to maps to provide geographic context, streets can also be their own unit of analysis. For example, traffic flow could be measured on street segments throughout a city. In the image below, streets are coloured by how many parking tickets that they have.

![Parking tickets in Toronto ([source](https://schoolofcities.github.io/parking-tickets-toronto/))](img/toronto-parking-tickets.png)


### Addresses

Some urban data is measured or collected at the address level. For example, address of businesses, non-profits, or community facilities. To map them and compare with other spatial data, addresses are often *[geocoded](https://en.wikipedia.org/wiki/Address_geocoding)*, where their names are converted into geographic coordinates (latitude and longitude). See our [Spatial data and GIS](../spatial-data-and-gis/spatial-data-and-gis.md) tutorial for more.

![Geocoded addresses of businesses in Mississauga from the Canadian Urban Institutes [Measuring Main Streets](https://measuringmainstreets.ca/casestudies/toronto/mississaugadundas/) project](img/addresses-mississauga.png)


## Biases and limitations of spatial data

When collecting and analyzing data, it is important to verify the quality of the dataset. Some data is incomplete or has missing values, which can bias the results, especially if data from certain categories is missing disproportionately. For example, if income data is missing more often for lower-income individuals, the results may overestimate average income and under-represent vulnerable populations.

These are a few important sources of bias or limitations when working with spatial data that are super important to be aware of when working with data linked to places.

- *Self-reporting bias* which is when individuals report inaccurate information about themselves in a survey. This can be intentional (e.g., under-reporting income or over-reporting education) or unintentional (e.g., forgetting details). This can lead to biases in the final dataset and any subsequent analysis.

- *[Ecological fallacy](https://en.wikipedia.org/wiki/Ecological_fallacy)* is the phenomenon of drawing conclusions about individuals based on the group they belong to. For example, one might infer that everyone in a census tract with an overall high median income is wealthy. Although the median income is high, there may be low income residents who live in the tract who are not close to the median.

- *[Edge effects](https://en.wikipedia.org/wiki/Boundary_problem_(spatial_analysis)#Types_and_examples)*  in spatial analysis refer to the limitations or distortions that occur at the boundaries of a study area. They can bias results or reduce accuracy, especially when spatial patterns or processes extend beyond the area being analyzed. For example, let's say you were mapping access to healthy food in a city. Your map may show that one corner of your city does not have a grocery store, leading to a conclusion of it being a food dessert. But if you didn't consider grocery stores just outside the edge or boundary of your city adjacent to this corner, this may not be the case. 

- *[Modifiable areal unit problem](https://en.wikipedia.org/wiki/Modifiable_areal_unit_problem)* (MAUP) is another source of bias when working with spatial data. It is a form of statistical bias that results from the fact that changing the scale or shape of aggregation units leads to different results. [Gerrymandering](https://en.wikipedia.org/wiki/Gerrymandering) is a classic example of intentional MAUP to obtain specific voting outcomes. Check out the graphic below, we can see the results of how different spatial units are arranged would impact the overall results of an election. Overall, it is important to think critically when working with different spatial units to avoid misrepresenting data or cherry-picking results.

![Gerrymandering example](img/gerrymandering.png){width=50%}


