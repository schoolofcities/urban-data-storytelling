# Week 4 Data Notes

## `data/raw/toronto_census_areas.geojson`

This is the Toronto census geography supplied for the course.

Checks performed while preparing the Week 4 package:

- 279 geographic records
- CRS: EPSG:4326
- geometry: 268 Polygon features and 11 MultiPolygon features
- contains `ADAUID`, population, income, housing, education, mobility, and related census variables

The file is copied into the package unchanged.

## `data/practice/toronto_library_points_practice.geojson`

This is a **practice fallback**, not an OpenStreetMap extract.

It was prepared from the Toronto Public Library point GeoPackage supplied with the course materials. It contains 112 library point records in EPSG:4326 with library name and address.

Its purpose is to allow learners to continue with GeoPandas, spatial joins, counts, and maps if a live OSMnx/Overpass request is unavailable during class.

## Live OpenStreetMap data

The primary lecture and assignment workflow downloads OpenStreetMap data live using OSMnx.

When the query succeeds, the notebook saves the returned GeoDataFrame to:

`data/raw/toronto_osm_libraries.gpkg`

This file is intentionally not pre-populated with fabricated or stale OSM records.


## `data/backup/`

This folder contains protected copies of successful Week 4 outputs:

- `toronto_osm_libraries_live_backup.gpkg` — successful live OSMnx query for `amenity=library`
- `toronto_libraries_clean_backup.gpkg` — cleaned version of that query
- `census_library_analysis_backup.gpkg` — completed census-area analysis

These files are kept separately from `data/raw/` and `data/processed/` so learners can safely rerun or overwrite working files without losing the classroom fallback.
