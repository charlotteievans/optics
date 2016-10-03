# -*- coding: utf-8 -*-
"""
Created on 2016-09-28

Equations used for curve fitting for linear and cosine squared functions

Functions for curve fits

@author: cie1
"""
import numpy as np


def fit_linear(x, M, B):
    return M * x + B
    # makes linear function


def fit_cossquared(x, A, B, C):
    return A * (np.cos(x + B)) ** 2 + C