"""Functions to download data from sheets in Google Sheets workbooks
and save these as CSV files.
"""

# Derived from source code on
#
# https://developers.google.com/sheets/api/quickstart/python
#
# Copyright (C) 2016, Google
# Changes Copyright (C) 2017-2018, The University of Edinburgh.
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

from __future__ import print_function

import yaml

from csv_utils import save_list_as_csv_file

WORKBOOK = "workbook"
""" YAML configuration file key. """
SHEETS = "sheets"
""" YAML configuration file key. """
SHEET = "sheet"
""" YAML configuration file key. """
CELLS = "cells"
""" YAML configuration file key. """
FILE = "file"
""" YAML configuration file key. """


def load_yaml(file):
    """Load YAML configuration file specifying data to download and
    local files to save these in.

       ---
       # YAML file must contain 0 or more entries of form:
       -
         workbook: Google Sheet workbook ID.
         sheets:
         # sheets must contain 0 or more entries of form:
         - sheet: Sheet name.
           cells: Cells, optional, e.g. A1:B38.
           file: File name in which data is to be saved.

    :param file: YAML configuration file.
    :type file: str or unicode
    :return: configuration, a list of dicts, one per sheet.
    :rtype: list(dict)
    :raises: yaml.YAMLError is the file is not valid YAML.
    """
    config = {}
    with open(file, 'r') as stream:
        config = yaml.load(stream)
    return config


def download_workbooks(service, config):
    """Given configuration for zero or more workbooks, download cells
    from sheets in each workbook and save in local files.
    config is expected to be a list of dicts, each of form:

        {
             "workbook": Google Workbook ID,
             "sheets": [
                 {
                     "sheets": Sheet name,
                     "cells": Cells, optional, e.g. A1:B38,
                     "file": File name in which data is to be saved
                 },...
              ]
        }

    Any content not conforming to this structure is ignored.

    :param service: Google service object.
    :type service: googleapiclient.discovery.Resource
    :param config: Workbook configuration.
    :type config: dict
    """
    for workbook_config in config:
        if WORKBOOK not in workbook_config:
            print(WORKBOOK, "not in", workbook_config, "skipping")
            continue
        if SHEETS not in workbook_config:
            print(SHEETS, "not in", workbook_config, "skipping")
            continue
        workbook = workbook_config[WORKBOOK]
        sheets = workbook_config[SHEETS]
        print("Workbook:", workbook)
        download_sheets(service, workbook, sheets)


def download_sheets(service, workbook, sheets_config):
    """Given configuration a workbook, download cells from sheets in
    the workbook and save in local files.
    sheets_config is expected to be a list of dicts, each of form:

        {
            "sheet": Sheet name,
            "cells": Cells, optional, e.g. A1:B38,
            "file": File name in which data is to be saved
        }

    Any content not conforming to this structure is ignored.

    Any problems in downloading are printed, but execution will
    continue onto the next sheet.

    :param service: Google service object.
    :type service: googleapiclient.discovery.Resource
    :param workbook: Workbook ID.
    :type workbook: str or unicode
    :param config: Sheets configuration.
    :type config: dict
    """
    for sheet_config in sheets_config:
        if SHEET not in sheet_config:
            print(SHEET, "not in", sheet_config, "skipping")
            continue
        if FILE not in sheet_config:
            print(FILE, "not in", sheet_config, "skipping")
            continue
        sheet = sheet_config[SHEET]
        if CELLS in sheet_config:
            cells = sheet_config[CELLS]
        else:
            cells = None
        file = sheet_config[FILE]
        print("Downloading:", workbook, sheet, cells, file)
        try:
            data = download_cells(service, workbook, sheet, cells)
            save_list_as_csv_file(data, file)
        except Exception as exc:
            print("Problem with accessing and saving data", exc)


def download_cells(service, workbook, sheet, cells):
    """Dowload cells from a sheet of a workbook.

    :param service: Google service object.
    :type service: googleapiclient.discovery.Resource
    :param workbook: Workbook ID.
    :type workbook: str or unicode
    :param sheet: Sheet name e.g. "Data".
    :type sheet: str or unicode
    :param cells: Cells e.g. "A2:L7" or None if all cells
    are to be downloaded.
    :type cells: str or unicode
    :return: Cells data.
    :rtype: list of list of str or unicode
    """
    if cells is None:
        sheet_and_cells = sheet
    else:
        sheet_and_cells = sheet + "!" + cells
    sheet_metadata = service.spreadsheets().get(
        spreadsheetId=workbook).execute()
    print("Workbook file name:", sheet_metadata["properties"]["title"])
    result = service.spreadsheets().values().get(
        spreadsheetId=workbook, range=sheet_and_cells).execute()
    values = result.get("values", [])
    return values
