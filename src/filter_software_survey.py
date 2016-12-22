"""Filter software survey data to count frequencies of software and
operating systems.
"""

# Copyright (c) 2016 The University of Edinburgh

from csv_utils import count_unique_values
from csv_utils import load_csv_file
from csv_utils import save_dict_as_csv_file


if __name__ == "__main__":
    _, data = load_csv_file("data/static/raw/The use of software in research (Responses) Cleaned For All Hands Hack - Form Responses 1.csv")
    sw_data = count_unique_values(
        data,
        "Question 11: Please provide the name(s) of the main research software you use.")
    save_dict_as_csv_file(
        "data/static/filtered/SoftwareSurvey2014Software.csv",
        "Research Software",
        "Count",
        sw_data)
    os_data = count_unique_values(
        data,
        "Extra question 4: What is your preferred Operating System?")
    save_dict_as_csv_file("data/static/filtered/SoftwareSurvey2014OS.csv",
                          "Operating System",
                          "Count",
                          os_data)
