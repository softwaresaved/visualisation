"""Download Software Carpentry sheets:

* SSI SWC from 2012-04-30 to 2014-04-09 from Mike sheet, Workshops-Summary tab.
* carpentry-workshops-instructors-affiliation_GB_2017-12-14 sheet
  - workshops-affiliation_GB_2017-12-14 tab
  - instructors-affiliation_GB_2017-12-14 tab
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

    # carpentry-workshops-instructors-affiliation_GB_2017-12-14
    sheet_id = '1-tfDUusAIs5clffqDpsHsncn7-W47-UC-TepG3xTlwU'

    tab_and_range = "workshops-affiliation_GB_2017-12-14!A1:B38"
    data = download_sheet(sheet_id, tab_and_range)
    file_name = "data/sheets/as-is/swc_workshops_affiliation_gb_2017.csv"
    save_list_as_csv_file(data, file_name)

    tab_and_range = "instructors-affiliation_GB_2017-12-14!A1:B42"
    data = download_sheet(sheet_id, tab_and_range)
    file_name = "data/sheets/as-is/swc_instructors_affiliation_gb_2017.csv"
    save_list_as_csv_file(data, file_name)
