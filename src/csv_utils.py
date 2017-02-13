"""Comma-separated values (CSV) data utilities.
"""

# Copyright (c) 2016 The University of Edinburgh

import csv
import operator


DELIMITER = ','
QUOTE = '"'
EMPTY_STRING_VALUE = "None"
UNKNOWN_STRING_VALUE = "Unknown"


def count_unique_values(csv_data, column):
    """
    Read CSV data and count occurrences of each unique value in a
    column. Values in column are split on "," and each part treated as
    a unique value. For example, given:

        [
            {"Tool":"Git", "Users":3},
            {"Tool":"R", "Users":1},
            {"Tool":"Git", "Users":4},
            {"Tool":"Python", "Users":6},
            {"Tool":"MATLAB", "Users":4},
            {"Tool":"R", "Users":3}
        ]

    with column="Tool", the value returned is:

        {"Git": 2, "MATLAB": 1, "Python": 1, "R": 2}

    :param csv_data: CSV data
    :type csv_data: list of dict
    :param column: Column name
    :type column: str or unicode
    :return: unique column values and frequency counts
    :rtype: dict from str or unicode to int
    """
    counts = {}
    for row in csv_data:
        row[column] = row[column].rstrip().rstrip(",")
        names = row[column].split(",")
        for name in names:
            name = name.strip()
            if name not in counts:
                counts[name] = 1
            else:
                counts[name] = counts[name] + 1
    return counts


def sum_unique_values(csv_data, key_column, value_column):
    """
    Read CSV data and create sum of values in value_column for
    each unique value in key_column. For example, given:

        [
            {"Tool":"Git", "Users":3},
            {"Tool":"R", "Users":1},
            {"Tool":"Git", "Users":4},
            {"Tool":"Python", "Users":6},
            {"Tool":"MATLAB", "Users":4},
            {"Tool":"R", "Users":3}
        ]

    with key_column="Tool" and value_column="Users", the value
    returned is:

        {"Git": 7, "MATLAB": 4, "Python": 6, "R": 4}

    :param csv_data: CSV data
    :type csv_data: list of dict
    :param key_column: Column name
    :type key_column: str or unicode
    :param value_column: Column name
    :type value_column: str or unicode
    :return: unique column values and sums
    :rtype: dict from str or unicode to int
    """
    sums = {}
    for row in csv_data:
        row[key_column] = row[key_column].rstrip().rstrip(",")
        if row[key_column] not in sums:
            if row[value_column] != "":
                sums[row[key_column]] = float(row[value_column])
        else:
            sums[row[key_column]] = sums[row[key_column]] +\
                float(row[value_column])
    return sums


def split_csv_column(columns, csv_data, column, column_a, column_b):
    """
    Read CSV data and, for a given column with comma-separated values,
    split it into two columns, where the first column contains the first
    comma-separated value and the second column contains the rest of
    the comma-separated values. If the column has no values then the
    two columns have values "Unknown".

    :param columns: CSV column names
    :type columns: list of str or unicode
    :param csv_data: CSV data
    :type csv_data: list of dict
    :param column: Column name
    :type column: str or unicode
    :param column_a: Output column name
    :type column_a: str or unicode
    :param column_b: Output column name
    :type column_b: str or unicode
    :return: (column names, CSV rows)
    :rtype: (list of str or unicode, list of dict from str or unicode)
    """
    filtered_csv_data = []
    index = columns.index(column)
    columns.remove(column)
    columns.insert(index, column_b)
    columns.insert(index, column_a)
    for row in csv_data:
        value = row[column]
        del row[column]
        values = value.split(",")
        values = [value.strip() for value in values]
        values[:] = (value for value in values if value != '')
        if values == []:
            row[column_a] = UNKNOWN_STRING_VALUE
            row[column_b] = UNKNOWN_STRING_VALUE
        else:
            row[column_a] = values[0]
            row[column_b] = ','.join(values[1:])
        filtered_csv_data.append(row)
    return (columns, filtered_csv_data)


def load_csv_file(file_name):
    """
    Load CSV data from a CSV file. For example, given:

        Tool   | Users
        ------ | -----
        Git    | 3
        R      | 1
        Git    | 4
        Python | 6
        MATLAB | 4
        R      | 3

    The value returned is:

        [
            {"Tool":"Git", "Users":3},
            {"Tool":"R", "Users":1},
            {"Tool":"Git", "Users":4},
            {"Tool":"Python", "Users":6},
            {"Tool":"MATLAB", "Users":4},
            {"Tool":"R", "Users":3}
        ]

    :param file_name: CSV file name
    :type file_name: str or unicode
    :return: (column names, CSV rows)
    :rtype: (list of str or unicode, list of dict from str or unicode)
    """
    with open(file_name, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file,
                                    delimiter=DELIMITER,
                                    quotechar=QUOTE)
        columns = csv_reader.fieldnames
        rows = [row for row in csv_reader]
    return (columns, rows)


def save_csv_file(columns, csv_data, file_name):
    """
    Save CSV data to a CSV file.

    :param columns: CSV column names
    :type columns: list of str or unicode
    :param csv_data: CSV rows
    :type csv_data: list of dict from str or unicode
    :param file_name: CSV file name
    :type file_name: str or unicode
    """
    print(("Saving: " + file_name))
    with open(file_name, 'w', newline="") as csv_file:
        csv_writer = csv.DictWriter(csv_file,
                                    fieldnames=columns,
                                    extrasaction="ignore",
                                    delimiter=DELIMITER,
                                    quotechar=QUOTE)
        csv_writer.writerow(dict(list(zip(columns, columns))))
        for row in csv_data:
            csv_writer.writerow(row)


def save_dict_as_csv_file(file_name, key_header, value_header, data):
    """
    Save data in two-column CSV file. If any key in data is ""
    then the token "None" is used in the file.

    :param file_name: CSV file name
    :type file_name: str or unicode
    :param key_header: Header for keys.
    :type key_header: list of str or unicode
    :param value_header: Header for values.
    :type value_header: list of str or unicode
    :param data: Data
    :type data: dict from str or unicode to int or float
    """
    print(("Saving: " + file_name))
    sorted_data = sorted(list(data.items()), key=operator.itemgetter(1))
    sorted_data.reverse()
    with open(file_name, 'w', newline="") as csv_file:
        csv_writer = csv.writer(csv_file,
                                delimiter=DELIMITER,
                                quotechar=QUOTE)
        csv_writer.writerow([key_header, value_header])
        for (name, value) in sorted_data:
            if name == "":
                name = EMPTY_STRING_VALUE
            csv_writer.writerow([name, value])


def save_list_as_csv_file(csv_data, file_name):
    """
    Save CSV data to a CSV file.

    :param csv_data: CSV rows
    :type csv_data: list of lists of str or unicode
    :param file_name: CSV file name
    :type file_name: str or unicode
    """
    print(("Saving: " + file_name))
    with open(file_name, 'w', newline="") as csv_file:
        csv_writer = csv.writer(csv_file,
                                delimiter=DELIMITER,
                                quotechar=QUOTE)
        for row in csv_data:
            csv_writer.writerow(row)


def tail(file_name, tail_file_name, num_lines):
    """
    Copy a file to another file, ignoring the first N lines.

    :param file_name: file name
    :type file_name: str or unicode
    :param tail_file_name: file name
    :type tail_file_name: str or unicode
    :param num_lines: Number of lines to ignore
    :type num_lines: int
    """
    print(("Saving: " + tail_file_name))
    with open(file_name, 'r') as in_file:
        with open(tail_file_name, 'w', newline="") as out_file:
            for _ in range(num_lines):
                next(in_file)
            for line in in_file:
                out_file.write(line)
