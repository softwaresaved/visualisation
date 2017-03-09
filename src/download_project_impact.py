"""Download Project Impact Data.

* Downloads project impact data generated from project questionnaire data
* The code grabs a block of data containing the data headers and categories,
* but also some information that we don't want in the spreadsheet for visualisation.
* So, the offending lines are removed before the data is written out.
"""

# Copyright (c) 2016-2017 The University of Edinburgh

from csv_utils import save_list_as_csv_file, save_csv_file
from sheet_utils import download_sheet

if __name__ == "__main__":
    # SSI questionnaire data
    sheet_id = '1h3IZ6C37pNtIQ_-1duZaQ6kbW788G6s0ARvdOZrOKT8'

    # grab block of data that we are after
    tab_and_range = "AnalysisByQuestion!C5:N16"
    data = download_sheet(sheet_id, tab_and_range)
    
    # remove the offending lines we dont want for our analysis
    del data[1:7]
    
    # write out the data
    file_name = "data/sheets/as-is/project_impact.csv"
    save_list_as_csv_file(data, file_name)

    
