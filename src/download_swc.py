"""Download Software Carpentry sheet Workshops tab and filter to sum
number of attendees by institution.
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
    tab_and_range = "Workshops"
    data = download_sheet(sheet_id, tab_and_range)
    file_name = "data/sheets/as-is/swc.csv"
    save_list_as_csv_file(data, file_name)

    _, data = load_csv_file(file_name)
    swc_data = sum_unique_values(data, "Institution", "Attendees")
    save_dict_as_csv_file("data/sheets/filtered/swc_attendees.csv",
                          "Institution",
                          "Attendees",
                          swc_data)
