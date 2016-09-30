# -*- coding: utf-8 -*-
"""
Created on 2016-09-28

@author: cie1
"""

from os import path
import os


def listdir(directory):
	return [path.join(directory, filename) for filename in os.listdir(directory)]


def return_only_text_files(datafiles):
	return [datafile for datafile in datafiles if datafile.endswith('.txt')]


def return_only_text_no_raman(datafiles):
	return [datafile for datafile in datafiles if (datafile.endswith('.txt') and 'Raman' not in datafile)]


def return_ramanspectra_files(datafiles):
    return [datafile for datafile in datafiles if (datafile.endswith('.txt') and "RamanSpectra" in datafile)]


def unzip_file(datafile, destination):
    with zipfile.ZipFile(datafile, "r") as z:
        z.extractall(destination)


