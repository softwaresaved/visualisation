#!/bin/bash

DOC_ID=$1
CSV_FILE=$2

wget --no-check-certificate --output-document=raw.csv "https://docs.google.com/spreadsheets/d/$DOC_ID/export?gid=0&format=csv"

# Trim first three blank rows from spreadsheet
awk 'NR > 3 { print }' < raw.csv > trimmed.csv

python filter_ssi_consultancy.py trimmed.csv $CSV_FILE
