"""Program to download data from files in GitHub repositories and save
these locally.

    usage: download_repository_files.py [-h]
        [--token GITHUB_TOKEN]
        --repositories REPOSITORIES_YAML_FILE

A GitHub personal token is only required if downloading files from
private repositories. As an alternative to the command-line flag,
a GITHUB_TOKEN environment variable can be set.
"""

# Copyright 2018 The University of Edinburgh
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
import os


from github_utils import download_repositories
from github_utils import GITHUB_TOKEN
from yaml_utils import load_yaml

if __name__ == "__main__":
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--token', required=False, type=str)
    parser.add_argument('--repositories', required=True, type=str)
    flags = parser.parse_args()
    token = flags.token
    if token is None and GITHUB_TOKEN in os.environ:
        token = os.environ[GITHUB_TOKEN]
    config_file = flags.repositories
    config = load_yaml(config_file)
    download_repositories(config, token)
