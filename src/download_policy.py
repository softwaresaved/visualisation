"""Download Software Used In Research Combined Results sheet
Unique names for publication tab and save as-is.
"""

# Copyright (c) 2016-2017 The University of Edinburgh

from csv_utils import save_list_as_csv_file
from sheet_utils import download_sheet

if __name__ == "__main__":
    # Software Used In Research Combined Results
    sheet_id = '15HBoRuJ0OcDDRspBGA0mH_71gaX1EdlWuXHTw4IybTY'
    tab_and_range = "Unique names for publication"
    data = download_sheet(sheet_id, tab_and_range)
    file_name = "data/sheets/as-is/software.csv"
    save_list_as_csv_file(data, file_name)
