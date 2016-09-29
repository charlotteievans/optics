# -*- coding: utf-8 -*-
"""
Created on 2016-09-28

@author: cie1
"""

import numpy as np

def findresistance(substratetemp, t, r):
    #takes data within a half a degree and returns the average resistance
    values = np.array([(t[i],r[i]) for i in range(t.size) if (substratetemp-1)<t[i]<(substratetemp+1)])
    resistance = np.average(values[:,1])
    rerror = np.std(values[:,1])
    return resistance,rerror

def get_drdt_and_resistance(rtfilepath, substratetemp):
    t, r = tempreader(rtfilepath)
    drdt, _, _ = rtlinearfit(t, r)
    resistance, _ = findresistance(substratetemp, t, r)
    return drdt, resistance
