# Software Sustainability Institute web-based data visualisation

Visualisations of [The Software Sustainability Institute](http://www.software.ac.uk) data.

To view, visit http://softwaresaved.github.io/visualisation.

---

## Get source code

Fork and clone this repository

* [Sign in](http://github.com/login) to GitHub.
* [Fork](https://github.com/softwaresaved/visualisation#fork-destination-box) this repository into your account.
* Clone your fork onto your computer:

```
$ git clone http://USERNAME@github.com/USERNAME/visualisation.git
$ cd visualisation
$ git remote add ssi  http://USERNAME@github.com/softwaresaved/visualisation.git
```

---

## Get Python 3

The [Anaconda](https://www.continuum.io/downloads) version of Python is recommended.

---

## Install Python packages

```
$ pip install -r requirements.txt
```

This installs (if not already installed):

* [requests](http://docs.python-requests.org/en/master/): Requests: HTTP for Humans.
* [google-api-python-client](https://github.com/google/google-api-python-client): Client library for Google's discovery based APIs. 

---

## View visualisations within GitHub pages

[GitHub pages](https://pages.github.com/) renders web site content in `gh-pages` branches of repositories hosted on GitHub.

When you push changes to the `gh-pages` branch of your cloned repository on GitHub, you can view the web site at http://USERNAME.github.io/visualisation/

---

## View visualisations within Python web server

Some browsers (e.g. Google Chrome) won't render JavaScript in HTML that is loaded into the browser via, for example, a file:// URL. 

Python 3 has a simple web server you can use to serve the pages. To start the web server:

```
$ cd visualisation
$ python -m http.server
```

Visit http://localhost:8000/ to see the visualisations index.html page.

---

## Deploy under Apache 2 web server

[Apache](https://httpd.apache.org/) is a popular web server.

* Note: These instructions assume the use of Apache 2.4 web server. Other versions of Apache 2, particularly Apache 2.2, differ in how they are installed, configured and managed. Consult the relevant documentation for your version of Apache 2.

These instructions assume you have sudo access to install and configure software (or a local system administrator can do this for you):

```
$ sudo su -
```

### Install Apache 2 on Ubuntu 14.04.3 LTS Trusty Tahr

Install:

```
$ apt-get install -y apache2 apache2-utils
$ apache2 -v
Server version: Apache/2.4.7 (Ubuntu)
Server built:   Jan 14 2016 17:45:23
$ service apache2 status
 * apache2 is running
```

### Install Apache 2 on Scientific Linux 6.6 (Carbon)

Install:

```
$ apt-get install -y httpd
$ /usr/sbin/httpd -v
Server version: Apache/2.2.15 (Unix)
Server built:   Aug 24 2015 11:20:01
$ chkconfig httpd on
$ /etc/init.d/httpd status
httpd (pid  18161) is running...
```

### Install Apache 2 on Scientific Linux 7.1 (Nitrogen)

Install:

```
$ apt-get install -y httpd
$ /usr/sbin/httpd -v
Server version: Apache/2.4.6 (Scientific Linux)
Server built:   Jul 23 2014 05:03:32
$ systemctl restart httpd.service
$ systemctl status httpd.service
$ systemctl enable httpd.service
$ systemctl status httpd.service
httpd.service - The Apache HTTP Server
   Loaded: loaded (/usr/lib/systemd/system/httpd.service; enabled)
   Active: active (running) since Mon 2016-03-07 13:02:03 GMT; 19s ago
n Main PID: 14675 (httpd)
```

### Clone this repository

Clone:

```
$ cd /var/www/html
$ git clone https://github.com/softwaresaved/visualisation
```

### Set permissions

* For Ubuntu:

```
$ chown -R www-data:www-data visualisation
```

* For Scientific Linux:

```
$ chown -R apache:apache visualisation
```

### View visualisations

Visit http://127.0.0.1/visualisation/

---

## Update Institute data

Create Google API project:

* Visit [Google API Console](https://console.developers.google.com/projectselector/apis/credentials)
* Click Create Project
* Enter project name e.g. ssi-viz

Enable Google Sheets API:

* Select your project.
* Click + ENABLE API
* Click Sheets API
* Click ENABLE

Create OAuth2 credentials:

* Click Credentials
* Click Create credentials
* Select OAuth client id
* Click Configure consent screen
* Enter 
  - E-mail address: user@somewhere.ac.uk
  - Product name shown to users: SSI visualisation scripts
* Select Application type: Other
* Name: SSI visualisation scripts downloader
* Click download icon to download JSON.
* Save as `client_secret.json` in the `visualisation` directory.

Download consultancy data:

```
$ python src/download_consultancy_data.py
```

Download Software Carpentry data:

```
$ python src/download_swc.py
```

Download policy data:

```
$ python src/download_policy.py
```

The first time you run one of these scripts, a browser will appear and you will be prompted for your Google username and password (if not already logged in) and then asked to allow the program access to your Google Sheets.

---

## JavaScript development

Browser developer tools:

* Google Chrome: CTRL+SHIFT+J opens Web Console and Debugger.
* Mozilla Firefox: CTRL+SHIFT+K opens Web Console and Debugger.

Comments:

* [jsdoc](http://usejsdoc.org/) is used for commenting JavaScript.

Logging:

* `console.log(...)` outputs to browser Web console.

---

## Copyright and licence

* Copyright 2015-2017, The University of Edinburgh and The University of Southampton except where noted in Third-party code below.
* Python code licence: [Apache 2.0](./LICENSE)
* JavaScript code licence: [GNU General Public License version 2](./LICENSE)

---

## Third-party code

Google Sheet and OAuth2 Python example

* https://developers.google.com/sheets/api/quickstart/python
* Copyright 2016, Google
* Licence: [Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0)
* Local code: `src/sheet_utils`

Bootstrap 3.3.6

* http://getbootstrap.com/
* Copyright 2011-2016 Twitter, Inc.
* Licence: [MIT License](https://github.com/twbs/bootstrap/blob/master/LICENSE)
* Local code: `css/bootstrapcss`, `css/bootstrap.min.css`, `js/bootstrap.js`, `js/bootstrap.min.js`

D3 4.2.1

* http://d3js.org/
* [Download page](https://github.com/d3/d3/releases/tag/v4.2.1)
* Copyright  2010-2016, Michael Bostock
* Licence: [BSD-style license](https://github.com/mbostock/d3/blob/master/LICENSE)
* Local code: `js/d3.js`,  `js/d3.min.js`

D3 bar chart

* http://bl.ocks.org/mbostock/3885304
* Copyright 2016, Mike Bostock
* Licence: [GNU General Public License version 3](https://opensource.org/licenses/GPL-3.0)
* Local code: `js/barchart.js` and `css/barchart.css` are modified versions.

D3 horizontal bar chart (bar chart IIc)

* http://bl.ocks.org/mbostock/7341714
* Copyright 2016, Mike Bostock
* Licence: [GNU General Public License version 3](https://opensource.org/licenses/GPL-3.0)
* Local code: `js/barchart_horiz.js` and `css/barchart_horiz.css` are modified versions.

D3 pie chart

* https://bl.ocks.org/mbostock/3887235
* Copyright 2016, Mike Bostock
* Licence: [GNU General Public License version 3](https://opensource.org/licenses/GPL-3.0)
* Local code: `js/pie.js` and `css/pie.css` are modified versions.

D3 circle packing

* http://bl.ocks.org/mbostock/07ec62d9957a29a30e71cad962ff2efd
* Copyright 2016, Mike Bostock
* Licence: [GNU General Public License version 3](https://opensource.org/licenses/GPL-3.0)
* Local code: `js/circle_packing.js` and `css/circle_packing.css` are modified versions.

jQuery 2.2.1

* http://jquery.com/
* Copyright 2005, 2013 jQuery Foundation, Inc. and other contributors
* Licence: [MIT license](https://github.com/jquery/jquery/blob/master/LICENSE.txt)
* Local code: `js/jquery.js`,  `js/jquery.min.js`

Underscore 1.8.3

* http://underscorejs.org
* Copyright 2009-2015 Jeremy Ashkenas, DocumentCloud and Investigative Reporters & Editors
* Licence: [MIT license](https://github.com/jashkenas/underscore/blob/master/LICENSE)
* Local code: `js/underscore.js`,  `js/underscore-min.js`
