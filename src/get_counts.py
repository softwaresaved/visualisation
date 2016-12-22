"""Read CSV file, summarise counts of unique values in a column and
and save values and counts in a new CSV file.

Usage:

   $ python get_counts.py IN_FILE IN_VALUE_COLUMN \
                          OUT_VALUE_COLUMN OUT_COUNT_COLUMN \
                          OUT_FILE

where:

    * IN_FILE: CSV file name
    * IN_VALUE_COLUMN: name of column to be counted in IN_FILE
    * OUT_VALUE_COLUMN: name for values column in OUT_FILE
    * OUT_COUNT_COLUMN: name for counts column in OUT_FILE
    * OUT_FILE: output file name

For example, given input.csv:

        Tool
        ------
        Git
        R
        Git
        Python
        MATLAB
        R

running:

   $ python get_counts.py input.csv Tool Tool Frequency output.csv

would produce output.csv:

        Tool,Frequency
        Git,2
        Python,1
        MATLAB,1
        R,2
"""

# Copyright (c) 2016 The University of Edinburgh


import sys
from csv_utils import count_unique_values
from csv_utils import load_csv_file
from csv_utils import save_dict_as_csv_file


if __name__ == "__main__":
    in_file = sys.argv[1]
    in_value_column = sys.argv[2]
    out_value_column = sys.argv[3]
    out_count_column = sys.argv[4]
    out_file = sys.argv[5]
    (_, data) = load_csv_file(in_file)
    filtered_data = count_unique_values(data, in_value_column)
    save_dict_as_csv_file(out_file,
                          out_value_column,
                          out_count_column,
                          filtered_data)
