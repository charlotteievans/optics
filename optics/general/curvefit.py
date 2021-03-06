# -*- coding: utf-8 -*-
"""
Created on 2016-09-28

Returns fit parameters for linear functions

@author: cie1
"""

import numpy as np
from general import goodnessoffit
from scipy.optimize import curve_fit

from optics.general import curvefitfunctions


def fit_linear(x,y): #returns fit parameters, their errors, and fit equation
    p, pcov = curve_fit(curvefitfunctions.fit_linear, x, y)
    # p is the parameters, m and b, and pcov is an array containing error info
    error = np.sqrt(np.diag(pcov))
    m=p[0]
    m_error=error[0]
    b=p[1]
    b_error=error[1]
    redchi = goodnessoffit.redchisqg(y, curvefitfunctions.fit_linear(x, m, b), deg=2, sd=None)
    equation = 'y = ({:.4f}±{:.4f})x + ({:.4f}±{:.4f}) \nChi Square: {:.4f}'.format(
    m, m_error, b, b_error, redchi)
    return m, b, equation


