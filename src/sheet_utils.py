"""Utilities for accessing Google Sheets.

Derived from source code on

https://developers.google.com/sheets/api/quickstart/python

Copyright (C) 2016, Google
Changes Copyright (C) 2017, The University of Edinburgh.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""

from __future__ import print_function

import os

import httplib2

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage


USER_CREDENTIAL_DIR = ".credentials"
USER_CREDENTIAL_FILE = "sheets.googleapis.com-python-quickstart.json"

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = "https://www.googleapis.com/auth/spreadsheets.readonly"
CLIENT_SECRET_FILE = "client_secret.json"
APPLICATION_NAME = "Google Sheets API Python Quickstart"


try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None


def get_credentials():
    """Gets valid user credentials from storage.
    If nothing has been stored, or if the stored credentials are
    invalid, the OAuth2 flow is completed to obtain the new
    credentials.

    :return: credentials, the obtained credential.
    :rtype: oauth2client.client.OAuth2Credentials
    """
    home_dir = os.path.expanduser("~")
    credential_dir = os.path.join(home_dir, USER_CREDENTIAL_DIR)
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   USER_CREDENTIAL_FILE)
    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print("Storing credentials to " + credential_path)
    return credentials


def download_sheet(sheet_id, tab_and_range):
    """
    Get Google Sheet data.

    :param sheet_id: Sheet ID
    :type sheet_id: str or unicode
    :param tab_and_range: Sheet tab and (optional) range e.g.
    "Workshops" or "Workshops!A1:B12"
    :type sheet_id: str or unicode
    :return: Sheet data
    :rtype: list of list of str or unicode
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discovery_url = ("https://sheets.googleapis.com/$discovery/rest?")
    service = discovery.build("sheets", "v4", http=http,
                              discoveryServiceUrl=discovery_url)
    result = service.spreadsheets().values().get(
        spreadsheetId=sheet_id, range=tab_and_range).execute()
    values = result.get("values", [])
    return values
