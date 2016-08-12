#!/bin/bash

python aggregate_data.py count dataCleaning/data/raw_institutions.csv "Home institution" "Institution" "Count" data/static/filtered/fellows_institutions.csv
