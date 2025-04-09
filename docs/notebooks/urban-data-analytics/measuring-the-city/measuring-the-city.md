# Measuring the city: metrics and indicators

In this module, we will explore how to measure urban phenomena using data, specifically focusing on:

- Common spatial units and measures of aggregation
- Common metrics and indicators used in urban analysis
- Limitations & potential errors in data collection

## Common spatial units and measures of aggregation

When analyzing geospatial data, it is often necessary to select a *spatial unit* or *unit of aggregation* to define the boundaries of the areas you are representing. Below are some units of aggregation that are often used in urban analysis:

### Census

Boundaries for spatial census data are either defined by federal or provincial/territorial governments or "according to a set of rules based on geographic attributes and one or more characteristics of the resident population" ([Statistics Canada](https://www12.statcan.gc.ca/census-recensement/2021/geo/sip-pis/boundary-limites/index2021-eng.cfm?year=21)). See [Canadian census data](../canadian-census-data/canadian-census-data.md) for more information.

![Common census boundaries in Toronto](img/census-boundaries-legend-eg.png){width=70%}

### Political

Political boundaries delineate areas that are governed by different authorities, like countries or states. Canadian federal electoral districts, or ridings, are geographic constituencies that are each represented by a Member of Parliament. There are also provincial and territorial electoral districts, which are smaller.

![Canadian electoral districts ([source](https://www.google.com/url?sa=i&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FElectoral_district_%2528Canada%2529&psig=AOvVaw0y9xqp_su-jxB3RT35MGD1&ust=1743958206809000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCJCo3dyswYwDFQAAAAAdAAAAABAE))](img/canada_electoral_districts.png){width=70%}

### Grids

A grid is "a network of evenly spaced horizontal and vertical lines used to identify locations on a map" ([source](https://pro.arcgis.com/en/pro-app/latest/help/layouts/grids-and-graticules.htm)). Grids are used in spatial analysis when existing boundaries are unavailable, unsuitable, or when evenly sized, uniform areas are required. [Geohashes](https://www.ibm.com/docs/en/streams/4.3.0?topic=334-geohashes) -- which uniquely identify specific regions according to their latitude and longitude everywhere on Earth -- are one type of commonly used grid.

![Geohashes in Québec City ([source](https://geohash.softeng.co/f2m677))](img/geohash.png){width=70%}

### Streets

While streets are often added to maps to provide geographic context, streets can also be their own unit of analysis. For example, traffic flow could be measured on street segments throughout a city. In the image below, streets are categorized by how friendly they are to pedestrians and other forms of traffic.

![Street types ([source](https://www.researchgate.net/figure/The-street-function-analysis-based-on-street-profiles_fig1_334670964))](img/streets.png){width=90%}

### Addresses

Some urban data is measured at the address level. Addresses are often *[geocoded](https://en.wikipedia.org/wiki/Address_geocoding)*, which means they are converted into geographic coordinates (latitude and longitude) so they can be mapped. See [Spatial data and GIS](../spatial-data-and-gis/spatial-data-and-gis.md) and [Spatial data in Python](../6-spatial-data-and-python/spatial-data-and-python.ipynb) **<-- FIX THIS LINK!** for more information about geocoding.

![Geocoded addresses ([source](https://desktop.arcgis.com/en/arcmap/latest/manage-data/geocoding/geocoding-a-table-of-addresses-about.htm))](img/geocoding.png)

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

## Limitations & potential errors in data collection

When collecting and analyzing data, it is important to verify the quality of the dataset. Some data is incomplete or has missing values, which can bias the results, especially if data from certain categories is missing disproportionately. For example, if income data is missing more often for lower-income individuals, the results may overestimate average income and underrepresent vulnerable populations.

*Self report bias* is another form of bias that occurs particularly in survey data like the census, when individuals report inaccurate information about themselves. This can be intentional (e.g., underreporting income or overreporting education) or unintentional (e.g., forgetting details).

The *[Modifiable Areal Unit Problem](https://en.wikipedia.org/wiki/Modifiable_areal_unit_problem)* (MAUP) is another source of bias when working with spatial data. It is a form of statistical bias that results from the fact that changing the scale or shape of aggregation units leads to different results. This issue often arises when creating choropleth maps, which use different colors to represent different values, like the ones below. It is important to think critically when choosing units of spatial aggregation to avoid misrepresenting data or cherry-picking results.

![Modifiable Areal Unit Problem ([source](https://www.metrans.org/news/the-modifiable-areal-unit-problem-an-overview))](img/maup.png){width=80%}

*[Ecological fallacy](https://en.wikipedia.org/wiki/Ecological_fallacy)* is the phenomenon of drawing conclusions about individuals based on the group they belong to. For example, one might infer that everyone in a census tract with an overall high median income is wealthy. Although the median income is high, there may be low income people who live in the tract who are not being captured by this measure of central tendency.

Another statistical bias to be aware of results from *changes in geographic boundaries over time*. Census boundaries, for example, can change on a yearly basis. Doing a longitudinal analysis of spatial census data requires using a technique like areal weighting, in which data are redistributed based on the amount they overlap.