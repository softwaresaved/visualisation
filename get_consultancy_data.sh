#!/bin/bash

# Google Sheet ID and tab
SHEET=$1
TAB=0

# Projects tab
# The first three lines are assumed to be blank.
# The fourth, header line, assumed to include:
# Project Name, Funder(s), Group(s), Institution, Type", PMs, 
# Research Field
python src/get_sheet.py $SHEET $TAB consultancy_raw.csv
# Parse above file to ignore blank lines and project columns, to
# create a new file with header:
# Project Name, Primary Funder, Other Funders, Group(s), Institution, 
# Type, PMs, Research Field
# where Funder(s) values from the original data are split on the first
# "," to derive the Primary Funder and Other Funders.

# Strip out first 3 messy rows so top row is header.
tail -n+4 consultancy_raw.csv > consultancy_raw_sliced.csv
python transform_consultancy_data.py consultancy_raw_sliced.csv data/sheets/filtered/consultancy.csv
python src/get_sums.py data/sheets/filtered/consultancy.csv "Project Name" "PMs" "Project" "PMs" data/sheets/filtered/project_effort.csv
