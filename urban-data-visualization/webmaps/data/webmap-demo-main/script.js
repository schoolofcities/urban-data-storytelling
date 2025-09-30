const map = new maplibregl.Map({
    container: 'map', // container id
    style: 'https://basemaps.cartocdn.com/gl/positron-gl-style/style.json', // style URL
    center: [-105, 58], // starting position [lng, lat]
    zoom: 3 // starting zoom
});

map.addControl(new maplibregl.NavigationControl());

map.on('load', () => {
 
    map.addSource('canada-provterr', {
        type: 'geojson',
        data: 'https://raw.githubusercontent.com/smith-lg/webmap-demo/refs/heads/main/data/can-provterr.geojson', //Link to raw github files when in development stage. Update to pages on deployment
        'generateId': true //Create a unique ID for each feature
    });
 
    map.addLayer({
        'id': 'provterr-fill',
        'type': 'fill',
        'source': 'canada-provterr',
        'paint': {
            'fill-color': [
                'step', // STEP expression produces stepped results based on value pairs
                ['get', 'POP2021'], // GET expression retrieves property value from 'population' data field
                '#fd8d3c', // Colour assigned to any values < first step
                100000, '#fc4e2a', // Colours assigned to values >= each step
                500000, '#e31a1c',
                1000000, '#bd0026',
                5000000, '#800026'
            ],
            'fill-opacity': [
                'case',
                ['boolean', ['feature-state', 'hover'], false],
                1,
                0.5
            ], //CASE and FEATURE STATE expression sets opactity as 0.5 when hover state is false and 1 when updated to true,
            'fill-outline-color': 'white'
        },
    });
 
});


// Simple click event
map.on('click', 'provterr-fill', (e) => {
    //console.log(e);   //e is the event info triggered and is passed to the function as a parameter (e)
    let provname = e.features[0].properties.PRENAME;
    console.log(provname);
});

// Add pop up event
map.on('click', 'provterr-fill', (e) => {
    new maplibregl.Popup() // Declare new popup object on each click
        .setLngLat(e.lngLat) // Use method to set coordinates of popup based on mouse click location
        .setHTML("Province/Territory: " + e.features[0].properties.PRENAME + " " + "Population: " + e.features[0].properties.POP2021) // Use click event properties to write text for popup
        .addTo(map); // Show popup on map
    });

// Update cursor
map.on('mouseenter', 'provterr-fill', () => {
    map.getCanvas().style.cursor = 'pointer'; //Switch cursor to pointer when mouse is over provterr-fill layer
});

map.on('mouseleave', 'provterr-fill', () => {
    map.getCanvas().style.cursor = ''; //Switch cursor back when mouse leaves provterr-fill layer
});

/*--------------------------------------------------------------------
HOVER EVENT USING setFeatureState() METHOD
// --------------------------------------------------------------------*/
let provID = null; //Declare initial province ID as null

map.on('mousemove', 'provterr-fill', (e) => {
    if (e.features.length > 0) { //If there are features in array enter conditional

        if (provID !== null) { //If provID IS NOT NULL set hover feature state back to false to remove opacity from previous highlighted polygon
            map.setFeatureState(
                { source: 'canada-provterr', id: provID },
                { hover: false }
            );
        }

        provID = e.features[0].id; //Update provID to featureID
        map.setFeatureState(
            { source: 'canada-provterr', id: provID },
            { hover: true } //Update hover feature state to TRUE to change opacity of layer to 1
        );
    }
});


map.on('mouseleave', 'provterr-fill', () => { //If mouse leaves the geojson layer, set all hover states to false and provID variable back to null
    if (provID !== null) {
        map.setFeatureState(
            { source: 'canada-provterr', id: provID },
            { hover: false }
        );
    }
    provID = null;
});


// Filter data layer to show selected Province from dropdown selection
let boundaryvalue;

document.getElementById("boundaryfieldset").addEventListener('change',(e) => {   
    boundaryvalue = document.getElementById('boundary').value;

    console.log(boundaryvalue); // Useful for testing whether correct values are returned from dropdown selection

    if (boundaryvalue == 'All') {
        map.setFilter(
            'provterr-fill',
            ['has', 'PRENAME'] // Returns all polygons from layer that have a value in PRENAME field
        );
    } else {
        map.setFilter(
            'provterr-fill',
            ['==', ['get', 'PRENAME'], boundaryvalue] // returns polygon with PRENAME value that matches dropdown selection
        );
    }

});

// Change map layer display based on check box using setLayoutProperty method
document.getElementById('layercheck').addEventListener('change', (e) => {
    map.setLayoutProperty(
        'provterr-fill',
        'visibility',
        e.target.checked ? 'visible' : 'none'
    );
});
