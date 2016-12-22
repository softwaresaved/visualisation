# Implementation details

## Consultancy data

```
$ python src/download_consultancy_funders_effort.py SHEET
```

* SHEET is the ID of the consultancy Google Sheet
* Download: consultancy projects sheet.FunderEffort tab
* Write: data/sheets/as-is/funders_effort.csv
* Rendered by: consultancy/projects.html, js/barchart.js, js/pie.js, js/circle_packing

```
$ python src/download_consultancy_funders_projects.py SHEET
```

* SHEET is the ID of the consultancy Google Sheet
* Download: consultancy projects sheet.Funding tab
* Write: data/sheets/as-is/funders_project.csv
* Rendered by: consultancy/projects.html, js/barchart.js, js/pie.js, js/circle_packing

```
$ python src/download_consultancy.py SHEET
```

* SHEET is the ID of the consultancy Google Sheet
* Download: consultancy projects sheet.default tab
* Write: data/sheets/filtered/consultancy.csv
* Write: data/sheets/filtered/project_effort.csv
* Rendered by: consultancy/projects.html, js/barchart.js, js/pie.js, js/circle_packing

## Software carpentry data

```
$ python src/download_swc.py SHEET
```

* SHEET is the ID of the Software Carpentry GoogleSheet
* Download: data/sheets/as-is/swc.csv 
* Write: data/sheets/filtered/swc_filtered.csv
* Rendered by: training/swc.html, js/barchart.js, js/pie.js

## Software survey data

```
$ python src/filter_software_survey.py
```

* Read: Static data set data/raw/as-is/The use of software in research (Responses) Cleaned For All Hands Hack - Form Responses 1.csv
* Write: data/raw/filtered/SoftwareSurvey2014OS.csv
* Write: data/raw/filtered/SoftwareSurvey2014Software.csv
* Rendered by: policy/survey.html, js/barchart_horiz.js, js/circle_packing.js

## Fellows data

```
$ python src/filter_fellows.py
```

* Read: Static data set dataCleaning/data/raw_institutions.csv
* Write: data/static/filtered/fellows_institutions.csv
* Rendered by: community/fellows.html, js/circle_packing.js

## Bubble graph visualisations (to be deprecated)

consultancy/bubble.html and related JavaScript render data/sheets/filtered/consultancy.csv.

training/bubble.html and related JavaScript render data/sheets/filtered/swc_filtered.csv.
