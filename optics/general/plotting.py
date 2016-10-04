# -*- coding: utf-8 -*-
"""
Created on 2016-09-28

Allows plotting for linear fits, color maps

@author: cie1
"""

from os import path

import matplotlib.pyplot as plt
import numpy as np
from optics.general import curvefitfunctions

DEFAULT_RESOLUTION=(1600,1200)
DEFAULT_DPI=100

def plot_linear_with_fit(ax, x, y, m, b, equation, plot_label, x_label, y_label):
    ax.scatter(x,y,label=plot_label)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    x_values=np.linspace(min(x),max(y),100)
    ax.legend(loc='upper left')
    ax.plot(x_values, curvefitfunctions.fit_linear(x_values, m, b), label=equation)


def plot_colormap(fig, ax, data, plot_title, colormap, x_label, y_label, clb_label, min_value, max_value):
    cax=ax.imshow(data, cmap=colormap, interpolation='none', vmin=min_value, vmax=max_value)
    clb=fig.colorbar(cax, orientation='vertical')
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(plot_title)
    clb.set_label(clb_label, rotation=270, labelpad=20)
    clb.set_clim(min_value, max_value)
    #TODO put this in the other functions


def save_figure(fig, figuredirectory, plotlabel, resolution=DEFAULT_RESOLUTION, dpi=DEFAULT_DPI, format_type='png'):
    figbasename=plotlabel+'.'+format_type
    figfilepath=path.join(figuredirectory,figbasename)
    fig.set_size_inches(resolution[0]/dpi, resolution[1]/dpi)
    fig.savefig(figfilepath, dpi=dpi, format=format_type)
    plt.savefig(figfilepath, format = format_type)
    #TODO put this in the other functions









