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
    t = rtdata[:, 0]  # sets first column as x val array
    r = rtdata[:, 1]  # sets second column as y val array
    return t, r