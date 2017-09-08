# Spreadsheets

The visualisation scripts visualise data downloaded from Google Sheets. 

## Post-processing in Python is a problem

After the sheets are downloaded, some are post-processed using Python scripts to do one or more of:

* Get the data into a form which is easy to visualise using JavaScript.
* Strip out personal information such as names and e-mail addresses.
* Perform calculations across the data e.g. calculating totals.

For example, the "SSI SWC from 2012-04-30 to 2014-04-09 from Mike" sheet's "Workshops" tab is a table of Software Carpentry workshop data. The columns include:

* Workshop code
* Start date
* End date
* Department
* Institution
* Country
* Domain
* Attendees

After downloading this sheet, a Python script needs to be run to create a data file with a table with the total number of attendees for all workshops run at each institution.

* Institution
* Attendees

As another example, the "Questionnaire Analysis" sheet;s "AnalysisByQuestion!C5:N16" tab, cells C5:N16, is a table with open call questionnaire data. The columns include:

* Improve how you manage your project?
* Improve the usability of your software?
* Improve the maintainability of your software?
* etc.

However, the first 7 rows of the table, after the header row, are problematic: 2 are blank lines and 5 contain summary data that is not to be visualised. After downloading this sheet, a Python script needs to be run to remove these 7 problematic rows.

It is an overhead to maintain these Python scripts. It would be easier if the above processing was done within the Google Sheets, by creating additional tables and tabs with the data in a form that can be downloaded and visualised as-is.

---

## How the scripts should access data

Ideally, all the scripts should need to do is specify:

* A Google Sheet ID.
* A tab name.
* An optional range of cells to read e.g. C5:N16 (read the cells bounded by C5 top-left to N16 bottom-right. If not present, then the whole sheet would be read and treated as a single table.

Using Google API notation the tab name and cell range can be represented together e.g. "Chart-InstitutionProjects!A3:B28".

There follows advice on how to structure data in a form easy to download and visualise as-is.

---

## How to structure data to be downloaded

The data to be downloaded should be structured as a table with:

* One or more columns.
* Zero or more contiguous rows of data.
* A header row with a human-readable name for each column.

There must **not** be:

* Columns with personal data i.e. no names, addresses, e-mails, phone numbers etc.
* Intermediate blank rows.
* Intermediate rows/columns aggregating data in other rows/columns e.g. sub-totals.
* Merged cells.

---

## Sums and averages

For calculations relating to groups of rows and columns e.g. the sum of all attendees for all workshops at a specific institution, do not use intermediate rows or columns. Instead, create a summary table with the results of calculations e.g.

* A column for the category by which the individual rows are grouped e.g. Institution.
* A column for the summary calculation e.g. Total Number of Attendees.
* One or more columns with additional information relating to the category or total e.g. an Institution URL.

For example, following sheets and tabs have categories and calculations tables structured as follows:

| Sheet/Tab                 | Category column | Summary calculation column |
| ------------------------- | --------------- | -------------------------- |
| SSI Consultancy Projects sheet | | |
| Chart-FunderEffort | Funder | Effort |
| Chart-Funding | Funder | Projects |
| Chart-InstitutionEffort!A3:B22 | Project (sic) | Total Effort (PMs) |
| Chart-InstitutionProjects!A3:B28 | Project  | Number |
| Chart-Effort!A3:B58 | Project | Effort (PMs) |
|                           |                 |                            |
| Software Used In Research Combined Results sheet | | |
| Unique names for publication | Unique names for counting | How many times reported? |

For the problematic sheet "SSI SWC from 2012-04-30 to 2014-04-09 from Mike" and its "Workshops" tab, mentioned above, we could create a new tab with a summary table with two columns:

* Institution: name each unique institution.
* Attendees: sum of all Attendees for all workshops for each institution.

---

## Redesign existing table, add new table, add new tab?

It is up to you whether you redesign your existing tables, create new tables on new tabs, or within existing tabs. So long as they meet the requirements above they can be downloaded as-is.

---
