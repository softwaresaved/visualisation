"""Download Software Carpentry sheet Workshops tab and filter to sum
number of attendees by institution.
"""

# Copyright (c) 2016 The University of Edinburgh

import sys

from csv_utils import load_csv_file
from csv_utils import save_dict_as_csv_file
from csv_utils import sum_unique_values
from web_utils import download_google_sheet


if __name__ == "__main__":
    sheet = sys.argv[1]
    tab = 0
    file_name = "data/sheets/as-is/swc.csv"
    download_google_sheet(file_name, sheet, tab)
    _, data = load_csv_file(file_name)
    swc_data = sum_unique_values(data, "Institution", "Attendees")
    save_dict_as_csv_file("data/sheets/filtered/swc_attendees.csv",
                          "Institution",
                          "Attendees",
                          swc_data)
