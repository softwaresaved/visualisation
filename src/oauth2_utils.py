"""Google APIs and OAuth2 constants and functions."""

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

import os

from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

USER_CREDENTIAL_DIR = ".credentials"
""" User credential directory. """

USER_CREDENTIAL_FILE = "sheets.googleapis.com-python-quickstart.json"
""" User credential file name. """

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json

SCOPES = "https://www.googleapis.com/auth/spreadsheets.readonly"
""" Google APIs OAuth 2.0 scope. """
CLIENT_SECRET_FILE = "client_secret.json"
""" User's client secret file. """
APPLICATION_NAME = "Google Sheets API Python Quickstart"
""" Application name. """


def get_credentials(flags):
    """Gets valid user credentials from ~/USER_CREDENTIAL_DIR.

    If there no credentials, or if the credentials are invalid, an
    OAuth2 workflow is completed to obtain new credentials.

    :param flags: OAuth2 flags.
    :type flags: argparse.Namespace
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
        else:  # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print("Storing credentials to " + credential_path)
    return credentials
