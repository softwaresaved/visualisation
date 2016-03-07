#!/bin/bash

# GoogleSheet ID
SHEET_ID=$1

# Projects tab
* The first three lines are assumed to be blank.
# The fourth, header line, assumed to include:
# Project Name, Funder(s), Group(s), Institution, Type", PMs, 
# Research Field
wget --no-check-certificate --output-document=consultancy_raw.csv "https://docs.google.com/spreadsheets/d/${SHEET_ID}/export?gid=0&format=csv"
# Parse above file to ignore blank lines and project columns, to
# create a new file with header:
# Project Name, Primary Funder, Other Funders, Group(s), Institution, 
# Type, PMs, Research Field
# where Funder(s) values from the original data are split on the first
# "," to derive the Primary Funder and Other Funders.

python transform_consultancy_data.py consultancy_raw.csv data/consultancy.csv

# Chart-FunderEffort tab
# Header assumed to include:
# Funder, Effort
wget --no-check-certificate --output-document=data/funders_effort.csv "https://docs.google.com/spreadsheets/d/${SHEET_ID}/export?gid=1949517833&format=csv"

# Chart-Funding tab
# Header assumed to include:
# Funder, Projects
wget --no-check-certificate --output-document=data/funders_project.csv "https://docs.google.com/spreadsheets/d/${SHEET_ID}/export?gid=7&format=csv"
