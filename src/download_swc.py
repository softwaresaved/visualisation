"""Download Software Carpentry sheet Workshops-Summary tab.
"""

# Copyright (c) 2016-2017 The University of Edinburgh

from csv_utils import load_csv_file
from csv_utils import save_dict_as_csv_file
from csv_utils import save_list_as_csv_file
from csv_utils import sum_unique_values
from sheet_utils import download_sheet

if __name__ == "__main__":
    # Software Carpentry
    sheet_id = '1xna48IRFl-lLJrPhlI7vC-1TWnl1kICxzEfrvpIKLp8'
    tab_and_range = "Workshops-Summary"
    data = download_sheet(sheet_id, tab_and_range)
    file_name = "data/sheets/as-is/swc.csv"
    save_list_as_csv_file(data, file_name)
