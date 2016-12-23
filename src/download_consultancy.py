"""Download consultancy sheet Projects tab and filter to sum
number of attendees by institution.
"""

# Copyright (c) 2016 The University of Edinburgh

import os
import sys

from csv_utils import load_csv_file
from csv_utils import save_csv_file
from csv_utils import save_dict_as_csv_file
from csv_utils import split_csv_column
from csv_utils import sum_unique_values
from web_utils import download_google_sheet


if __name__ == "__main__":
    sheet = sys.argv[1]
    tab = 0
    file_name = "tmp.csv"
    download_google_sheet(file_name, sheet, tab)
    # Trim off first three lines
    trimmed_file_name = "tmp_trimmed.csv"
    with open(file_name, 'r') as in_file:
        with open(trimmed_file_name, 'w', newline="") as out_file:
            for _ in range(3):
                next(in_file)
            for line in in_file:
                out_file.write(line)
    os.remove(file_name)
    columns, data = load_csv_file(trimmed_file_name)
    # Split off primary funder into new column.
    columns, data = split_csv_column(
        columns,
        data,
        "Funder(s)",
        "Primary Funder",
        "Other Funders")
    projected_columns = [
        "Project Name",
        "Primary Funder",
        "Other Funders",
        "Group(s)",
        "Institution",
        "Type",
        "PMs",
        "Research Field"]
    save_csv_file(projected_columns,
                  data,
                  "data/sheets/filtered/consultancy.csv")
    os.remove(trimmed_file_name)
    # Calculate effort per project.
    effort_data = sum_unique_values(data, "Project Name", "PMs")
    save_dict_as_csv_file("data/sheets/filtered/project_effort.csv",
                          "Project",
                          "PMs",
                          effort_data)
