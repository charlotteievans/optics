# -*- coding: utf-8 -*-
"""
Created on 2016-09-29

Read the LabView Raman Spectra txt files from gphoto program

@author: cie1
"""

import numpy as np

def read(filepath):
    array=np.loadtxt(filepath,delimiter='\t').T
    wavelength=array[array.shape[0]-1,:]
    raman_scans=array[:-1,:]
    return wavelength, raman_scans

