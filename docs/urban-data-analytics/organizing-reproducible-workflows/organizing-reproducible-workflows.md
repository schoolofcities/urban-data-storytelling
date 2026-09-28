---
title: "Organizing reproducible Python workflows"
author: "Aniket Kali"
---

[📥 Click here to download this document and any associated data and images](/downloads/organizing-reproducible-workflows.zip)

This section will cover:

- why it's worth organizing a project before it grows out of hand
- separating raw data from data you've processed yourself
- avoiding repeated, expensive downloads or computations
- keeping settings and file paths easy to find and change
- a short checklist for handing off or revisiting your own work

By now you've written code that loads data, processes it, and produces some kind of output: a cleaned table, a joined dataset, a map. As your notebooks grow past a single, lecture-sized example, a few habits make the difference between a project you (or a collaborator) can pick back up in six months, and one that only makes sense to whichever version of you wrote it yesterday.

None of this is really Python-specific. It's about how you organize files and structure a project, but it becomes especially important once you're working with real, messy urban data: files downloaded from open data portals, addresses you've geocoded yourself, or live queries to services like OpenStreetMap's Overpass API (see [OpenStreetMap](../openstreetmap/openstreetmap.md)).

## Keep raw and processed data separate

A simple, effective habit is to give raw data and processed data their own folders, and to never edit the raw folder by hand.

```text
project/
├── data/
│   ├── raw/          # exactly what you downloaded or queried, never edited by hand
│   └── processed/    # cleaned or joined versions that your own code produces
├── output/           # maps, charts, and summary tables you're ready to share
└── analysis.ipynb
```

If your raw data stays untouched, you can always regenerate anything downstream just by re-running your code, and you'll never lose track of what's "the real data" versus "something I already modified." The geocoding example in [Spatial data processing](../spatial-data-processing/spatial-data-processing.ipynb) and the `osmnx` queries in [OpenStreetMap](../openstreetmap/openstreetmap.md) both follow this same pattern: query or geocode once, save the result, and load that saved file everywhere else.

## Don't repeat expensive work

Some operations are slow, rate-limited, or depend on an external service, like geocoding hundreds of addresses (as in [Spatial data processing](../spatial-data-processing/spatial-data-processing.ipynb)), or querying OpenStreetMap's Overpass API. Re-running these every time you restart your notebook wastes your own time, and puts unnecessary load on services that plenty of other people also rely on.

The general pattern: do the expensive thing once, save the result to a file, and load that file everywhere else.

```python
import os
import geopandas as gpd

if os.path.exists("data/raw/geocoded_addresses.gpkg"):
    gdf = gpd.read_file("data/raw/geocoded_addresses.gpkg")
else:
    gdf = gpd.tools.geocode(addresses, provider="nominatim", user_agent="my-project")
    gdf.to_file("data/raw/geocoded_addresses.gpkg", driver="GPKG")
```

The first time this cell runs, it does the slow geocoding work and saves the result. Every time after that, it just reads the file instantly, without needing an internet connection at all.

## Put your settings where you can find them

As a notebook grows, small hardcoded values (a place name, a file path, a buffer distance) end up scattered across dozens of cells, which makes them easy to miss when you need to change one later. A useful convention is to define these as constants near the top of your notebook, written in `ALL_CAPS` to signal "this is a setting, not a regular variable."

```python
PLACE = "Toronto, Ontario, Canada"
TAGS = {"amenity": "library"}
CRS = "EPSG:32617"

RAW_DATA_PATH = "data/raw/toronto_libraries_osm.gpkg"
PROCESSED_DATA_PATH = "data/processed/toronto_libraries_clean.gpkg"
```

Everything below can then refer to these names instead of repeating the same string or number in five different cells. If you want to re-run the whole analysis for a different city, you change one line instead of hunting through the whole notebook.

## Use relative file paths

Recall from [Programming with Python and computational notebooks](../intro-to-python-and-jupyter/intro-to-python-and-jupyter.ipynb) that a file path describes where a file lives on your computer. Prefer paths that are *relative* to your project folder, like `"data/raw/file.gpkg"`, over *absolute* ones like `"/Users/yourname/Desktop/project/data/raw/file.gpkg"`. A relative path works no matter whose computer the project is opened on (including your own, a year from now, on a different laptop), as long as the folder structure around the notebook stays the same.

## Restart and run everything, in order, before you're done

[Programming with Python and computational notebooks](../intro-to-python-and-jupyter/intro-to-python-and-jupyter.ipynb) pointed out that a notebook runs in the order you *execute* its cells, not necessarily the order they appear on the page. A notebook that "works" only because of cells you ran in a particular order, and have since edited, deleted, or forgotten about, isn't actually reproducible. The only real test is what happens when you restart the kernel and run every cell, top to bottom, from a clean slate.

Get in the habit of doing this ("Restart Kernel and Run All") before sharing a notebook, or before considering an analysis finished.

## A short checklist

Before calling an analysis done, it's worth running through a short checklist:

- Imports are all together, near the top of the notebook
- Settings (place names, file paths, thresholds) are defined once, near the top, not scattered throughout
- File paths are relative to the project folder, not specific to your computer
- Raw data lives in its own folder and is never edited directly
- Anything slow or rate-limited (an API query, a geocoding job) is saved to a file rather than re-run every time
- The notebook runs cleanly from a restarted kernel, top to bottom, without errors
- Markdown cells briefly explain any non-obvious decisions, so a reader, including future you, understands *why*, not just *what*

None of these habits are unique to Python or to spatial data. They're the same practices that make any project easier to trust, share, and pick back up later.
