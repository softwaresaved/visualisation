"""Comma-separated values (CSV) data utilities.
"""

# Copyright (c) 2016 The University of Edinburgh

import csv
import operator


DELIMITER = ','
QUOTE = '"'
EMPTY_STRING_VALUE = "None"


def count_unique_values(file_name, column):
    """
    Read CSV file and create count occurrences of each unique value in
    column. Values in column are split on "," and each part treated as
    a unique value. For example, given:

        Tool
        ------
        Git
        R
        Git
        Python
        MATLAB
        R

    The output would be:

        {"Git": 2, "MATLAB": 1, "Python": 1, "R": 2}

    :param file_name: CSV file name
    :type file_name: str or unicode
    :param column: Column name
    :type column: str or unicode
    :return: unique column values and frequency counts
    :rtype: dict from str or unicode to int
    """
    counts = {}
    with open(file_name, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file,
                                    delimiter=DELIMITER,
                                    quotechar=QUOTE)
        for row in csv_reader:
            row[column] = row[column].rstrip().rstrip(",")
            names = row[column].split(",")
            for name in names:
                name = name.strip()
                if name not in counts:
                    counts[name] = 1
                else:
                    counts[name] = counts[name] + 1
    sorted_counts = sorted(list(counts.items()), key=operator.itemgetter(1))
    sorted_counts.reverse()
    return sorted_counts


def sum_unique_values(file_name, key_column, value_column):
    """
    Read CSV file and create sum of values in value_column for
    each unique value in key_column. For example, given:

        Tool   | Users
        ------ | -----
        Git    | 3
        R      | 1
        Git    | 4
        Python | 6
        MATLAB | 4
        R      | 3

    The output would be:

        {"Git": 7, "MATLAB": 4, "Python": 6, "R": 4}

    :param file_name: CSV file name
    :type file_name: str or unicode
    :param key_column: Column name
    :type key_column: str or unicode
    :param value_column: Column name
    :type value_column: str or unicode
    :return: unique column values and sums
    :rtype: dict from str or unicode to int
    """
    sums = {}
    with open(file_name, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file,
                                    delimiter=DELIMITER,
                                    quotechar=QUOTE)
        for row in csv_reader:
            row[key_column] = row[key_column].rstrip().rstrip(",")
            if row[key_column] not in sums:
                if row[value_column] != "":
                    sums[row[key_column]] = float(row[value_column])
            else:
                sums[row[key_column]] = sums[row[key_column]] +\
                    float(row[value_column])
    sorted_sums = sorted(list(sums.items()), key=operator.itemgetter(1))
    sorted_sums.reverse()
    return sorted_sums


def save_csv_file(file_name, header, data):
    """
    Save data in two-column CSV file. If any key in data is ""
    then the token "None" is used in the file.

    :param file_name: CSV file name
    :type file_name: str or unicode
    :param header: Header, with two values.
    :type header: list of str or unicode
    :param data: Data
    :rtype: dict from str or unicode to int or float
    """
    with open(file_name, 'w', newline="") as csv_file:
        csv_writer = csv.writer(csv_file,
                                delimiter=DELIMITER,
                                quotechar=QUOTE)
        csv_writer.writerow(header)
        for (name, value) in data:
            if name == "":
                name = EMPTY_STRING_VALUE
            csv_writer.writerow([name, value])
