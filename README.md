# Software Sustainability Institute web-based data visualisation

Visualisations of [The Software Sustainability Institute](http://www.software.ac.uk) data.

To view, visit http://softwaresaved.github.io/visualisation.

---

## Requesting a visualisation for a data set (Institute staff)

To request that a data set be added to the visualisations:

* Consider data you currently maintain in Google Sheets.
  - The data should be in a reasonably well-structured format.
  - See [Spreadsheets](./SpreadsheetDesign.md) for the preferred format.
* For each data set you'd like to have a visualisation for, create a New issue:
  - Add the "Data" label to the issue.
  - Add the Google Sheet URL, tab name and additional information on the data you want visualised e.g. how frequently you update its content.
    - Remember the Google Sheet URL should not be anonymously readable unless it's a public data set.
  - Suggest visualisations you might want (optional):
    - You may want to look at [Chart Suggestions - a Thought Starter](https://www.flickr.com/photos/amit-agarwal/3196386402/)...
    - ...and D3 examples (e.g. see [M Bostock](https://bl.ocks.org/mbostock)) for possibilities!

**Note:** Any vague suggestions for which data does not yet exist, or does exist but not as a Google Sheet, can be added as a comment to the general issue, [What data should we visualise?](https://github.com/softwaresaved/visualisation/issues/1).

---

## Deploy visualisations

### Get source code

Fork and clone this repository

* [Sign in](http://github.com/login) to GitHub.
* [Fork](https://github.com/softwaresaved/visualisation#fork-destination-box) this repository into your account.
* Clone your fork onto your computer:

```
$ git clone http://USERNAME@github.com/USERNAME/visualisation.git
$ cd visualisation
$ git remote add ssi  http://USERNAME@github.com/softwaresaved/visualisation.git
```

### Get Python 3

The [Anaconda](https://www.continuum.io/downloads) version of Python is recommended.

### Install Python packages

```
$ pip install -r requirements.txt
```

This installs (if not already installed):

* [requests](http://docs.python-requests.org/en/master/): Requests: HTTP for Humans.
* [google-api-python-client](https://github.com/google/google-api-python-client): Client library for Google's discovery based APIs. 

### View visualisations within GitHub pages

[GitHub pages](https://pages.github.com/) renders web site content in `gh-pages` branches of repositories hosted on GitHub.

When you push changes to the `gh-pages` branch of your cloned repository on GitHub, you can view the web site at http://USERNAME.github.io/visualisation/

### View visualisations within Python web server

Some browsers (e.g. Google Chrome) won't render JavaScript in HTML that is loaded into the browser via, for example, a file:// URL. 

Python 3 has a simple web server you can use to serve the pages. To start the web server:

```
$ cd visualisation
$ python -m http.server
```

Visit http://localhost:8000/ to see index.html.

### Deploy under Apache 2 web server

[Apache](https://httpd.apache.org/) is a popular web server.

* Note: These instructions assume the use of Apache 2.4 web server. Other versions of Apache 2, particularly Apache 2.2, differ in how they are installed, configured and managed. Consult the relevant documentation for your version of Apache 2.

These instructions assume you have sudo access to install and configure software (or a local system administrator can do this for you):

```
$ sudo su -
```

**Install Apache 2 on Ubuntu 14.04.3 LTS Trusty Tahr**

Install:

```
$ apt-get install -y apache2 apache2-utils
$ apache2 -v
Server version: Apache/2.4.7 (Ubuntu)
Server built:   Jan 14 2016 17:45:23
$ service apache2 status
 * apache2 is running
```

**Install Apache 2 on Scientific Linux 6.6 (Carbon)**

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

**Install Apache 2 on Scientific Linux 7.1 (Nitrogen)**

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

**Clone the repository**

Clone:

```
$ cd /var/www/html
$ git clone https://github.com/softwaresaved/visualisation
```

**Set permissions**

* For Ubuntu:

```
$ chown -R www-data:www-data visualisation
```

* For Scientific Linux:

```
$ chown -R apache:apache visualisation
```

**View visualisations**

Visit http://127.0.0.1/visualisation/ to see index.html.

---

## Update data (Institute staff)

Updates to data in `data/` can be downloaded from the Institute's Google Sheets and private GitHub repositories.

### Set up Google API authentication

You need to set up Google API authentication to access the Institute's Google Sheets as they are private. 

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

Run a data download script to add the Google API authentication files to your local machine:

Download data:

```
$ python src/download_sheets.py --noauth_local_webserver --sheets sheets.yml
```

When you run this script for the first time, with the given flag, Google's authentication component will ask you to give your permission for the use of your credentials to access Google Sheets to which you have access. It does this by asking you to go to a Google Accounts link to get a verification code and enter that code. For example:

```
Go to the following link in your browser:
https://accounts.google.com/o/oauth2/auth?client_id=12345-678910.apps.googleusercontent.com&redirect_uri=urn%3Aietf%3Awg%3Aoauth%3A2.0%3Aoob&access_type=offline&response_type=code&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fspreadsheets.readonly

Enter verification code:
```

Using a web browser:

* Go to the link you are shown.
* Sign in to your Google Account.
* Click ALLOW to allow access to the Google Sheets.
* Copy your verification code.

Enter the verification code to successfully authenticate. For example:

```
Enter verification code: ABCDEF1234567890
```

You should then see a message like:

```
Authentication successful.
Storing credentials to /home/someuser/credentials/sheets.googleapis.com-python-quickstart.json
```

When you run any of the download scripts, you will not be asked to authenticate again.

### Download updated Google Sheets data

Run:

```
$ python src/download_sheets.py --noauth_local_webserver --sheets sheets.yml
```

### Create GitHub personal access token

You need to set up a GitHub personal access token as some of the Institute's GitHub repositories are private.

Within GitHub:

* Select USER => Settings
* Click Settings
* Click Developer settings
* Click Personal access tokens
* Click Generate new token
* Enter Token description: metrics
* Select scopes: check repo
* Click Generate token
* Copy the token text

### Download updated GitHub data

Run:

```
$ python src/download_repository_files.py --token <YOUR_GITUHUB_TOKEN> --repositories repositories.yml
```

As an alternative to the command-line flag, a GITHUB_TOKEN environment variable can be set e.g.

```
$ GITHUB_TOKEN=<YOUR_GITHUB_TOKEN> python src/download_repository_files.py --repositories repositories.yml
```

---

## Development

Introduction to HTML, CSS, JavaScript and D3:

* Software Carpentry's [Visualizing your data on the web using D3](http://isakiko.github.io/D3-visualising-data/).

Browser developer tools:

* Google Chrome: CTRL+SHIFT+J opens Web Console and Debugger.
* Mozilla Firefox: CTRL+SHIFT+K opens Web Console and Debugger.

Comments:

* [jsdoc](http://usejsdoc.org/) can be used for commenting JavaScript.

Logging:

* `console.log(...)` outputs to browser Web console.

Google Chrome developer tools:

* Force Chrome to reload page, JavaScript and CSS: CTRL+reload icon.
* View element style: Right-click => Inspect:
  - Explore Elements and Styles tabs.
* Console tab:
  - Outputs from `console.log("...")`.
  - Errors.
* Elements tab:
  - HTML elements.
  - Roll mouse over Elements to highlight elements in HTML.
  - Check layout and styles.
  - Make changes in Styles tab to see effect of changes.
* Sources tab:
  - CTRL+P: Load and view sources e.g. `.html`, `.jsp`, `.css`.
  - Add breakpoints.

Google Sheets and OAuth2 APIs:

* [Introduction to the Google Sheets API](https://developers.google.com/sheets/api/guides/concepts)
* Google Sheets API v4 [Python Quickstart](https://developers.google.com/sheets/api/quickstart/python)

---

## Copyright and licence

* Copyright 2015-2018, The University of Edinburgh and The University of Southampton except where noted in Third-party code below.
* Python code licence: [Apache 2.0](./LICENSE)
* JavaScript code licence: [GNU General Public License version 2](./LICENSE)

---

## Third-party code

Google Sheet and OAuth2 Python example

* https://developers.google.com/sheets/api/quickstart/python
* Copyright 2016, Google
* Licence: [Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0)
* Local code: `src/sheet_utils`

Automattic Color.js

* https://github.com/Automattic/Color.js
* Copyright 2015, Matt Wiebe
* Licence: [GNU General Public License version 2](https://github.com/Automattic/Color.js/blob/master/LICENSE)
* Local code: `js/Color.js`

Bootstrap 3.3.6

* http://getbootstrap.com/
* Copyright 2011-2016 Twitter, Inc.
* Licence: [MIT License](https://github.com/twbs/bootstrap/blob/master/LICENSE)
* Local code: `css/bootstrap.css`, `css/bootstrap.min.css`, `js/bootstrap.js`, `js/bootstrap.min.js`

D3 4.2.1

* http://d3js.org/
* [Download page](https://github.com/d3/d3/releases/tag/v4.2.1)
* Copyright  2010-2016, Michael Bostock
* Licence: [BSD-style license](https://github.com/mbostock/d3/blob/master/LICENSE)
* Local code: `js/d3.js`,  `js/d3.min.js`

D3 horizontal bar chart

* https://bl.ocks.org/curran/e842c1b64974666c60fc3e437f8c8cf9
* Copyright 2017, Curran Kelleher
* Licence: [MITc License](https://opensource.org/licenses/MIT)
* Local code: `js/barchart_horiz.js`, `js/barchart_horiz_shaded.js` and `js/barchart.js` are modified versions.

D3 pie chart

* https://bl.ocks.org/mbostock/3887235
* Copyright 2016, Mike Bostock
* Licence: [GNU General Public License version 3](https://opensource.org/licenses/GPL-3.0)
* Local code: `js/pie.js` is a modified version.

D3 circle packing

* http://bl.ocks.org/mbostock/07ec62d9957a29a30e71cad962ff2efd
* Copyright 2016, Mike Bostock
* Licence: [GNU General Public License version 3](https://opensource.org/licenses/GPL-3.0)
* Local code: `js/circle_packing.js` is a modified version.

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
