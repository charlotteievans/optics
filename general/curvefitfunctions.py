# -*- coding: utf-8 -*-
"""
Created on 2016-09-28

Functions for curve fits

@author: cie1
"""
import numpy as np

def linear(x, M, B):
    return M * x + B
    # makes linear function


def cossquared(x, A, B, C):
    return A * (np.cos(x + B)) ** 2 + C