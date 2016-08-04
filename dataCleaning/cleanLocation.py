#!/usr/bin/env python
# encoding: utf-8



"""
General script to clean the different locations  -- home institution
"""
import csv

from include.logger import logger
from include.textClean import textClean
from include.textProcess import textProcess



INDATA = './data/'
OUTDATA = '../data/'


def read_file(filename, datafolder='./', header=True):
    """
    """
    infile = datafolder+filename
    outlist = list()
    with open(infile, 'r') as f:
        # FIXME Need to check if value is T/F only
        if header==True:
            csv_file = csv.DictReader(f)
            for l in csv_file:
                outlist.append(l)
        else:
            csv_file = csv.reader(f)
            for l in csv_file:
                outlist.append(l[0])

        return outlist


def institution_set(csv_file):
    """
    Receive the csv row and pick up the institution column
    """
    setInstitution = list()
    for l in csv_file:
        setInstitution.append(l['Home institution'])
    return setInstitution


def clean_list(inlist, cleaner):
    """
    Clean separated element from the list and return a cleaned list
    """
    outlist = list()
    for element in inlist:
        returndict = dict()
        returndict['original']  = element
        cleaned = cleaner.run(element)
        second_clean = set()
        for i in cleaned:
            if i not in ['university']:
                second_clean.add(i)

        returndict['cleaned'] = second_clean
        outlist.append(returndict)
    return outlist


def compare_set(list1, list2):
    """
    """
    outlist = list()
    for i in list1:
        i['match'] = False
        for k in list2:
            if set(i['cleaned']) == set(k['cleaned']):
                i['good'] = k['original']
                i['match'] = True
                break
        outlist.append(i)
    return outlist


def counting_per_institution(inlist):
    """
    """
    final_result = dict()
    for i in inlist:
        if i['match'] is True:
            final_result[i['good']] = final_result.get(i['good'], 0)+1

    return final_result


def write_csv(indict, data_folder):
    """
    """
    print(indict)
    infile = data_folder+'cleaned_result.csv'
    with open(infile, 'w') as f:  # Just use 'w' mode in 3.x
        for i in indict:
            f.write(i)
            f.write('\n')


def write_list(indict, data_folder):
    infile = data_folder+'cleaned_result.csv'
    with open(infile, 'w') as f:  # Just use 'w' mode in 3.x
        for i in indict:
            try:
                f.write(i['good'])
                f.write('\n')
            except KeyError:
                pass


def main():
    """
    """
    # load the list of UK university
    csv_university = read_file('list_universities.csv', INDATA, header=False)
    csv_institutions = read_file('raw_institutions.csv', INDATA)
    list_institutions = institution_set(csv_institutions)
    clean_process = textClean()
    clean_university = clean_list(csv_university, clean_process)
    clean_institutions = clean_list(list_institutions, clean_process)
    # for i in clean_university:

    result = compare_set(clean_institutions, clean_university)
    # final_result = counting_per_institution(result)
    # write_csv(result, OUTDATA)
    write_list(result, OUTDATA)

if __name__ == "__main__":
    main()
