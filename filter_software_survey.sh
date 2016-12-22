#!/bin/bash

python src/get_counts.py data/static/raw/The\ use\ of\ software\ in\ research\ \(Responses\)\ Cleaned\ For\ All\ Hands\ Hack\ -\ Form\ Responses\ 1.csv "Question 11: Please provide the name(s) of the main research software you use." "Research Software" "Count" data/static/filtered/SoftwareSurvey2014Software.csv

python src/get_counts.py data/static/raw/The\ use\ of\ software\ in\ research\ \(Responses\)\ Cleaned\ For\ All\ Hands\ Hack\ -\ Form\ Responses\ 1.csv "Extra question 4: What is your preferred Operating System?" "Operating System"  "Count" data/static/filtered/SoftwareSurvey2014OS.csv
