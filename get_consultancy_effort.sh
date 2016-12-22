#!/bin/bash

# Google Sheet ID and tab
SHEET=$1
TAB=1949517833

# Chart-FunderEffort tab
# Header assumed to include:
# Funder, Effort
python src/get_sheet.py $SHEET $TAB data/sheets/as-is/funders_effort.csv
