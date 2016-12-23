"""Download Software Used In Research Combined Results
Unique names for publication tab.
"""

# Copyright (c) 2016 The University of Edinburgh

import sys

from web_utils import download_google_sheet

if __name__ == "__main__":
    sheet = sys.argv[1]
    tab = 2010786314
    file_name = "data/sheets/as-is/software.csv"
    download_google_sheet(file_name, sheet, tab)
