# -*- coding: utf-8 -*-
"""
Created on 2016-09-28

Plots gphoto data

@author: cie1
"""

def plot_gphoto(dt,plotlabel,header):
    im = plt.imshow(dt.T, cmap='coolwarm',interpolation='none')
    plt.suptitle(plotlabel + '\nPolarization: ' + str(math.floor(header['Polarization'])) + ' degrees')
    plt.xlabel('x pixel')
    plt.ylabel('y pixel')
    clb = plt.colorbar(im, orientation='vertical')
    clb.set_label('dT (K)', rotation=270, labelpad=20)

