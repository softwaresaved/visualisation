#!/bin/bash

DOC_ID=$1

wget --no-check-certificate --output-document=consultancy_raw.csv "https://docs.google.com/spreadsheets/d/$DOC_ID/export?gid=0&format=csv"
python transform_consultancy_data.py consultancy_raw.csv data/consultancy.csv

wget --no-check-certificate --output-document=data/funders_effort.csv "https://docs.google.com/spreadsheets/d/$DOC_ID/export?gid=1949517833&format=csv"
