# -*- coding: utf-8 -*-
"""
Created on 2016-09-28

Plots gphoto data

@author: cie1
"""

from general import plots

def plot_heatingmap(dtemperature,plotlabel,header,min_val,max_val):
    plot_title=plotlabel + '\nPolarization: ' + str(math.floor(header['Polarization'])) + ' degrees'
    plots.plot_color_map(ax, dtemperature, plot_title, 'coolwarm', 'x pixel', 'y pixel', 'dT (K)', min_val, max_val)
    #TODO return something here


