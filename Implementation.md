# Implementation details

## Consultancy data

```
$ ./get_consultancy_data.sh SHEET_ID
```

where SHEET_ID is the ID of the consultancy GoogleSheet, downloads consultancy spreadsheet and runs aggregate_data.py to create data/sheets/filtered/project_effort.csv and also downloads data/sheets/as-is/funders_effort.csv and data/sheets/as-is/funders_project.csv which are rendered by consultancy/charts.html, js/barchart.js, js/pie.js, js/circle_packing

## Software carpentry data

```
$ ./get_swc_data.sh SHEET_ID
```

where SHEET_ID is the ID of the Software Carpentry GoogleSheet, downloads data/sheets/as-is/swc.csv and runs filter_swc.sh which runs aggregate_data.py and produces data/sheets/filtered/swc_filtered.csv which is rendered by js/barchart.js, js/pie.js

## Software survey data

Static data set data/raw/as-is/The use of software in research (Responses) Cleaned For All Hands Hack - Form Responses 1.csv can be processed with 

```
$ bash filter_software_survey.sh
```

which runs aggregate_data.py and produces data/raw/filtered/SoftwareSurvey2014OS.csv and data/raw/filtered/SoftwareSurvey2014Software.csv which is rendered by policy/survey.html, js/barchart_horiz.js, js/circle_packing.js

## Fellows data

Static data set dataCleaning/data/raw_institutions.csv can be processed with

```
$ bash filter_fellows.sh
```

which runs aggregate_data.py and produces data/static/filtered/fellows_institutions.csv which is which is rendered by community/fellows.html, js/circle_packing.js

## Bubble graph visualisations (to be deprecated)

```
$ ./get_consultancy_data.sh SHEET_ID
```

downloads  consultancy_raw.csv and runs transform_consultancy_data.py which produces data/sheets/filtered/consultancy.csv which is rendered by consultancy/bubble.html and related JavaScript.

```
$ ./get_swc_data.sh SHEET_ID
```

downloads data/sheets/as-is/swc.csv and runs filter_swc.sh which runs aggregate_data.py and produces data/sheets/filtered/swc_filtered.csv which is rendered by swc/bubble.html and related JavaScript.
