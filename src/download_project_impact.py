"""Download SSI questionnaire data sheet
AnalysisByQuestion-VisualisationCompliant tab.
"""

# Copyright (c) 2016-2017 The University of Edinburgh

from csv_utils import save_list_as_csv_file, save_csv_file
from sheet_utils import download_sheet

if __name__ == "__main__":
    # SSI questionnaire data
    sheet_id = '1h3IZ6C37pNtIQ_-1duZaQ6kbW788G6s0ARvdOZrOKT8'

    tab_and_range = "AnalysisByQuestion-VisualisationCompliant!A2:L7"
    data = download_sheet(sheet_id, tab_and_range)
    
    file_name = "data/sheets/as-is/project_impact.csv"
    save_list_as_csv_file(data, file_name)
