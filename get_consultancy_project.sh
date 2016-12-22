#!/bin/bash

# Google Sheet ID and tab
SHEET=$1
TAB=7

# Chart-Funding tab
# Header assumed to include:
# Funder, Projects
python src/get_sheet.py $SHEET $TAB data/sheets/as-is/funders_project.csv
