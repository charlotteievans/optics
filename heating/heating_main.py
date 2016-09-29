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


def plot_single_heating_map(rtfilepath, gphotofilepath, figurepath, substrate_temperature):
    os.makedirs(figurepath, exist_ok=True)
    plotlabel = path.splitext(path.basename(gphotofilepath))[0]
    header, arrays = gphoto_reader.read(gphotofilepath)
    drdt, resistance = resistance_and_drdt.get_drdt_and_resistance(rtfilepath, substrate_temperature)
    dcurrent = conversions.rms_to_peak(arrays[0])
    dtemperature = heating_conversions.dcurrent_to_dtemperature(dcurrent, drdt, resistance, header["Applied Voltage"])
    fig, ax = plt.subplots()
    min_val = np.amin(dtemperature)
    max_val = np.sort(dtemperature, axis=None)[int(np.rint(0.9 * np.size(dtemperature)))]
    heating_plots.plot_heating_map(ax, dtemperature, plotlabel, header, min_val, max_val)
    plots.save_figure(plotlabel, figurepath)


def plot_all_heating_maps(rtfilepath, datapath, figurepath, substrate_temperature):
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
            max_val = np.sort(dtemperature, axis=None)[int(np.rint(0.9 * np.size(dtemperature)))]
            heating_plots.plot_heating_map(ax, dtemperature, plotlabel, header, min_val, max_val)
            plots.save_figure(plotlabel, figurepath)
            plt.close("all")
            if header['Applied Voltage'] == 0:
                zerobias.append(plotlabel)
        except:
            errors.append(plotlabel)
            pass
    return errors, zerobias
