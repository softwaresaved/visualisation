# Implementation details

## D3 visualisations

```
$ ./get_consultancy_data.sh SHEET_ID
```

downloads data/funders_effort.csv and data/funders_project.csv which are rendered by consultancy/charts.html, js/barchart.js, js/pie.js

```
$ ./get_swc_data.sh SHEET_ID
```

downloads data/swc.csv and runs filter_swc.sh which runs aggregate_data.py and produces data/swc_filtered.csv which is rendered by js/barchart.js, js/pie.js

Static data set data/The use of software in research (Responses) Cleaned For All Hands Hack - Form Responses 1.csv can be processed with 

```
$ bash filter_software_survey.sh
```

which runs aggregate_data.py and produces data/SoftwareSurvey2014OS.csv and data/SoftwareSurvey2014Software.csv which are rendered by policy/survey.html, js/barchart_horiz.js

## Bubble graph visualisations (to be deprecated)

```
$ ./get_consultancy_data.sh SHEET_ID
```

downloads  consultancy_raw.csv and runs transform_consultancy_data.py which produces data/consultancy.csv which is rendered by consultancy/bubble.html and related JavaScript.

```
$ ./get_swc_data.sh SHEET_ID
```

downloads data/swc.csv and runs filter_swc.sh which runs aggregate_data.py and produces data/swc_filtered.csv which is rendered by swc/bubble.html and related JavaScript.
