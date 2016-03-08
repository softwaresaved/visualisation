# D3 demos

This is a collection of demos to help anyone who is new to D3
or geo visualisations and need to create visualisations for the Software Sustainable Institute.

## Acknoledgements

The demos provide here are based on https://bost.ocks.org/mike/map/.

## How to view

1.   Install Node.

2.   Run

     ~~~
     $ sudo npm install topojson leaflet d3
     ~~~

3.   Run

     ~~~
     $ python3 -m http.server
     ~~~

## Demos

1. [uk.html](uk.html)

   Map of UK.

2. [uk-high.html](uk-high.html)

   Map of UK in high resolution.


## How to add new maps

1.   Install Geospatial Data Abstraction Library.

     For Linux:

     ~~~
     $ sudo apt-get install gdal-bin
     ~~~

     For OS X:

     ~~~
     $ sudo brew install gdal
     ~~~

2.   Download the shape file that you need.
     You can find good shape files that are free to use at
     http://www.naturalearthdata.com/downloads/.

3.   Unzip the file that you downloaded. You will end up with a `.shp` file.

4.   Filter the file to just have the information that you want.
     For example, to a map with UK and Ireland you can use

     ~~~
     $ ogr2ogr -f GeoJSON -where "iso_a3 IN ('GBR', 'IRL')" output-file.json input-file.shp
     ~~~
