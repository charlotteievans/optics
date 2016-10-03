# -*- coding: utf-8 -*-
"""
Created on 2016-09-28

@author: cie1
"""

import numpy as np

# Returns the reduced chi-square error statistic for an arbitrary model,
# chisq/nu, where nu is the number of degrees of freedom. If individual
# standard deviations (array sd) are supplied, then the chi-square error
# statistic is computed as the sum of squared errors divided by the standard
# deviations. See http://en.wikipedia.org/wiki/Goodness_of_fit for reference.
#
# ydata,ymod,sd assumed to be Numpy arrays. deg integer.
#
# Usage:
# >>> chisq=redchisqg(ydata,ymod,n,sd)
# where
#  ydata : data
#  ymod : model evaluated at the same x points as ydata
#  n : number of free parameters in the model
#  sd : uncertainties in ydata
#
# Rodrigo Nemmen
# http://goo.gl/8S1Oo
#       """
#http://astropython.blogspot.com/2012/02/computing-chi-squared-and-reduced-chi.html


def redchisqg(ydata,ymod,deg=2,sd=None):
    if sd==None:
        chisq=np.sum((ydata-ymod)**2)
    else:
        chisq=np.sum(((ydata-ymod)/sd)**2)
    #Numer of DOF assuming 2 free paramteters
    nu=ydata.size-1-deg
    return chisq/nu
