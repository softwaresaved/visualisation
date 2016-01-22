# EPCC web-based data visualisation

Current examples of use include:

* Visualising usage data from HPC facilities. Initially based around
[ARCHER](http://www.archer.ac.uk):
  - ARCHER [Application usage over past month](http://www.archer.ac.uk/status/codes/).
* Visualising [The Software Sustainability Institute](http://www.software.ac.uk) data:
  - [Consultancy](https://ssi-dev.epcc.ed.ac.uk/viz/prototypes/codes-force-bubbles/ssi_consultancy.php)
  - [Software Carpentry](https://ssi-dev.epcc.ed.ac.uk/viz/prototypes/codes-force-bubbles/ssi_swc.php)

---

## Copyright and licence

* Copyright 2016-2016, The University of Edinburgh.
* Licence: [GPL 2](./LICENSE]).

---

## Third-party code

Bootstrap 3.0.3

* http://getbootstrap.com/
* Copyright 2011-2016 Twitter, Inc.
* License: MIT license
* Local copies:

```
prototypes/codes-force-bubbles/css/bootstrap_min.css
prototypes/codes-force-bubbles/css/bootstrap.css
prototypes/codes-force-bubbles/js/bootstrap.js
```

* prototypes/codes-force-bubbles/css/bootstrap_min.css changed to not disrupt ARCHER styles - A. Turner, Oct 2015.

D3

* http://d3js.org/
* Copyright  2010-2016, Michael Bostock
* License: BSD license

```
prototypes/codes-force-bubbles/js/d3.min.js
prototypes/codes-streamgraph/js/d3.min.js
```

jQuery 2.0.0

* http://jquery.com/
* Copyright 2005, 2013 jQuery Foundation, Inc. and other contributors
* License: MIT license
* Local copies:

```
prototypes/codes-force-bubbles/js/jquery.js
prototypes/codes-streamgraph/js/jquery.js
```

Underscore 1.5.2

* http://underscorejs.org
* Copyright 2009-2015 Jeremy Ashkenas, DocumentCloud and Investigative Reporters & Editors
* License: MIT license
* Local copies:

```
prototypes/codes-force-bubbles/js/underscore.js
```

---

## How to configure for ARCHER usage data

ARCHER usage data is in a file of comma-separated values:

* The header line is assumed to contain fields: "Rank", "Code",
  "Usage", "Jobs", "Users", "CodeType", "ProgLang", "ResArea",
  "LicType" 


To deploy under ARCHER:

* Edit graph_bubbles.php and change:

```
@import url("css/bootstrap_min.css");
```

* to

```
@import url("/assets/css/bootstrap_min.css");
```

* Edit code_usage.php and change:

```
d3.csv('data/d3codes_summary.csv', function (error, data) {
```

* to

```
d3.csv('/dynamic-content/monitoring/d3codes_summary.csv', function (error, data) {
```

---

## How to configure for SSI consultancy data

SSI consultancy data is in a Google spreadsheet of comma-separated values:

* The first three lines are assumed to be blank.
* The fourth, header, line is assumed to contain fields: "Project
  Name", "Funder(s)", "Group(s)", "Institution", "Type", "PMs",
  "Research Field"

To download and transform the SSI consultancy data:

```
$ cd prototypes/codes-force-bubbles/transform_consultancy_data.py
$ ./get_consultancy_data.sh SSI_CONSULTANCY_SPREADSHEET_ID data/ssi-consultancy.csv
```

where SSI_CONSULTANCY_SPREADSHEET_ID is the ID of the Google
spreadsheet.

See [prototypes/codes-force-bubbles/transform_consultancy_data.py](./prototypes/codes-force-bubbles/transform_consultancy_data.py) for information on how the data is transformed into a state for rendering.

---

## JavaScript development

Logging:

* console.log(...) outputs to browser console. 
* CTRL+SHIFT+J opens console in Google Chrome.

---

## Possible SSI enhancements

* Add links from pop-up meta-data to open call web pages on SSI web site. Requires adding this information to the CSV file.
* Smaller text fonts
* Alternative grid layouts e.g. 2 columns, multiple rows. See [Using d3js to draw a grid](http://knowledgestockpile.blogspot.co.uk/2012/01/using-d3js-to-draw-grid.html)
