# -*- coding: utf-8 -*-
"""
Created on 2016-09-28

@author: cie1
"""

import os
from os import path


def listdir(directory):
	return [os.path.join(directory, filename) for filename in os.listdir(directory)]


def return_only_text_files(datafiles):
	return [datafile for datafile in datafiles if datafile.endswith('.txt')]


def return_only_text_no_raman(datafiles):
	return [datafile for datafile in datafiles if (datafile.endswith('.txt') and 'Raman' not in datafile)]