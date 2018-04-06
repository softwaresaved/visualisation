"""Utilities for downloading data from URLs and Google Sheets.
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

import requests


GOOGLE_SHEET_URL = \
    "https://docs.google.com/spreadsheets/d/%s/export?gid=%s&format=%s"


def get_url(url):
    """
    Issue HTTP GET at URL and return response. Uses an assert to check
    response is 200.

    :param url: URL
    :type url: str or unicode
    :return: response
    :rtype: bytes
    """
    print("HTTP GET:")
    print(url)
    response = requests.get(url)
    # pylint: disable=E1103
    assert response.status_code == requests.codes.ok
    # pylint: enable=E1103
    return response.content


def get_google_sheet(sheet,
                     tab=0,
                     sheet_format="csv"):
    """
    Issue HTTP GET at Google sheet URL and return response.

    :param sheet: sheet ID
    :type sheet: str or unicode
    :param tab: tab index in sheet
    :type tab: int
    :param sheet_format: response format
    :type sheet_format: str or unicode
    :return: response
    :rtype: bytes
    """
    sheet_url = GOOGLE_SHEET_URL % (sheet, tab, sheet_format)
    return get_url(sheet_url)


def download_google_sheet(file_name, sheet, tab, sheet_format="csv"):
    """
    Issue HTTP GET at Google sheet URL and save response in a file.

    :param file_name: file name
    :type file_name: str or unicode
    :param sheet: sheet ID
    :type sheet: str or unicode
    :param tab: tab index in sheet
    :type tab: int
    :param sheet_format: response format
    :type sheet_format: str or unicode
    :return: response
    :rtype: bytes
    """
    sheet_content = get_google_sheet(sheet, tab, sheet_format)
    print("Saving:", file_name)
    open(file_name, 'wb').write(sheet_content)
