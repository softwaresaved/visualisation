"""Transform spreadsheet.

Usage::

   $ python aggregate_data.py IN_FILE OUT_FILE COLUMN [VALUE_COLUMN]
"""

# TODO if VALUE_COLUMN is provided then sum the number of values
# in this column (e.g. for SWC attendees by location)

# Copyright (c) 2016 The University of Edinburgh

import csv
import os
import sys
import tempfile

DELIMITER = ','
QUOTE = '"'

def transform(in_file, out_file, column):
  """
  Transform spreadsheet. Read in the spreadsheet as
  comma-separated values. It is assumed that:

  - The first three blank lines have been stripped out.
  - The spreadsheet has a header.

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
  entries = {}
  header = [column, "Count"]
  with open(in_file, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file,
                                delimiter=DELIMITER,
                                quotechar=QUOTE)
    for row in csv_reader:
      row[column] = row[column].rstrip().rstrip(",")
      if row[column] not in entries:
        entries[row[column]] = 1
      else:
        entries[row[column]] = entries[row[column]] + 1
  with open(out_file, 'w') as csv_out_file:
    csv_writer = csv.writer(csv_out_file,
                            delimiter=DELIMITER,
                            quotechar=QUOTE)
    # Replace with 2.7 writeheaderr
    csv_writer.writerow(header)
    for name in entries:
      value = entries[name]
      if (name == ""):
        name = "None"
      csv_writer.writerow([name, value])

if __name__ == "__main__":
    in_file = sys.argv[1]
    out_file = sys.argv[2]
    column = sys.argv[3]
    transform(in_file, out_file, column)
