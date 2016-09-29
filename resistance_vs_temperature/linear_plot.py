# -*- coding: utf-8 -*-
"""
Created on 2016-09-28

Plots linear fits

@author: cie1
"""

import numpy as np
from general import plots


def find_linear_regime(temperature,resistance):
    #take only linear regime of resistance vs. temperature data for linear fit
    #T>35K. Reference: Joey's heating paper
    valuesforfit = np.array([(temperature[i],resistance[i]) for i in range(temperature.size) if temperature[i]>35])
    newtemperature=valuesforfit[0]
    newresistance=valuesforfit[1]
    return newtemperature,newresistance


def plot_resistance_vs_temperature(ax,temperature,resistance,m,b,equation):
    #Input the full resistance vs temperature values
    linear_plot=plots.plot_linear_with_fit(ax, temperature, resistance, m, b, equation, "R vs. T", "Temperature (K)",
                                          "Resistance (Ω)", np.amin(temperature), np.amax(temperature))
    return linear_plot
