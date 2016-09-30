# -*- coding: utf-8 -*-
"""
Created on 2016-09-28

@author: cie1
"""

from os import path
import os
import zipfile


def listdir(directory):
	return [path.join(directory, filename) for filename in os.listdir(directory)]


def return_only_zip_files(datafiles):
    return [datafile for datafile in datafiles if datafile.endswith('.zip')]


def return_only_text_files(datafiles):
	return [datafile for datafile in datafiles if datafile.endswith('.txt')]


def return_only_text_no_raman(datafiles):
	return [datafile for datafile in datafiles if (datafile.endswith('.txt') and 'Raman' not in datafile)]


def return_ramanspectra_files(datafiles):
    return [datafile for datafile in datafiles if (datafile.endswith('.txt') and "RamanSpectra" in datafile)]


def unzip_file(datafile, destination_directory):
    os.makedirs(destination_directory, exist_ok=True)
    with zipfile.ZipFile(datafile, "r") as z:
        z.extractall(destination_directory)


def match_files(shortername_listdir,longername_listdir,key_word): #TODO this is janky
    dummy_list=[]
    sorted_list=[]
    for item in shortername_listdir:
        dummy_list.append(path.splitext(path.basename(item))[0]+key_word)
    for item in dummy_list:
        for n in longername_listdir:
            if item in n:
                sorted_list.append(n)
    return sorted_list

