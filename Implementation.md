# Implementation details

## Consultancy data

```
$ bash get_consultancy_effort.sh SHEET
```

where SHEET is the ID of the consultancy GoogleSheet and downloads data/sheets/as-is/funders_effort.csv which is rendered by consultancy/projects.html, js/barchart.js, js/pie.js, js/circle_packing

```
$ bash get_consultancy_projects.sh SHEET
```

where SHEET is the ID of the consultancy GoogleSheet and downloads data/sheets/as-is/funders_project.csv which is rendered by consultancy/projects.html, js/barchart.js, js/pie.js, js/circle_packing

```
$ bash get_consultancy_data.sh SHEET
```

where SHEET is the ID of the consultancy GoogleSheet, downloads consultancy spreadsheet, slices top 4 redundant rows off, runs transform_consultancy_data.py to create data/sheets/filtered/consultancy.csv, then runs src/get_sums.py to create data/sheets/filtered/project_effort.csv which is rendered by consultancy/projects.html, js/barchart.js, js/pie.js, js/circle_packing

## Software carpentry data

```
$ bash get_swc_data.sh SHEET
```

where SHEET is the ID of the Software Carpentry GoogleSheet, downloads data/sheets/as-is/swc.csv and runs filter_swc.sh which runs src/get_sums.py and produces data/sheets/filtered/swc_filtered.csv which is rendered by training/swc.html, js/barchart.js, js/pie.js

## Software survey data

Static data set data/raw/as-is/The use of software in research (Responses) Cleaned For All Hands Hack - Form Responses 1.csv can be processed with 

```
$ bash filter_software_survey.sh
```

which runs src/get_counts.py and produces data/raw/filtered/SoftwareSurvey2014OS.csv and data/raw/filtered/SoftwareSurvey2014Software.csv which is rendered by policy/survey.html, js/barchart_horiz.js, js/circle_packing.js

## Fellows data

Static data set dataCleaning/data/raw_institutions.csv can be processed with

```
$ bash filter_fellows.sh
```

which runs src/get_counts.py and produces data/static/filtered/fellows_institutions.csv which is which is rendered by community/fellows.html, js/circle_packing.js

## Bubble graph visualisations (to be deprecated)

```
$ bash get_consultancy_data.sh SHEET
```

where SHEET is the ID of the consultancy GoogleSheet, downloads consultancy spreadsheet, slices top 4 redundant rows off, runs transform_consultancy_data.py to create data/sheets/filtered/consultancy.csv which is rendered by consultancy/bubble.html and related JavaScript.

```
$ bash get_swc_data.sh SHEET
```

downloads data/sheets/as-is/swc.csv and runs filter_swc.sh which runs src/get_sums.py and produces data/sheets/filtered/swc_filtered.csv which is rendered by training/bubble.html and related JavaScript.
