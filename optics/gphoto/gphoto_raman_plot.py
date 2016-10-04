# -*- coding: utf-8 -*-
"""
Created on 2016-09-28

Plots gphoto raman data

@author: cie1
"""

from optics.general import plotting


def plot_raman_map(fig, ax, raman_array, plotlabel, polarization, min_value, max_value):
    plot_title='{} Raman\nPolarization: {} degrees'.format(plotlabel, polarization)
    plotting.plot_colormap(fig, ax, raman_array, plot_title, 'coolwarm', 'x pixel', 'y pixel', 'counts', min_value,
                           max_value)

#TODO: polarization from header: str(math.floor(header['Polarization'])
#TODO: integrate this for higher programs