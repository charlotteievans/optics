# -*- coding: utf-8 -*-
"""
Created on 2016-09-28

Plots gphoto raman data

@author: cie1
"""

from general import plots

def plot_raman_map(ax, raman_array, plotlabel, header, min_val, max_val):
    plot_title = plotlabel+' Raman' + '\nPolarization: ' + str(math.floor(header['Polarization'])) + ' degrees'
    plots.plot_color_map(ax, raman_array, plot_title, 'coolwarm', 'x pixel', 'y pixel', 'counts', min_val, max_val)
    # TODO return something here
