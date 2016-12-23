# Implementation details

## Python scripts

Scripts prefixed with `download`:

* These scripts download Google Sheets then filter the data using Python and save the resultant data as CSV.
* Data that is saved as-is without filtering, is saved into data/sheets/as-is/.
* Filtered data is saved into data/sheets/filtered/.

Scripts prefixed with `filter`:

* These scripts filter data held locally within the data/raw/as-is.
* Filtered data is saved into data/raw/filtered/.

Other scripts:

* Utilities used by the foregoing.

## Data

data/:

* sheets/: data from Google Sheets downloaded by Python scripts
  - as-is/: data downloaded and saved as-is
  - filtered/: data filtered after downloading
* data/static/: data inserted into this directory directly
  - raw/: data downloaded and saved as-is
  - filtered/: data filtered after downloading

---

## Consultancy scripts and data

```
$ python src/download_consultancy_funders_effort.py SHEET
```

* SHEET is the ID of the consultancy Google Sheet
* Download: consultancy projects sheet FunderEffort tab
* Write: data/sheets/as-is/funders_effort.csv
* Rendered by: html/consultancy/projects.html, js/barchart.js, js/pie.js, js/circle_packing

```
$ python src/download_consultancy_funders_projects.py SHEET
```

* SHEET is the ID of the consultancy Google Sheet
* Download: consultancy projects sheet Funding tab
* Write: data/sheets/as-is/funders_projects.csv
* Rendered by: html/consultancy/projects.html, js/barchart.js, js/pie.js, js/circle_packing

```
$ python src/download_consultancy.py SHEET
```

* SHEET is the ID of the consultancy Google Sheet
* Download: consultancy projects sheet Projects tab
* Write: data/sheets/filtered/consultancy.csv
* Write: data/sheets/filtered/project_effort.csv
* Rendered by: html/consultancy/projects.html, js/barchart.js, js/pie.js, js/circle_packing

## Software Carpentry scripts and data

```
$ python src/download_swc.py SHEET
```

* SHEET is the ID of the Software Carpentry Google Sheet
* Download: Software Carpentry sheet Workshops tab
* Write: data/sheets/as-is/swc.csv 
* Write: data/sheets/filtered/swc_attendees.csv
* Rendered by: html/training/swc.html, js/barchart.js, js/pie.js

## Policy scripts and data

```
$ python src/filter_software_survey.py
```

* Read: data/raw/as-is/The use of software in research (Responses) Cleaned For All Hands Hack - Form Responses 1.csv
* Write: data/raw/filtered/software_survey_2014_os.csv
* Write: data/raw/filtered/software_survey_2014_software.csv
* Rendered by: html/policy/survey.html, js/barchart_horiz.js, js/circle_packing.js

## Fellows scripts and data

```
$ python src/filter_fellows.py
```

* Read: data/static/raw/fellows_institutions.csv
* Write: data/static/filtered/fellows_institutions.csv
* Rendered by: html/community/fellows.html, js/circle_packing.js
