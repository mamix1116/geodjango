mapboxgl.accessToken = 'pk.eyJ1IjoibWFtaXgxMTE2IiwiYSI6ImNqMTY4eThldTAyY2QzNG82aHU2ZjIxMWcifQ.bZx90CIoa9Kp849JEk8ZBg';

var map = new mapboxgl.Map({
    container: 'map', // container id
    style: 'mapbox://styles/mapbox/streets-v9', // stylesheet location
    center: [139.739143, 35.678707], // starting position [lng, lat]
    zoom: 6 // starting zoom
});

// //WorldBorderの日本
// map.on('load', function () {
//   map.addSource("world-data", {
//     'type' : 'geojson',
//     'data': 'http://127.0.0.1:8000/api/world/89.json'});
//   map.addLayer({
//     'id': 'maine',
//     'type': 'fill',
//     'source': 'world-data',
//     'layout': {},
//     'paint': {
//         'fill-color': '#088',
//         'fill-opacity': 0.8
//     }
//   });
// });

//水難事故データ
map.on('load', function () {
  map.addSource("suinanjiko-data", {
    'type' : 'geojson',
    'data': 'http://127.0.0.1:8000/api/suinanjiko.json',
    'cluster': true,
    'clusterMaxZoom': 10,
    'clusterRadius': 50
  });
  map.addLayer({
    'id': 'clusters',
    'type': 'circle',
    'source': 'suinanjiko-data',
    'paint': {
        "circle-color": [
                "step",
                ["get", "point_count"],
                "#51bbd6",
                100,
                "#f1f075",
                750,
                "#f28cb1"
            ],
        "circle-radius": [
                "step",
                ["get", "point_count"],
                20,
                100,
                30,
                750,
                40
            ]
    },
  });
  map.addLayer({
        id: "cluster-count",
        type: "symbol",
        source: "suinanjiko-data",
        filter: ["has", "point_count"],
        layout: {
            "text-field": "{point_count_abbreviated}",
            "text-font": ["DIN Offc Pro Medium", "Arial Unicode MS Bold"],
            "text-size": 12
        }
  });
  map.addLayer({
        id: "unclustered-point",
        type: "circle",
        source: "suinanjiko-data",
        filter: ["!has", "point_count"],
        paint: {
            "circle-color": "#11b4da",
            "circle-radius": 4,
            "circle-stroke-width": 1,
            "circle-stroke-color": "#fff"
        }
  });
  // Add zoom and rotation controls to the map.
  map.addControl(new mapboxgl.NavigationControl({ position: 'top-left' }));
  // When a click event occurs near a place, open a popup at the location of
  // the feature, with HTML description from its properties
  map.on('click', function(e) {
    var features = map.queryRenderedFeatures(e.point, { layers: ['unclustered-point'] });

    // if the features have no info, return nothing
    if (!features.length) {
      return;
    }

    var feature = features[0];

    // Populate the popup and set its coordinates
    // based on the feature found
    var popup = new mapboxgl.Popup()
    .setLngLat(feature.geometry.coordinates)
    .setHTML('<div id=\'popup\' class=\'popup\' style=\'z-index: 10;\'> <h5> Detail: </h5>' +
    '<ul class=\'list-group\'>' +
    '<li class=\'list-group-item\'> 年月: ' + feature.properties['ym'] + ' </li>' +
    '<li class=\'list-group-item\'> 内容: ' + feature.properties['jiko'] + ' </li>' +
    '<li class=\'list-group-item\'> 河川: ' + feature.properties['river'] + ' </li></ul></div>')
    .addTo(map);
  });

  // Use the same approach as above to indicate that the symbols are clickable
  // by changing the cursor style to 'pointer'
  map.on('mousemove', function(e) {
    var features = map.queryRenderedFeatures(e.point, { layers: ['unclustered-point'] });
    map.getCanvas().style.cursor = features.length ? 'pointer' : '';
  });

});
