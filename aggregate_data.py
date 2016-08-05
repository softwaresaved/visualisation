"""Summarise CSV data.

Usage::

Read CSV file, count number of occurrences of unique values in KEY_COLUMN
and output 2 column CSV file with values and counts. Column headers 
are "OUT_KEY_COLUMN, OUT_COUNT_COLUMN".

   $ python aggregate_data.py count IN_FILE KEY_COLUMN OUT_KEY_COLUMN OUT_COUNT_COLUMN OUT_FILE

Read CSV file, sum together all values in VALUE_COLUMN whose rows
have the same KEY_COLUMN value, and output 2 column CSV file with
values and counts. Column headers are "OUT_KEY_COLUMN, OUT_COUNT_COLUMN".

   $ python aggregate_data.py sum IN_FILE KEY_COLUMN VALUE_COLUMN OUT_KEY_COLUMN OUT_COUNT_COLUMN OUT_FILE
"""

# Copyright (c) 2016 The University of Edinburgh

import csv
import operator
import os
import sys
import tempfile

DELIMITER = ','
QUOTE = '"'

def count_occurrences(in_file, column):
  """
  Read CSV file in_file and create count of occurrences of each unique
  value in column. Values in column are split on "," and each
  constituent treated as a unique value.

  :param in_file: Input file name
  :type in_file: str or unicode
  :param column: Column name
  :type column: str or unicode
  :return: unique column values and frequency counts
  :rtype: dict
  """
  occurrences = {}
  with open(in_file, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file,
                                delimiter=DELIMITER,
                                quotechar=QUOTE)
    for row in csv_reader:
      row[column] = row[column].rstrip().rstrip(",")
      names = row[column].split(",")
      for name in names:
        name = name.strip()
        if name not in occurrences:
          occurrences[name] = 1
        else:
          occurrences[name] = occurrences[name] + 1
  sorted_occurrences = sorted(occurrences.items(), key=operator.itemgetter(1))
  sorted_occurrences.reverse()
  return sorted_occurrences


def sum_occurrences(in_file, key_column, value_column):
  """
  Read CSV file in_file and create sum of values in value_column for
  each unique value in key_column.

  :param in_file: Input file name
  :type in_file: str or unicode
  :param key_column: Column name
  :type key_column: str or unicode
  :param value_column: Column name
  :type value_column: str or unicode
  :return: unique column values and frequency counts
  :rtype: dict
  """
  occurrences = {}
  with open(in_file, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file,
                                delimiter=DELIMITER,
                                quotechar=QUOTE)
    for row in csv_reader:
      row[key_column] = row[key_column].rstrip().rstrip(",")
      if row[key_column] not in occurrences:
          occurrences[row[key_column]] = float(row[value_column])
      else:
        occurrences[row[key_column]] = occurrences[row[key_column]] + float(row[value_column])

  sorted_occurrences = sorted(occurrences.items(), key=operator.itemgetter(1))
  sorted_occurrences.reverse()
  return sorted_occurrences


def save_csv(out_file, header, data):
  """
  Save data in two-column CSV file out_file.

  :param out_file: Output file name
  :type out_file: str or unicode
  :param header: Header, with two values.
  :type header: list of str or unicode
  :param data: Data
  :type data: dict
  """
  with open(out_file, 'w') as csv_out_file:
    csv_writer = csv.writer(csv_out_file,
                            delimiter=DELIMITER,
                            quotechar=QUOTE)
    # Replace with 2.7 writeheaderr
    csv_writer.writerow(header)
    for (name, value) in data:
      if (name == ""):
        name = "None"
      csv_writer.writerow([name, value])


if __name__ == "__main__":
    aggregate_type = sys.argv[1]
    in_file = sys.argv[2]
    key_column = sys.argv[3]
    if (aggregate_type == "count"):
      out_key_column = sys.argv[4]
      out_count_column = sys.argv[5]
      out_file = sys.argv[6]
      data = count_occurrences(in_file, key_column)
      header = [out_key_column, out_count_column]
      save_csv(out_file, header, data)
    elif (aggregate_type == "sum"):
      value_column = sys.argv[4]
      out_key_column = sys.argv[5]
      out_count_column = sys.argv[6]
      out_file = sys.argv[7]
      data = sum_occurrences(in_file, key_column, value_column)
      header = [out_key_column, out_count_column]
    else:
        print("Unrecognised command");
        exit(1)
    save_csv(out_file, header, data)
