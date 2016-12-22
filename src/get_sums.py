"""Read CSV file, and for each unique value in one column, calculate
the sum of corresponding values in another column, and save values and
sums in a new CSV file.

Usage:

   $ python get_counts.py IN_FILE IN_KEY_COLUMN IN_VALUE_COLUMN \
                          OUT_KEY_COLUMN OUT_SUM_COLUMN \
                          OUT_FILE

where:

    * IN_FILE: CSV file name
    * IN_KEY_COLUMN: name of column for which sums are to be calculated
    * IN_VALUE_COLUMN: name of column whose values are to be summed
    * OUT_KEY_COLUMN: name for key column in OUT_FILE
    * OUT_SUM_COLUMN: name for sum column in OUT_FILE
    * OUT_FILE: output file name

For example, given input.csv:

        Tool   | Users
        ------ | -----
        Git    | 3
        R      | 1
        Git    | 4
        Python | 6
        MATLAB | 4
        R      | 3

Running:

   $ python get_counts.py input.csv Tool Users Tool TotalUsers output.csv

would produce output.csv:

        Tool,TotalUsers
        Git,7
        Python,6
        MATLAB,4
        R,4
"""

# Copyright (c) 2016 The University of Edinburgh


import sys
from csv_utils import load_csv_file
from csv_utils import save_dict_as_csv_file
from csv_utils import sum_unique_values


if __name__ == "__main__":
    in_file = sys.argv[1]
    in_key_column = sys.argv[2]
    in_value_column = sys.argv[3]
    out_key_column = sys.argv[4]
    out_sum_column = sys.argv[5]
    out_file = sys.argv[6]
    (_, data) = load_csv_file(in_file)
    filtered_data = sum_unique_values(data, in_key_column, in_value_column)
    save_dict_as_csv_file(out_file,
                          out_key_column,
                          out_sum_column,
                          filtered_data)
