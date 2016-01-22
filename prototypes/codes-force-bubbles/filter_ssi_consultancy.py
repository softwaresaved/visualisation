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

  - The first three blank lines have been stripped out.
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
      with open(out_file, 'w') as out_file:
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


def remove_lines(in_file, out_file, lines=0):
  """
  Copy a file removing the first N lines from the file.

  :param in_file: Input file name
  :type in_file: str or unicode
  :param out_file: Output file name
  :type out_file: str or unicode
  :param lines: Number of lines to remove
  :type lines: int
  """
  with open(in_file, 'r') as input_file:
      with open(out_file, 'w') as output_file:
          for _ in xrange(lines):
              next(input_file)
          for line in input_file:
              output_file.write(line)


if __name__ == "__main__":
    in_file = sys.argv[1]
    out_file = sys.argv[2]
    tmp = tempfile.mkstemp(suffix=".csv")[1]
    remove_lines(in_file, tmp, 3)
    transform(tmp, out_file)
    os.remove(tmp)
