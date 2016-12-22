"""Transform SSI consultancy spreadsheet.

Usage::

   $ python transform_consultancy_data.py IN_FILE OUT_FILE

For IN_FILE and OUT_FILE, see definition of filter.
"""

# Copyright (c) 2016 The University of Edinburgh

import csv
import os
import sys
import tempfile

DELIMITER = ','
QUOTE = '"'
OUT_HEADER = ["Project Name", "Primary Funder", "Other Funders",
              "Group(s)", "Institution", "Type", "PMs",
              "Research Field"]

def transform(in_file, out_file):
  """
  Transform SSI consultancy spreadsheet. Read in the spreadsheet as
  comma-separated values. It is assumed that:

  - The spreadsheet has a header.
  - The header fields include: ["Project Name", "Funder(s)",
  - "Group(s)", "Institution", "Type", "PMs", "Research Field"]

  Read this spreadsheet and output a new spreadsheet of
  comma-separated values. This spreadsheet has:

  - A header ["Project Name", "Primary Funder", "Other Funders",
    "Group(s)", "Institution", "Type", "PMs", "Research Field"].
  - Rows with the above columns, all copied from the original
    spreadsheet.
  - "Primary Funder" and "Other Funders" fields are formed by
    splitting the "Funder(s)" column on its first comma
    e.g. a "Funder(s)" value of "EPSRC,MRC,EU" is replaced by a
    "Primary Funder" value of "EPSRC" and an "Other Funders" value of
    "MRC,EU".

  :param in_file: Input file name
  :type in_file: str or unicode
  :param out_file: Output file name
  :type out_file: str or unicode
  """
  with open(in_file, 'r') as csv_file:
      csv_reader = csv.DictReader(csv_file,
                                  delimiter=DELIMITER,
                                  quotechar=QUOTE)
      with open(out_file, 'w', newline="") as out_file:
          csv_writer = csv.DictWriter(out_file,
                                      fieldnames=OUT_HEADER,
                                      extrasaction="ignore",
                                      delimiter=DELIMITER,
                                      quotechar=QUOTE)
          # Replace with 2.7 writeheaderr
          csv_writer.writerow(dict(zip(OUT_HEADER, OUT_HEADER)))
          for row in csv_reader:
              row["Research Field"] = \
                  row["Research Field"].rstrip().rstrip(",")
              funders = row["Funder(s)"]
              del(row["Funder(s)"])
              funders = funders.split(",")
              # Trim white-space.
              funders = [item.strip() for item in funders]
              # Remove ''.
              funders[:] = (value for value in funders if value != '')
              if funders == []:
                  row["Primary Funder"] = "Unknown"
                  row["Other Funders"] = ""
              else:
                  row["Primary Funder"] = funders[0]
                  row["Other Funders"] = ','.join(funders[1:])
                  csv_writer.writerow(row)


if __name__ == "__main__":
    in_file = sys.argv[1]
    out_file = sys.argv[2]
    transform(in_file, out_file)
