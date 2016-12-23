"""Download consultancy projects sheet FunderEffort tab."""

# Copyright (c) 2016 The University of Edinburgh

import sys

from web_utils import download_google_sheet

if __name__ == "__main__":
    sheet = sys.argv[1]
    tab = 1949517833
    file_name = "data/sheets/as-is/funders_effort.csv"
    download_google_sheet(file_name, sheet, tab)
