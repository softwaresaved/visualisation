"""Get a Google Sheet as comma-separated values and save in a file.

Usage:

   $ python get_sheet.py SHEET_ID TAB_ID FILE_NAME

For example, to get a tab in a sheet
https://docs.google.com/spreadsheets/d/a1b2c3d4/export?gid=7:

   $ python get_sheet.py a1b2c3d4 7 data.csv
"""

# Copyright (c) 2016-2018 The University of Edinburgh
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
from web_utils import download_google_sheet


if __name__ == "__main__":
    sheet = sys.argv[1]
    tab = sys.argv[2]
    file_name = sys.argv[3]
    download_google_sheet(file_name, sheet, tab)
