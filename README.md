# Software Sustainability Institute web-based data visualisation

Visualising [The Software Sustainability Institute](http://www.software.ac.uk) data.

---

## Copyright and licence

* Copyright 2015-2016, The University of Edinburgh except where noted in Third-party code below.
* Licence: [GPL 2](./LICENSE]).

---

## Third-party code

Bootstrap 3.0.3

* http://getbootstrap.com/
* Copyright 2011-2016 Twitter, Inc.
* License: MIT license
* Local copies:

```
css/bootstrap_min.css
css/bootstrap.css
js/bootstrap.js
```

* css/bootstrap_min.css changed to not disrupt ARCHER styles - A. Turner, Oct 2015.

D3

* http://d3js.org/
* Copyright  2010-2016, Michael Bostock
* License: BSD license

```
js/d3.min.js
```

jQuery 2.0.0

* http://jquery.com/
* Copyright 2005, 2013 jQuery Foundation, Inc. and other contributors
* Licence: MIT license
* Local copies:

```
js/jquery.js
```

Underscore 1.5.2

* http://underscorejs.org
* Copyright 2009-2015 Jeremy Ashkenas, DocumentCloud and Investigative Reporters & Editors
* Licence: MIT license
* Local copies:

```
js/underscore.js
```

Usage visualisation scripts

* https://github.com/aturner-epcc/usage-visualisation
* Copyright 2015, The University of Edinburgh.
* Licence:  GNU General Public License, version 2.
* `js/graph_bubbles.js` is derived from `prototypes/codes-force-bubbles/code_usage.html` (commit [b5749bb7](https://github.com/aturner-epcc/usage-visualisation/commit/b5749bb711045246abc3edeec4e98b18a28d2c53)).

D3 pie chart

* https://bl.ocks.org/mbostock/3887235
* Copyright 2016, Mike Bostock
* Licence: [GNU General Public license, version 3](https://opensource.org/licenses/GPL-3.0)
* `js/pie.js` and `css/pie.css` are derived from [index.html](https://bl.ocks.org/mbostock/3887235#index.html) downloaded on 02/03/2016.

D3 bar chart

* http://bl.ocks.org/mbostock/3885304
* Copyright 2016, Mike Bostock
* Licence: [GNU General Public license, version 3](https://opensource.org/licenses/GPL-3.0)
* `js/pie.js` and `css/barchart.css` are derived from [index.html](https://bl.ocks.org/mbostock/3885304#index.html) downloaded on 02/03/2016.

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
