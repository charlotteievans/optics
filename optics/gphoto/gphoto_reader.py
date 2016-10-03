# -*- coding: utf-8 -*-
"""
Created on 2016-09-28

Read the LabView txt file for the gphoto program ***NOT FOR GPHOTO RAMAN SPECTRA TXT FILE***

@author: cie1
"""

from itertools import takewhile
import numpy as np

def read(filepath):
    with open(filepath) as inputfile:
        next(inputfile)
        header = {}
        for line in inputfile:
            if not line.strip() and key != 'Notes':
                break
            elif not line.strip() and key == 'Notes':
                pass
            else:
                key, value = (token.strip() for token in line.split(':', maxsplit=1))
                MAGIC_FIELDS = ['Notes', 'Filename and path', 'Center Position']
                header[key] = value if key in MAGIC_FIELDS else float(value)
        arrays=[]
        for line in inputfile:
            if line.startswith('rows'):
                arrays.append(np.loadtxt(takewhile(str.strip, inputfile), delimiter='\t'))
    return header, arrays
