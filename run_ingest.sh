#!/usr/bin/env bash

# Software Sustainability Institute web site API

# Try and install requirements, regardless as to whether
# they are there already to avoid having to check.
pip install -r requirements.txt

# Create directories for raw and filtered data, if they
# don't exist.
mkdir -p data/sheets/as-is
mkdir -p data/sheets/filtered

python src/download_consultancy.py --noauth_local_webserver
python src/download_swc.py --noauth_local_webserver
python src/download_policy.py --noauth_local_webserver
