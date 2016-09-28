# -*- coding: utf-8 -*-
"""
Created on 2016-09-28

Computes general conversions for projects (e.g. degrees to radians)

@author: cie1
"""

import numpy as np

def dcurrent_to_dtemperature(dcurrent, drdt, resistance, bias):
    # convert from lock-in x to ∆T. 2.22 is from square wave
    return -resistance * resistance * dcurrent * 2.22 / (drdt * bias)

def degrees_to_radians(degrees):
    # converts to radians
    return degrees * np.pi / 180

def power_to_intensity(power):
    # kW/cm^2 for intensity units!!!
    beamdiameter = 0.00018  # in cm
    return power / (np.pi * (beamdiameter / 2) ** 2) * (1 * 10 ** (-3))

def current_to_voltage(current, resistance):
    return current * resistance