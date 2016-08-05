#!/bin/bash

python aggregate_data.py count data/The\ use\ of\ software\ in\ research\ \(Responses\)\ Cleaned\ For\ All\ Hands\ Hack\ -\ Form\ Responses\ 1.csv "Question 11: Please provide the name(s) of the main research software you use." "Research Software" "Count" data/SoftwareSurvey2014Software.csv

python aggregate_data.py count data/The\ use\ of\ software\ in\ research\ \(Responses\)\ Cleaned\ For\ All\ Hands\ Hack\ -\ Form\ Responses\ 1.csv "Extra question 4: What is your preferred Operating System?" "Operating System"  "Count" data/SoftwareSurvey2014OS.csv
