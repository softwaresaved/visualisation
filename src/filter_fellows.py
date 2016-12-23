"""Filter fellows data to count number of fellows by institution.
"""

# Copyright (c) 2016 The University of Edinburgh

from csv_utils import count_unique_values
from csv_utils import load_csv_file
from csv_utils import save_dict_as_csv_file

if __name__ == "__main__":
    _, data = load_csv_file("data/static/raw/fellows_institutions.csv")
    fellows_data = count_unique_values(data, "Home institution")
    save_dict_as_csv_file("data/static/filtered/fellows_institutions.csv",
                          "Institution",
                          "Count",
                          fellows_data)
