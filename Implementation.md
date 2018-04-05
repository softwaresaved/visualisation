# Implementation details

## Python scripts

`src/download_sheets.py`:

* This script downloads Google Sheets, using OAuth2 for authentication, then saves the resultant data as CSV files.
* The sheets, tabs and cells to download, and the files to save the data in, are specified via a YAML file (see `sheets.yml`).
* For more on the Google Sheets and OAuth2 APIs used, see:
  - [Introduction to the Google Sheets API](https://developers.google.com/sheets/api/guides/concepts)
  - Google Sheets API v4 [Python Quickstart](https://developers.google.com/sheets/api/quickstart/python)
* Data is saved into files under data/sheets/as-is/.

Other scripts are utilities used by the above.

## Data

data/:

* sheets/: data from Google Sheets downloaded by Python scripts
  - as-is/: data downloaded and saved as-is
  - filtered/: data filtered after downloading
* data/static/: data stored as-is

## Visualisation

Data files visualised by HTML pages.

### Consultancy data

html/consultancy/funders.html:

* data/sheets/as-is/funders_effort.csv
* data/sheets/as-is/funders_projects.csv

html/consultancy/institutions.html:

* data/sheets/as-is/institution_effort.csv
* data/sheets/as-is/institution_projects.csv

html/consultancy/projects.html:

* data/sheets/as-is/projects_effort.csv

html/impact/impact.html:

* data/sheets/as-is/project_impact.csv 
* data/sheets/as-is/project_impact.csv 

### Software Carpentry data

html/training/swc.html:

* data/sheets/as-is/swc.csv 

html/training/swc_workshops_2017.html:

* data/sheets/as-is/swc_workshops_affiliation_gb_2017.csv 

html/training/swc_instructors_2017.html:

* data/sheets/as-is/swc_instructors_affiliation_gb_2017.csv 

### Policy data

html/policy/software.html:

* data/sheets/as-is/software.csv 

html/policy/survey.html:

* data/static/software_survey_2014_os.csv
* data/static/software_survey_2014_software.csv

### Fellows data

html/community/fellows.html:

* data/static/fellows_institutions.csv
