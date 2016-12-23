"""Download consultancy projects sheet Funding tab.

Usage:

   $ python download_consultancy_projects.py SHEET

where SHEET is the Google Sheet ID.
"""

# Copyright (c) 2016 The University of Edinburgh

import sys

from web_utils import download_google_sheet

if __name__ == "__main__":
    sheet = sys.argv[1]
    tab = 7
    file_name = "data/sheets/as-is/funders_projects.csv"
    download_google_sheet(file_name, sheet, tab)
