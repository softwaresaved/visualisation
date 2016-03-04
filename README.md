# Software Sustainability Institute web-based data visualisation

Visualising [The Software Sustainability Institute](http://www.software.ac.uk) data.


---

## Copyright and licence

* Copyright 2016-2016, The University of Edinburgh except where identified below.
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
* License: MIT license
* Local copies:

```
js/jquery.js
```

Underscore 1.5.2

* http://underscorejs.org
* Copyright 2009-2015 Jeremy Ashkenas, DocumentCloud and Investigative Reporters & Editors
* License: MIT license
* Local copies:

```
js/underscore.js
```

Andrew Turner's ARCHER usage visualisation scripts:

* https://github.com/aturner-epcc/usage-visualisation
* Copyright 2015, The University of Edinburgh.
* Licence: [GPL 2](./LICENSE]).
* `js/graph_bubbles.js` was abstracted out from `prototypes/codes-force-bubbles/code_usage.html` (commit [b5749bb7](https://github.com/mikej888/usage-visualisation/commit/b5749bb711045246abc3edeec4e98b18a28d2c53)).

---

## How to configure for consultancy data

Consultancy data is in a Google spreadsheet of comma-separated values:

* The first three lines are assumed to be blank.
* The fourth, header, line is assumed to contain fields: "Project
  Name", "Funder(s)", "Group(s)", "Institution", "Type", "PMs",
  "Research Field"

To download and transform the consultancy data:

```
$ ./get_consultancy_data.sh CONSULTANCY_SPREADSHEET_ID data/ssi-consultancy.csv
```

where CONSULTANCY_SPREADSHEET_ID is the ID of the Google
spreadsheet.

See [transform_consultancy_data.py](./transform_consultancy_data.py) for information on how the data is transformed into a state for rendering.

---

## JavaScript development

Logging:

* console.log(...) outputs to browser console. 
* CTRL+SHIFT+J opens console in Google Chrome.

---

## Possible enhancements

* Add links from pop-up meta-data to open call web pages on web site. Requires adding this information to the CSV file.
* Smaller text fonts
* Alternative grid layouts e.g. 2 columns, multiple rows. See [Using d3js to draw a grid](http://knowledgestockpile.blogspot.co.uk/2012/01/using-d3js-to-draw-grid.html)
