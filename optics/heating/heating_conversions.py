# -*- coding: utf-8 -*-
"""
Created on 2016-09-28

Converts dI to dT

@author: cie1
"""

def dcurrent_to_dtemperature(dcurrent, drdt, resistance, bias):
    #Reference: Joey's heating paper
    return -resistance * resistance * dcurrent / (drdt * bias)