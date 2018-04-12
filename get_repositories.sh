#!/usr/bin/env bash

# Download data from softwaresaved repositories.

mkdir -p data/repositories/
mkdir -p data/repositories/consultancy

TMP_GIT=/tmp/git-metrics
rm -rf $TMP_GIT
mkdir -p $TMP_GIT
git clone https://${GIT_TOKEN}:x-oauth-basic@github.com/softwaresaved/metrics $TMP_GIT
cp $TMP_GIT/consultancy/data/project_metrics/output_csv/effort_by_jacs data/repositories/consultancy/effort_by_jacs.csv
cp $TMP_GIT/consultancy/data/project_metrics/output_csv/projects_by_jacs.csv data/repositories/consultancy
rm -rf $TMP_GIT
