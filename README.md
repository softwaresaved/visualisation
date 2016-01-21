# usage-visualisation

Web-based visualisation of data. 

Current examples of use include:

* Visualising usage data from HPC facilities. Initially based around ARCHER (http://www.archer.ac.uk). See ARCHER [Application usage over past month]( http://www.archer.ac.uk/status/codes/).
* Visualising project effort by The Software Sustainability Institute (http://www.software.ac.uk).

---

## Copyright and licence

* Copyright 2016-2016, The University of Edinburgh.
* Licence: GPL 2 (see [LICENCE](./LICENSE]).

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

## Use with SSI consultancy data

Assumes schema:

```
Project Name,SSI Contact,Other SSI Staff,Funder(s),Group(s),Institution,Contact,Type,Start,End,Days,Months,P-days,PMs,FTE,Research Field,#Blog posts,Trac Ticket,Notes,Blog post links and papers,,,,,,,,Email
```

Get data and filter data:

```

$ ./get_consultancy_data.sh SSI_CONSULTANCY_SPREADSHEET_ID/export?gid=0&format=csv' data/ssi-consultancy.csv
```
