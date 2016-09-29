# -*- coding: utf-8 -*-
"""
Created on 2016-09-28

@author: cie1
"""

import numpy as np

def read(filepath):
    with open(filepath) as inputfile:
        rtdata = np.loadtxt(inputfile, delimiter='\t')
        rtdata = rtdata[np.isfinite(rtdata).all(axis=1)]
    temperature = rtdata[:, 0]
    resistance = rtdata[:, 1]
    return temperature, resistance