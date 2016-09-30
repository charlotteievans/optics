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


def single_gphoto_raman_map(gphotofilepath, figurepath, format_type, min_value, max_value, explicit_value_boolean):
    os.makedirs(figurepath, exist_ok=True)
    plotlabel = path.splitext(path.basename(gphotofilepath))[0]
    fig, ax = plt.subplots()
    header,arrays=gphoto_reader.read(gphotofilepath)
    raman_array = arrays[2]
    if max_value<min_value:
        print('max value must be larger than min value')
        return
    if explicit_value_boolean is False:
        if max_value>1:
            print('max value percentage must be a decimal less than or equal to 1')
            return
        min_value = np.sort(raman_array, axis=None)[int(np.rint(min_value * (np.size(raman_array) - 1)))]
        max_value=np.sort(raman_array, axis=None)[int(np.rint(max_value * (np.size(raman_array) - 1)))]
    gphoto_raman_plot.plot_raman_map(ax, raman_array, plotlabel, header, min_value, max_value)
    plots.save_figure(plotlabel, figurepath, format_type)

