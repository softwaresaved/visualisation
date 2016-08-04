#!/usr/bin/env python
# encoding: utf-8

"""
    Using nltk requires to download separately the pickle files.
    This script check if the required module are available and updated
    If not launch the install or update them.
    Also, set up the OS environment variable to a local folder to ensure
    that the file are installed there instead of the default installation
    folder. This to keep all the needed file into the same folder.
    This nltk modules are needed for the include/topicTranformation.py
"""

import os
from include.configParser import ConfigParserPerso as configParser


def get_config():
    """ """
    config_value = configParser().read_config('./config.ini')
    return config_value


def import_nltk(var, value):
    """ Change the os variable and then return the module
        If the module is imported before the change of the env_var, the change
        of the var is not applied
    """
    init_env_var(var, value)
    import nltk as nltk
    # Create it global but not sure is needed
    global nltk


def init_env_var(var, value):
    """ Init an environment variable """
    os.environ[var.upper()] = str(value)


def dl_pickles(l):
    """ Download the pickle file name input as list or string """
    if isinstance(l, list):
        for element in l:
            nltk.download(element)
    elif isinstance(l, str):
        nltk.download(l)
    else:
        raise('Not a list or a string, Abort, it is a {}'.format(type(l)))


def update_nltk(nltk_value=None, list_pickles=None):
    """ Download the required files """
    config_value = get_config()
    if nltk_value is None:
        nltk_value = config_value.get('nltk_files'.lower(), None)
    if list_pickles is None:
        list_pickles = config_value.get('list_pickles'.lower(), None)
    import_nltk('nltk_data', nltk_value)
    dl_pickles(list_pickles)


if __name__ == '__main__':
    update_nltk()
