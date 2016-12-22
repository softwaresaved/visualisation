#!/bin/bash

python src/get_counts.py dataCleaning/data/raw_institutions.csv "Home institution" "Institution" "Count" data/static/filtered/fellows_institutions.csv
