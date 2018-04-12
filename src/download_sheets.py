"""Program to download data from sheets in Google Sheets workbooks and
save these as CSV files.

    usage: download_sheets.py [-h]
        [--auth_host_name AUTH_HOST_NAME]
        [--noauth_local_webserver]
        [--auth_host_port [AUTH_HOST_PORT [AUTH_HOST_PORT ...]]]
        [--logging_level {DEBUG,INFO,WARNI NG,ERROR,CRITICAL}]
        --sheets SHEETS_YAML_FILE
"""

# Copyright 2016-2018 The University of Edinburgh
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

import argparse

from oauth2client import tools

from oauth2_utils import get_credentials
from oauth2_utils import get_google_service
from sheet_utils import download_workbooks
from yaml_utils import load_yaml

if __name__ == "__main__":
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--sheets', required=True, type=str)
    flags = argparse.ArgumentParser(
        parents=[tools.argparser, parser]).parse_args()
    config_file = flags.sheets
    config = load_yaml(config_file)
    credentials = get_credentials(flags)
    service = get_google_service(credentials)
    download_workbooks(service, config)
