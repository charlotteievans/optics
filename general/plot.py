# -*- coding: utf-8 -*-
"""
Created on 2016-09-28

Allows plotting for linear fits

@author: cie1
"""

import numpy as np
from general import curvefitfunctions
import matplotlib.pyplot as plt


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

    #this needs to be more robust and actually return something...

