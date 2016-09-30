# -*- coding: utf-8 -*-
"""
Created on 2016-09-28

Top level programs used in main files

@author: cie1
"""

from gphoto import gphoto_raman_plot
from gphoto import gphoto_reader
from general import plots
import os
import numpy as np
from os import path
import matplotlib.pyplot as plt
from general import fileutil


def plot_single_gphoto_raman_map(gphotofilepath, figurepath, format_type, min_value, max_value, explicit_value_boolean):
    os.makedirs(figurepath, exist_ok=True)
    plotlabel = path.splitext(path.basename(gphotofilepath))[0]
    fig, ax = plt.subplots()
    header,arrays=gphoto_reader.read(gphotofilepath)
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
    gphoto_raman_plot.plot_raman_map(ax, raman_array, plotlabel, header, min_value, max_value)
    plots.save_figure(plotlabel, figurepath, format_type)
    plt.close('all')

def plot_all_gphoto_raman_maps(datapath, figurepath, format_type, min_value, max_value, explicit_value_boolean):
    if min_value>max_value:
        print('Max value must be greater than min value')
        return
    if not explicit_value_boolean:
        if max_value>1:
            print('maximum percentage must be a decimal less than or equal to 1')
            return
    os.makedirs(figurepath, exist_ok=True)
    errors=[]
    datafiles = fileutil.return_only_text_no_raman(fileutil.listdir(datapath))
    for datafile in datafiles:
        plotlabel=path.splitext(path.basename(datafile))[0]
        try:
            header, arrays = gphoto_reader.read(datafile)
            raman_array = arrays[2]
            fig, ax = plt.subplots()
            if max_value<=1: #TODO why is this janky
                min_value = np.sort(raman_array, axis=None)[int(np.rint(min_value * (np.size(raman_array) - 1)))]
                max_value = np.sort(raman_array, axis=None)[int(np.rint(max_value * (np.size(raman_array) - 1)))]
            gphoto_raman_plot.plot_raman_map(ax, raman_array, plotlabel, header, min_value, max_value)
            plots.save_figure(plotlabel, figurepath, format_type)
            plt.close('all')
        except:
            errors.append(plotlabel)
            pass
    return errors
datapath='C:\\DOCUMENTS\\Projects\\Gratings\\Data\\2016\\Sept 21\\Gphoto'
figurepath='C:\\DOCUMENTS\\Projects\\Testing All the Raman'
format_type='png' #Supported formats: emf, eps, pdf, png, ps, raw, rgba, svg, svgz
min_value=0
max_value=1
explicit_value_boolean=False
errors=plot_all_gphoto_raman_maps(datapath, figurepath, format_type, min_value, max_value, explicit_value_boolean)
print(errors)