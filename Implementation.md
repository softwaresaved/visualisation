# Implementation details

## Consultancy data

```
$ ./get_consultancy_data.sh SHEET_ID
```

where SHEET_ID is the ID of the consultancy GoogleSheet, downloads data/funders_effort.csv and data/funders_project.csv which are rendered by consultancy/charts.html, js/barchart.js, js/pie.js

## Software carpentry data

```
$ ./get_swc_data.sh SHEET_ID
```

where SHEET_ID is the ID of the Software Carpentry GoogleSheet, downloads data/swc.csv and runs filter_swc.sh which runs aggregate_data.py and produces data/swc_filtered.csv which is rendered by js/barchart.js, js/pie.js

## Software survey data

Static data set data/The use of software in research (Responses) Cleaned For All Hands Hack - Form Responses 1.csv can be processed with 

```
$ bash filter_software_survey.sh
```

which runs aggregate_data.py and produces data/SoftwareSurvey2014OS.csv and data/SoftwareSurvey2014Software.csv which is rendered by policy/survey.html, js/barchart_horiz.js, js/circle_packing.js

## Fellows data

Static data set dataCleaning/data/raw_institutions.csv can be processed with

```
$ bash filter_fellows.sh
```

which runs aggregate_data.py and produces data/fellows_institutions.csv which is which is rendered by community/fellows.html, js/circle_packing.js

## Bubble graph visualisations (to be deprecated)

```
$ ./get_consultancy_data.sh SHEET_ID
```

downloads  consultancy_raw.csv and runs transform_consultancy_data.py which produces data/consultancy.csv which is rendered by consultancy/bubble.html and related JavaScript.

```
$ ./get_swc_data.sh SHEET_ID
```

downloads data/swc.csv and runs filter_swc.sh which runs aggregate_data.py and produces data/swc_filtered.csv which is rendered by swc/bubble.html and related JavaScript.
