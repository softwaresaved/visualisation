"""Utilities for downloading data from URLs and Google Sheets.
"""

# Copyright (c) 2016 The University of Edinburgh

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
    print(sheet_url)
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
    open(file_name, 'wb').write(sheet_content)
