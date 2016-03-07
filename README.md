# Software Sustainability Institute web-based data visualisation

Visualising [The Software Sustainability Institute](http://www.software.ac.uk) data.

---

## Copyright and licence

* Copyright 2015-2016, The University of Edinburgh and The University of Southampton except where noted in Third-party code below.
* Licence: [GNU General Public License, version 2](,/LICENSE)

---

## Third-party code

Bootstrap 3.0.3

* http://getbootstrap.com/
* Copyright 2011-2016 Twitter, Inc.
* Licence: [MIT License](https://github.com/twbs/bootstrap/blob/master/LICENSE)
* Local code: `css/bootstrap_min.css`, `css/bootstrap.css`, `js/bootstrap.js`
  - css/bootstrap_min.css changed by Andy Turner October 2015, to not disrupt ARCHER styles.

D3

* http://d3js.org/
* Copyright  2010-2016, Michael Bostock
* Licence: [BSD-style license](https://github.com/mbostock/d3/blob/master/LICENSE)
* Local code: `js/d3.min.js`

D3 bar chart

* http://bl.ocks.org/mbostock/3885304
* Copyright 2016, Mike Bostock
* Licence: [GNU General Public License version 3](https://opensource.org/licenses/GPL-3.0)
* Local code: `js/pie.js` and `css/barchart.css` are modified versions.

D3 pie chart

* https://bl.ocks.org/mbostock/3887235
* Copyright 2016, Mike Bostock
* Licence: [GNU General Public License version 3](https://opensource.org/licenses/GPL-3.0)
* Local code: js/pie.js` and `css/pie.css` are modified versions.

jQuery 2.0.0

* http://jquery.com/
* Copyright 2005, 2013 jQuery Foundation, Inc. and other contributors
* Licence: [MIT license](https://github.com/jquery/jquery/blob/master/LICENSE.txt)
* Local code: `js/jquery.js`

Underscore 1.5.2

* http://underscorejs.org
* Copyright 2009-2015 Jeremy Ashkenas, DocumentCloud and Investigative Reporters & Editors
* Licence: (MIT license](https://github.com/jashkenas/underscore/blob/master/LICENSE)
* Local code: `js/underscore.js`

Usage visualisation

* https://github.com/aturner-epcc/usage-visualisation
* Copyright 2015, The University of Edinburgh.
* Licence: [GNU General Public License version 2](https://github.com/aturner-epcc/usage-visualisation/blob/master/LICENSE)
* Local code: `js/graph_bubbles.js` is a modified version.


---

## How update consultancy data

Consultancy data is in a Google spreadsheet of comma-separated values:

* The first three lines are assumed to be blank.
* The fourth, header, line is assumed to contain fields: "Project
  Name", "Funder(s)", "Group(s)", "Institution", "Type", "PMs",
  "Research Field"

To download and transform the consultancy data:

```
$ ./get_consultancy_data.sh CONSULTANCY_SPREADSHEET_ID
```

where CONSULTANCY_SPREADSHEET_ID is the ID of the Google
spreadsheet.

See [transform_consultancy_data.py](./transform_consultancy_data.py) for information on how the data is transformed into a state for rendering.

---

## JavaScript development

Browser developer tools:

* Google Chrome: CTRL+SHIFT+J opens Web Console and Debugger.
* Mozilla Firefox: CTRL+SHIFT+K opens Web Console and Debugger.

Comments:

* [jsdoc](http://usejsdoc.org/) is used for commenting JavaScript.
* [jsdoc on GitHub](https://github.com/jsdoc3/jsdoc)

Logging:

* console.log(...) outputs to browser console.

---
