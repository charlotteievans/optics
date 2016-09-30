# -*- coding: utf-8 -*-
"""
Created on 2016-09-28

Creates heating map

@author: cie1
"""

from general import plotting
import math


def plot_heating_map(ax, dtemperature,plotlabel,header,min_val,max_val):
    plot_title=plotlabel + '\nPolarization: ' + str(math.floor(header['Polarization'])) + ' degrees'
    plotting.plot_color_map(ax, dtemperature, plot_title, 'coolwarm', 'x pixel', 'y pixel', 'dT (K)', min_val, max_val)
    #TODO return something here


