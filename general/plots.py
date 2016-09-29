# -*- coding: utf-8 -*-
"""
Created on 2016-09-28

Allows plotting for linear fits, color maps

@author: cie1
"""

import numpy as np
from general import curvefitfunctions
import matplotlib.pyplot as plt
from os import path


def plot_linear_with_fit(ax=None,x,y,m,b,equation,plot_label,x_label,y_label,x_min,x_max):
    if ax is None:
        ax = plt.gca()
    ax.plot(x,y,label=plot_label)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    x_values=np.linspace(x_min,x_max,100) #values to plot over
    ax.legend(loc="upper left")
    linear_plot=ax.plot(x_values,curvefitfunctions.linear(x_values,m,b), label=equation)
    return linear_plot
    #TODO this needs to be more robust and actually return something...

def plot_color_map(ax, array, plot_title, colormap, x_label, y_label, clb_label, min_val, max_val):
    im = ax.imshow(array.T, cmap=colormap, interpolation='none', vmin=min_val, vmax=max_val)
    ax.set_title(plot_title)
    ax.xlabel(x_label)
    ax.ylabel(y_label)
    clb = plt.colorbar(im, orientation='vertical')
    clb.set_label(clb_label, rotation=270, labelpad=20)
    im.set_clim(min_val,max_val)
    #TODO figure out how to return this

def save_figure(plotlabel,figurepath):
    figbasename = plotlabel + '.png'
    figfilepath = path.join(figurepath,figbasename)
    plt.savefig(figfilepath, format='png')
    #TODO unfuck this so it's not always stuck as png









