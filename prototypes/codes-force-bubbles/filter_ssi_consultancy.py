# Python 2.6.6+
# Usage:
# $ python filter_ssi_consultancy.py data/ssi-consultancy.csv 
#    data/ssi-consultancy-filtered.csv

import csv
import sys

DELIMITER = ','
QUOTE = '"'

in_file = sys.argv[1]
out_file = sys.argv[2]

header = ["Project Name", "Primary Funder", "Other Funders", "Group(s)", "Institution", "Type", "PMs", "Research Field"]
with open(in_file, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=DELIMITER, quotechar=QUOTE)
    with open(out_file, 'w') as out_file:
        csv_writer = csv.DictWriter(out_file, 
                                    fieldnames=header,
                                    extrasaction="ignore",
                                    delimiter=DELIMITER,
                                    quotechar=QUOTE)
        # Replace with 2.7 writeheader
        csv_writer.writerow(dict(zip(header, header)))
        for row in csv_reader:
            row["Research Field"] = row["Research Field"].rstrip().rstrip(",")
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
