# -*- coding: utf-8 -*-
"""
Created on 2016-09-28

Returns fit parameters for linear functions

@author: cie1
"""

from os import path
import os
from gphoto import gphoto_reader
from resistance_vs_temperature import resistance_and_drdt
from heating import heating_conversions
from general import conversions
from heating import heating_plots
import matplotlib.pylab as plt
import numpy as np
from general import plots
from general import fileutil

def plot_single_heating_map(rtfilepath, gphotofilepath, figurepath, substrate_temperature, max_value_percent):
    os.makedirs(figurepath, exist_ok=True)
    plotlabel = path.splitext(path.basename(gphotofilepath))[0]
    header, arrays = gphoto_reader.read(gphotofilepath)
    drdt, resistance = resistance_and_drdt.get_drdt_and_resistance(rtfilepath, substrate_temperature)
    dcurrent = conversions.rms_to_peak(arrays[0])
    dtemperature = heating_conversions.dcurrent_to_dtemperature(dcurrent, drdt, resistance, header["Applied Voltage"])
    fig, ax = plt.subplots()
    min_val = np.amin(dtemperature)
    max_val = np.sort(dtemperature, axis=None)[int(np.rint(max_value_percent * (np.size(dtemperature)-1)))]
    heating_plots.plot_heating_map(ax, dtemperature, plotlabel, header, min_val, max_val)
    plots.save_figure(plotlabel, figurepath)


def plot_all_heating_maps(rtfilepath, datapath, figurepath, substrate_temperature, max_value_percent):
    drdt, resistance = resistance_and_drdt.get_drdt_and_resistance(rtfilepath, substrate_temperature)
    errors=[]
    zerobias=[]
    os.makedirs(figurepath, exist_ok=True)
    datafiles=fileutil.return_only_text_no_raman(fileutil.listdir(datapath))
    for datafile in datafiles:
        plotlabel = path.splitext(path.basename(datafile))[0]
        try:
            header, arrays = gphoto_reader.read(datafile)
            dcurrent = conversions.rms_to_peak(arrays[0])
            dtemperature = heating_conversions.dcurrent_to_dtemperature(dcurrent, drdt, resistance,
                                                                        header["Applied Voltage"])
            fig, ax = plt.subplots()
            min_val = np.amin(dtemperature)
            max_val = np.sort(dtemperature, axis=None)[int(np.rint(max_value_percent * (np.size(dtemperature)-1)))]
            heating_plots.plot_heating_map(ax, dtemperature, plotlabel, header, min_val, max_val)
            plots.save_figure(plotlabel, figurepath)
            plt.close("all")
            if header['Applied Voltage'] == 0:
                zerobias.append(plotlabel)
        except:
            errors.append(plotlabel)
            pass
    return errors, zerobias

# rtfilepath='C:\\DOCUMENTS\\Projects\\Gratings\\Data\\2016\\Sept 21\\rvst.txt'
# datapath='C:\\DOCUMENTS\\Projects\\Gratings\\Data\\2016\\Sept 21\\Gphoto'
# figurepath='C:\\DOCUMENTS\\Projects\\Test Again'
# substrate_temperature=40.5
# max_value_percent=1
# plot_all_heating_maps(rtfilepath, datapath, figurepath, substrate_temperature, max_value_percent)