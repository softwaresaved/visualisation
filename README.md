# usage-visualisation

Web-based visualisation of usage data from HPC facilities. Initially based around ARCHER (http://www.archer.ac.uk)

Updates by mikej888 to visualise [The Software Sustainability Institute](http://www.software.ac.uk) data.

## Usage

After cloning this repository:

* Export SSI Consultancy Projects Google spreadsheet.
* Chop out all columns except:
  - Project Name 
  - Funder(s)
  - Institution
  - Type
  - Research Field
  - PMs
* Rename Funder(s) to Funder
* Rename PMs to Effort
* Save as comma-separated values file SSIConsultancyProjects.csv 
* Move file to prototypes/codes-force-bubbles/data/

## TODO

* In ARCHER code, bubble size is derived from number of users. For SSI, derive bubble size from actual effort.
* Add handler for projects that have multiple funders or institutions.
* Add SSI open call project meta-data to balloons that pop up when mouse hovers over bubble.
* Add links from pop-up meta-data to open call web pages on SSI web site. Requires adding this information to the CSV file.
* Make code generic so can be used for both ARCHER and SSI - configure titles, button names, columns queried, meta-data, which column(s) are used to calculate bubble sizes etc.
