# -*- coding: utf-8 -*-
"""
Created on 2016-09-28

Top level programs used in main files

@author: cie1
"""

import os
from os import path

import matplotlib.pylab as plt
import numpy as np
from general import fileutil
from general import plotting

from heating import heating_plots
from optics.general import conversions
from optics.gphoto import gphoto_reader
from optics.heating import heating_conversions, heating_plots
from optics.resistance_vs_temperature import resistance_and_drdt


def plot_single_heating_map(rtfilepath, gphotofilepath, figuredirectory, substrate_temperature, format_type, min_value,
                            max_value, explicit_value_boolean):
    os.makedirs(figuredirectory, exist_ok=True)
    plotlabel = path.splitext(path.basename(gphotofilepath))[0]
    header, arrays = gphoto_reader.read(gphotofilepath)
    drdt, resistance = resistance_and_drdt.get_drdt_and_resistance(rtfilepath, substrate_temperature)
    dcurrent = conversions.rms_to_peak(arrays[0])
    dtemperature = heating_conversions.dcurrent_to_dtemperature(dcurrent, drdt, resistance, header["Applied Voltage"])
    fig, ax = plt.subplots()
    if max_value<min_value:
        print('max value must be larger than min value')
        return
    if explicit_value_boolean is False:
        if max_value>1:
            print('max value percentage must be a decimal less than or equal to 1')
            return
        min_value = np.sort(dtemperature, axis=None)[int(np.rint(min_value * (np.size(dtemperature) - 1)))]
        max_value=np.sort(dtemperature, axis=None)[int(np.rint(max_value * (np.size(dtemperature) - 1)))]
    heating_plots.plot_heating_map(ax, dtemperature.T, plotlabel, header, min_value, max_value)
    plotting.save_figure(plotlabel, figuredirectory, format_type)
    plt.close('all')


def plot_all_heating_maps(rtfilepath, datadirectory, figuredirectory, substrate_temperature, format_type, min_value, max_value,
                          explicit_value_boolean):
    if min_value>max_value:
        print('Max value must be greater than min value')
        return
    if not explicit_value_boolean:
        if max_value>1:
            print('maximum percentage must be a decimal less than or equal to 1')
            return
    drdt, resistance = resistance_and_drdt.get_drdt_and_resistance(rtfilepath, substrate_temperature)
    errors=[]
    zerobias=[]
    os.makedirs(figuredirectory, exist_ok=True)
    datafiles= fileutil.return_only_text_no_raman(fileutil.listdir(datadirectory))
    for datafile in datafiles:
        plotlabel = path.splitext(path.basename(datafile))[0]
        try:
            header, arrays = gphoto_reader.read(datafile)
            dcurrent = conversions.rms_to_peak(arrays[0])
            dtemperature = heating_conversions.dcurrent_to_dtemperature(dcurrent, drdt, resistance,
                                                                        header["Applied Voltage"])
            fig, ax = plt.subplots()
            if max_value<=1: #TODO this doesn't work
                min_value=np.sort(dtemperature, axis=None)[int(np.rint(min_value * (np.size(dtemperature)-1)))]
                max_value = np.sort(dtemperature, axis=None)[int(np.rint(max_value * (np.size(dtemperature)-1)))]
            heating_plots.plot_heating_map(ax, dtemperature.T, plotlabel, header, min_value, max_value)
            plotting.save_figure(plotlabel, figuredirectory, format_type)
            plt.close("all")
            if header['Applied Voltage'] == 0:
                zerobias.append(plotlabel)
        except:
            errors.append(plotlabel)
            pass
    return errors, zerobias

