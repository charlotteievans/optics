# -*- coding: utf-8 -*-
"""
Created on 2016-09-28

Converts dI to dT

@author: cie1
"""

def dcurrent_to_dtemperature(dcurrent, drdt, resistance, bias):
    # convert from lock-in x to ∆T. 2.22 is from square wave
    #Reference: Joey's heating paper
    return -resistance * resistance * dcurrent * 2.22/ (drdt * bias)
#TODO change this so 2.22 is out