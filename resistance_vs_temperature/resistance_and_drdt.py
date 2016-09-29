# -*- coding: utf-8 -*-
"""
Created on 2016-09-28

@author: cie1
"""

import numpy as np
from resistance_vs_temperature import resistance_vs_temperature_reader

def find_resistance(substrate_temperature, temperature, resistance):
    #takes data within a half a degree and returns the average resistance
    values = np.array([(temperature[i],resistance[i]) for i in range(temperature.size) if (substrate_temperature - 1) < t[i] < (substrate_temperature + 1)])
    resistance = np.average(values[:,1])
    resistance_error = np.std(values[:,1])
    return resistance,resistance_error

def get_drdt_and_resistance(resistance_vs_temperature_filepath, substrate_temperature):
    t, r = resistance_vs_temperature_reader.read(resistance_vs_temperature_filepath)
    drdt, _, _ = rtlinearfit(t, r)
    resistance, _ = findresistance(substrate_temperature, t, r)
    return drdt, resistance
