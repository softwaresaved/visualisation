"""Download SSI Consultancy Projects sheet tabs.

* Chart-FunderEffort
* Chart-Funding
* Chart-InstitutionEffort
* Chart-InstitutionProjects
* Chart-Effort
"""

# Copyright (c) 2016-2017 The University of Edinburgh

from csv_utils import save_list_as_csv_file, save_csv_file
from sheet_utils import download_sheet

if __name__ == "__main__":
    # SSI Consultancy Projects
    sheet_id = '1h3IZ6C37pNtIQ_-1duZaQ6kbW788G6s0ARvdOZrOKT8'

    tab_and_range = "AnalysisByQuestion!C5:N16"
    data = download_sheet(sheet_id, tab_and_range)
    
    del data[1:7]
    for d in data:
        print (d)
    

    file_name = "data/sheets/as-is/project_impact.csv"
    save_list_as_csv_file(data, file_name)

    
