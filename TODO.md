# TODOs

## Refactoring

Look at src/csv_utils.py (count_unique_values) challenges in handling data with spaces, newlines, semi-colons.

Look at src/csv_utils.py (count_unique_values) in terms of ensuring equality of upper, lower and mixed case values that are the same.

## Look at additional data sets

Simon:

* Look at use of stacked charts for data/The use of software in research (Responses) Cleaned For All Hands Hack - Form Responses 1.csv.

Neil:

* How many applications we get to each of the things we ask for applications for (workshops, Fellows, open calls, surveys), split by institution, gender, and primary domain of applicant etc.
* Breakdown of what was accepted. For open call, we have this data (applications, accepted), but would need cleaning (particularly for applications)
* Top 5 most mentioned pieces of software across our blog/news/twitter, surveys and workshops, using a model that does some sort of weighting for the last few months and across different media.
* How many people we've helped each month. (not sure about this one, not necessarily easy to define...). Ideally split into the types of impact (societal, knowledge transfer, economic etc)

Shoaib:

* Fellows by discipline. This data has been collected.
* 3 or more pieces of software you use most. Requires free text processing.

Aleksandra:

* Number of SWC/DC workshops held every year in the UK.
* Training-related table, like http://1onjea25cyhx3uvxgs4vu325.wpengine.netdna-cdn.com/wp-content/uploads/2014/11/blog_dataChart_white.png)
* Key skills recognised by the RCs that need more training investments, that fall into reproducible science, (big) data science, etc. categories that fall within our remit.

Mario:

* Fellows applications by institution and city via both bar chart and map.
* Map-based visualisation of where fellows have visited (based on work by Mario and Devasena at https://github.com/softwaresaved/SSINetworkGraphics) from their home institution.

## Look at alternative D3 visualisations

Do an example using [Population Pyramid](http://bl.ocks.org/mbostock/4062085) - stacked bars - to render effort per funder.

## Documentation

Write guidance for theme leads on how data can be organised in CSV (GoogleSheet/Drupal-friendly formats) to make visualisation easier.

Write guidance on how to add new visualisations.

Add links from pop-up meta-data to web pages. Requires adding this information to the CSV file and extending D3 components to read and render this.
