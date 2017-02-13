"""Download SSI Consultancy Projects sheet tabs.

* Chart-FunderEffort
* Chart-Funding
* Chart-InstitutionEffort
* Chart-InstitutionProjects
* Chart-Effort
"""

# Copyright (c) 2016-2017 The University of Edinburgh

from csv_utils import save_list_as_csv_file
from sheet_utils import download_sheet

if __name__ == "__main__":
    # SSI Consultancy Projects
    sheet_id = '1Jmq6ongECyJih7HbroltnAGZOecWOsl1qFdemw8Hj8A'

    tabs_files = [
        ["Chart-FunderEffort", "funders_effort.csv"],
        ["Chart-Funding", "funders_projects.csv"],
        ["Chart-InstitutionEffort!A3:B22",
         "institution_effort.csv"],
        ["Chart-InstitutionProjects!A3:B28",
         "institution_projects.csv"],
        ["Chart-Effort!A3:B58",
         "projects_effort.csv"]]

    for [tab_and_range, file_name] in tabs_files:
        data = download_sheet(sheet_id, tab_and_range)
        save_list_as_csv_file(data, "data/sheets/as-is/" + file_name)
