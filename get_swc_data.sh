#!/bin/bash

# Google Sheet ID and tab
SHEET=$1
TAB=0

# Workshops sheet
# Header assumed to include:
# Code, Start, End, Department, Institution, Country, Domain,
# Attendees, Admin?, Host?, Host (fellow)?, Instruct, 
# Instruct (fellow), Help, Help (felllow) 
python src/get_sheet.py $SHEET $TAB data/sheets/as-is/swc.csv
bash filter_swc_data.sh
