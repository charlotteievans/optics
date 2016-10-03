# -*- coding: utf-8 -*-
"""
Created on 2016-09-28

Top level programs used in main files

@author: cie1
"""

import os
from os import path

import matplotlib.pyplot as plt
import numpy as np
from general import fileutil
from gphoto import gphoto_raman_plot

from optics.general import plotting
from optics.gphoto import gphoto_reader


def plot_single_gphoto_raman_map(gphotofilepath, figuredirectory, format_type, min_value, max_value, explicit_value_boolean):
    os.makedirs(figuredirectory, exist_ok=True)
    plotlabel = path.splitext(path.basename(gphotofilepath))[0]
    fig, ax = plt.subplots()
    header,arrays= gphoto_reader.read(gphotofilepath)
    raman_array = arrays[2]
    if max_value<min_value:
        print('max value must be larger than min value')
        return
    if not explicit_value_boolean:
        if max_value>1:
            print('max value percentage must be a decimal less than or equal to 1')
            return
        min_value = np.sort(raman_array, axis=None)[int(np.rint(min_value * (np.size(raman_array) - 1)))]
        max_value=np.sort(raman_array, axis=None)[int(np.rint(max_value * (np.size(raman_array) - 1)))]
    gphoto_raman_plot.plot_raman_map(ax, raman_array.T, plotlabel, header, min_value, max_value)
    plotting.save_figure(plotlabel, figuredirectory, format_type)
    plt.close('all')


def plot_all_gphoto_raman_maps(datadirectory, figuredirectory, format_type, min_value, max_value, explicit_value_boolean):
    if min_value>max_value:
        print('Max value must be greater than min value')
        return
    if not explicit_value_boolean:
        if max_value>1:
            print('maximum percentage must be a decimal less than or equal to 1')
            return
    os.makedirs(figuredirectory, exist_ok=True)
    errors=[]
    datafiles = fileutil.return_only_text_no_raman(fileutil.listdir(datadirectory))
    for datafile in datafiles:
        plotlabel=path.splitext(path.basename(datafile))[0]
        try:
            header, arrays = gphoto_reader.read(datafile)
            raman_array = arrays[2]
            fig, ax = plt.subplots()
            if max_value<=1: #TODO this doesn't work
                min_value = np.sort(raman_array, axis=None)[int(np.rint(min_value * (np.size(raman_array) - 1)))]
                max_value = np.sort(raman_array, axis=None)[int(np.rint(max_value * (np.size(raman_array) - 1)))]
            gphoto_raman_plot.plot_raman_map(ax, raman_array.T, plotlabel, header, min_value, max_value)
            plotting.save_figure(plotlabel, figuredirectory, format_type)
            plt.close('all')
        except:
            errors.append(plotlabel)
            pass
    return errors