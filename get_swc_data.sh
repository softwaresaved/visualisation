#!/bin/bash

# GoogleSheet ID
SHEET_ID=$1

# Workshops sheet
# Header assumed to include:
# Code, Start, End, Department, Institution, Country, Domain,
# Attendees, Admin?, Host?, Host (fellow)?, Instruct, 
# Instruct (fellow), Help, Help (felllow) 
wget --no-check-certificate --output-document=data/swc.csv "https://docs.google.com/spreadsheets/d/${SHEET_ID}/export?gid=0&format=csv"
