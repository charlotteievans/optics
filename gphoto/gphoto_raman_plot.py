# -*- coding: utf-8 -*-
"""
Created on 2016-09-28

Plots gphoto raman data

@author: cie1
"""

from general import plotting
import math


def plot_raman_map(ax, raman_array, plotlabel, header, min_value, max_value):
    plot_title = plotlabel+' Raman' + '\nPolarization: ' + str(math.floor(header['Polarization'])) + ' degrees'
    plotting.plot_color_map(ax, raman_array, plot_title, 'coolwarm', 'x pixel', 'y pixel', 'counts', min_value,
                             max_value)
    # TODO return something here
