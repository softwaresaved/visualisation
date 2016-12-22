"""Get a Google Sheet as comma-separated values and save in a file.

Usage:

   $ python get_sheet.py SHEET_ID TAB_ID FILE_NAME

For example, to get a tab in a sheet
https://docs.google.com/spreadsheets/d/a1b2c3d4/export?gid=7:

   $ python get_sheet.py a1b2c3d4 7 data.csv
"""

# Copyright (c) 2016 The University of Edinburgh


import sys
from web_utils import download_google_sheet


if __name__ == "__main__":
    sheet = sys.argv[1]
    tab = sys.argv[2]
    file_name = sys.argv[3]
    download_google_sheet(file_name, sheet, tab)
