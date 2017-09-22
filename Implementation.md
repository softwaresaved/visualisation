# Implementation details

## Python scripts

Scripts prefixed with `download`:

* These scripts download Google Sheets, using OAuth2 for authentication, then filter the data using Python and save the resultant data as CSV.
* For more on the Google Sheets and OAuth2 APIs used, see:
  - [Introduction to the Google Sheets API](https://developers.google.com/sheets/api/guides/concepts)
  - Google Sheets API v4 [Python Quickstart](https://developers.google.com/sheets/api/quickstart/python)
* Data that is saved as-is without filtering, is saved into data/sheets/as-is/.
* Filtered data is saved into data/sheets/filtered/.

Other scripts:

* Utilities used by the foregoing.

## Data

data/:

* sheets/: data from Google Sheets downloaded by Python scripts
  - as-is/: data downloaded and saved as-is
  - filtered/: data filtered after downloading
* data/static/: data stored as-is

---

## Consultancy scripts and data

```
$ python src/download_consultancy.py
```

* Download SSI Consultancy Projects sheet, tabs:
  - Chart-FunderEffort
  - Chart-Funding
* Write:
  - data/sheets/as-is/funders_effort.csv
  - data/sheets/as-is/funders_projects.csv
* Rendered by: html/consultancy/funders.html, js/barchart.js, js/pie.js
* Download SSI Consultancy Projects sheet:
  - Chart-InstitutionEffort
  - Chart-InstitutionProjects
* Write:
  - data/sheets/as-is/institution_effort.csv
  - data/sheets/as-is/institution_projects.csv
* Rendered by: html/consultancy/institutions.html, js/barchart.js, js/pie.js
* Download SSI Consultancy Projects sheet, tabs:
  - Chart-Effort
* Write: data/sheets/as-is/projects_effort.csv
* Rendered by: html/consultancy/projects.html, js/circle_packing

```
$ python src/download_impact.py
```

* Download Questionnaire Analysis sheet, AnalysisByQuestion tab, C5:N16.
* Write: data/sheets/as-is/project_impact.csv 
* Rendered by: html/impact/impact.html, JavaScript within HTML, js/d3.min.js.

## Software Carpentry scripts and data

```
$ python src/download_swc.py
```

* Download: SSI SWC from 2012-04-30 to 2014-04-09 from Mike sheet, Workshops-Summary tab
* Write: data/sheets/as-is/swc.csv 
* Rendered by: html/training/swc.html, js/barchart.js, js/pie.js

## Policy scripts and data

```
$ python src/download_policy.py
```

* Download: Software Used In Research Combined Results sheet, Unique names for publication tab
* Write: data/sheets/as-is/software.csv 
* Rendered by: html/policy/software.html, js/barchart_horiz.js, js/circle_packing.js

Local data:

* data/static/software_survey_2014_os.csv
* data/static/software_survey_2014_software.csv
* Rendered by: html/policy/survey.html, js/barchart_horiz.js, js/circle_packing.js

## Fellows scripts and data

Local data:

* data/static/fellows_institutions.csv
* Rendered by: html/community/fellows.html, js/circle_packing.js
