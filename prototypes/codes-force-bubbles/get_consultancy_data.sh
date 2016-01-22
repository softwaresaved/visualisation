#!/bin/bash

DOC_ID=$1
CSV_FILE=$2

wget --no-check-certificate --output-document=raw.csv "https://docs.google.com/spreadsheets/d/$DOC_ID/export?gid=0&format=csv"

python transform_consultancy_data.py raw.csv $CSV_FILE
