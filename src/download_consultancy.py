"""Download SSI Consultancy Projects sheet tabs.

* Chart-FunderEffort
* Chart-Funding
* Chart-InstitutionEffort
* Chart-InstitutionProjects
* Chart-Effort
"""

# Copyright (c) 2016 The University of Edinburgh

import os
import sys

from csv_utils import tail
from web_utils import download_google_sheet

if __name__ == "__main__":
    sheet = sys.argv[1]

    tab = 1949517833 # Chart-FunderEffort
    file_name = "data/sheets/as-is/funders_effort.csv"
    download_google_sheet(file_name, sheet, tab)

    tab = 7 # Chart-Funding tab
    file_name = "data/sheets/as-is/funders_projects.csv"
    download_google_sheet(file_name, sheet, tab)

    tab = 9 # Chart-InstitutionEffort
    file_name = "tmp.csv"
    download_google_sheet(file_name, sheet, tab)
    # Trim notes lines
    trimmed_file_name = "data/sheets/filtered/institution_effort.csv"
    tail(file_name, trimmed_file_name, 2)

    tab = 8 # Chart-InstitutionProjects
    download_google_sheet(file_name, sheet, tab)
    # Trim notes lines
    trimmed_file_name = "data/sheets/filtered/institution_projects.csv"
    tail(file_name, trimmed_file_name, 2)

    tab = 1 # Chart-Effort
    download_google_sheet(file_name, sheet, tab)
    # Trim notes lines
    trimmed_file_name = "data/sheets/filtered/projects_effort.csv"
    tail(file_name, trimmed_file_name, 2)
    os.remove(file_name)
