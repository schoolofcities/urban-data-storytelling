# Reference: OpenStreetMap, OSMnx, and Overpass

## OpenStreetMap

OpenStreetMap is a collaborative geographic database of physical features.

Useful links:

- [OpenStreetMap](https://www.openstreetmap.org/)
- [OpenStreetMap map features](https://wiki.openstreetmap.org/wiki/Map_features)
- [OSMnx documentation](https://osmnx.readthedocs.io/en/stable/)

## Inspect a real feature

- [Search OpenStreetMap for Toronto Reference Library](https://www.openstreetmap.org/search?query=Toronto%20Reference%20Library)

Inspect the selected feature's tags and geometry.

## Overpass Turbo

- [Overpass Turbo](https://overpass-turbo.eu/)
- [Overpass API examples](https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_API_by_Example)

Overpass Turbo lets you run Overpass queries and inspect the resulting features interactively on a map. The Wizard is often the easiest starting point.

Try these Wizard searches:

```text
amenity=library
amenity=school
leisure=park
amenity=bicycle_parking
railway=station
shop=supermarket
```

A simple query often resembles:

```text
[out:json][timeout:25];

nwr["amenity"="library"]({{bbox}});

out geom;
```

You do not need to memorize Overpass Query Language. Focus on understanding the search area, tag filter, and returned data.

## OSMnx

Typical feature query:

```python
import osmnx as ox

features = ox.features_from_place(
    "Toronto, Ontario, Canada",
    tags={"amenity": "library"}
)
```

Other examples:

```python
{"amenity": "school"}
{"leisure": "park"}
{"amenity": "bicycle_parking"}
{"railway": "station"}
{"shop": "supermarket"}
```

Several values for one key:

```python
{
    "amenity": ["library", "school"]
}
```

## Good practice

1. Start with a focused query.
2. Inspect the output.
3. Save successful downloads locally.
4. Do not repeatedly query the service unnecessarily.
5. Keep raw and processed data separate.
6. Verify that returned OSM features represent what you intended to measure.
7. Attribute OpenStreetMap contributors when publishing OSM-derived work.
