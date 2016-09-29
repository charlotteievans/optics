# -*- coding: utf-8 -*-
"""
Created on 2016-09-28

@author: cie1
"""

import numpy as np
from resistance_vs_temperature import resistance_vs_temperature_reader
from resistance_vs_temperature import linear_plot
from general import curvefit


def find_resistance(substratetemp, t, r):
    #takes data within a half a degree and returns the average resistance
    values = np.array([(t[i], r[i]) for i in range(t.size) if (substratetemp - 1) < t[i] < (substratetemp + 1)])
    resistance = np.average(values[:,1])
    resistance_error = np.std(values[:,1])
    return resistance,resistance_error


def get_drdt_and_resistance(resistance_vs_temperature_filepath, substrate_temperature):
    t, r = resistance_vs_temperature_reader.read(resistance_vs_temperature_filepath)
    fittemperature,fitresistance=linear_plot.find_linear_regime(t,r)
    drdt,_,_=curvefit.fit_linear(fittemperature, fitresistance)
    resistance, _ = find_resistance(substrate_temperature, t, r)
    return drdt, resistance


