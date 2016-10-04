# -*- coding: utf-8 -*-
"""
Created on 2016-09-28

Creates heating map

@author: cie1
"""

import math

from optics.general import plotting


def plot_heating_map(ax, dtemperature,plotlabel,polarization,min_value,max_value):
    plot_title = '{}\nPolarization: {} degrees'.format(plotlabel, polarization)
    plotting.plot_colormap(fig, ax, dtemperature, plot_title, 'coolwarm', 'x pixel', 'y pixel', 'dT (K)', min_value,
                           max_value)

#TODO: polarization from header: str(math.floor(header['Polarization'])
#TODO integrate this for higher programs


