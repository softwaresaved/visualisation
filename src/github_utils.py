"""Functions to download data from files in GitHub repositories and
save these locally.
"""

# Copyright (c) 2018, The University of Edinburgh.
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

import requests

GITHUB_TOKEN = "GITHUB_TOKEN"
""" Environment variable. """
USER = "user"
""" YAML configuration file key. """
REPOSITORY = "repository"
""" YAML configuration file key. """
FILES = "files"
""" YAML configuration file key. """
FILE = "file"
""" YAML configuration file key. """
LOCAL_FILE = "local_file"
""" YAML configuration file key. """


def download_repositories(config, token=None):
    """Given configuration for zero or more repositories, download
    files from each repository and save in local files.
    config is expected to be a list of dicts, each of form:

        {
             "user": GitHub user name.
             "repository": GitHub repository.
             "files": [
                 {
                     "file": File name,
                     "local_file": File name in which data is to be saved
                 },...
              ]
        }

    Any content not conforming to this structure is ignored.

    :param config: Repository configuration.
    :type config: dict
    :param token: GitHub personal token.
    :type token: str or unicode
    """
    for repository_config in config:
        if USER not in repository_config:
            print(USER, "not in", repository_config, "skipping")
            continue
        if REPOSITORY not in repository_config:
            print(REPOSITORY, "not in", repository_config, "skipping")
            continue
        if FILES not in repository_config:
            print(FILES, "not in", repository_config, "skipping")
            continue
        user = repository_config[USER]
        repository = repository_config[REPOSITORY]
        files = repository_config[FILES]
        print("Repository:", user + "/" + repository)
        download_files(user, repository, files, token)


def download_files(user, repository, files_config, token=None):
    """Given configuration for a repository, download
    files from the repository and save in local files.
    config is expected to be a list of dicts, each of form:

        {
            "file": File name,
            "local_file": File name in which data is to be saved
        }

    Any content not conforming to this structure is ignored.

    Any problems in downloading are printed, but execution will
    continue onto the next file.

    :param user: GitHub user name.
    :type user: str or unicode
    :param repository: GitHub repository name.
    :type repository: str or unicode
    :param files_config: Files configuration.
    :type files_config: dict
    :param token: GitHub personal token.
    :type token: str or unicode
    """
    for file_config in files_config:
        if FILE not in file_config:
            print(FILE, "not in", file_config, "skipping")
            continue
        if LOCAL_FILE not in file_config:
            print(LOCAL_FILE, "not in", file_config, "skipping")
            continue
        file = file_config[FILE]
        local_file = file_config[LOCAL_FILE]
        try:
            data = download_file(user, repository, file, "master", token)
            with open(local_file, "w") as local_file:
                local_file.write(data)
        except Exception as exc:
            print("Problem with accessing and saving data", exc)


def download_file(user, repository, file, branch="master", token=None):
    """Download a file from GitHub.

    :param user: GitHub user name.
    :type user: str or unicode
    :param repository: GitHub repository name.
    :type repository: str or unicode
    :param branch: Repository branch name.
    :type branch: str or unicode
    :param config: Files configuration.
    :type config: dict
    :param token: GitHub personal token.
    :type token: str or unicode
    :return: File data.
    :rtype: str or unicode
    """
    url = "https://raw.githubusercontent.com"
    full_url = "/".join([url, user, repository, branch, file])
    print("Downloading:", full_url)
    headers = {}
    if token is not None:
        headers["Authorization"] = "token " + token
    headers["Accept"] = "application/vnd.github.v3.raw"
    response = requests.get(full_url, headers=headers)
    assert response.status_code == requests.codes.ok,\
        "Response was " + str(response.status_code)
    return response.text
