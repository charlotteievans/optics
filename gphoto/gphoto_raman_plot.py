# -*- coding: utf-8 -*-
"""
Created on 2016-09-28

Plots gphoto raman data

@author: cie1
"""

def gphotomapplot_raman(raman_array,plotlabel,header):
    im = plt.imshow(raman_array.T, cmap='coolwarm', interpolation='none')
    plt.suptitle(plotlabel+' Raman' + '\nPolarization: ' + str(math.floor(header['Polarization'])) + ' degrees')
    plt.xlabel('x pixel')
    plt.ylabel('y pixel')
    clb = plt.colorbar(im, orientation='vertical')
    clb.set_label('counts', rotation=270, labelpad=20)