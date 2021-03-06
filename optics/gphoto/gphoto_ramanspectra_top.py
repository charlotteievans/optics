import math
import os
from os import path

import matplotlib.pyplot as plt
import numpy as np
from general import fileutil
from gphoto import gphoto_ramanspectra_data

from optics.general import plotting
from optics.gphoto import gphoto_raman_plot


def plot_single_ramanspectra_map(filepath, gphotofilepath, figuredirectory, startwavelength, endwavelength,
                                 format_type, min_value, max_value, explicit_value_boolean):
    os.makedirs(figuredirectory, exist_ok=True)
    plotlabel = path.splitext(path.basename(filepath))[0]
    fig, ax = plt.subplots()
    raman_array, header= gphoto_ramanspectra_data.get_ramanspectra_array(filepath, gphotofilepath, startwavelength,
                                                                         endwavelength)
    if max_value<min_value:
        print('max value must be larger than min value')
        return
    if not explicit_value_boolean:
        if max_value>1:
            print('max value percentage must be a decimal less than or equal to 1')
            return
        min_value = np.sort(raman_array, axis=None)[int(np.rint(min_value * (np.size(raman_array) - 1)))]
        max_value=np.sort(raman_array, axis=None)[int(np.rint(max_value * (np.size(raman_array) - 1)))]
    gphoto_raman_plot.plot_raman_map(ax, raman_array, plotlabel, header, min_value, max_value)
    plotting.save_figure(plotlabel, figuredirectory, format_type)
    plt.close('all')


def plot_all_ramanspectra_maps(datadirectory,gphotofiledirectory,figuredirectory,startwavelength,endwavelength,
                               format_type, min_value, max_value, explicit_value_boolean):
    if min_value>max_value:
        print('Max value must be greater than min value')
        return
    if not explicit_value_boolean:
        if max_value>1:
            print('maximum percentage must be a decimal less than or equal to 1')
            return
    os.makedirs(figuredirectory, exist_ok=True)
    errors=[]
    datafiles_temp = fileutil.return_ramanspectra_files(fileutil.listdir(datadirectory))
    gphotofiles= fileutil.return_only_text_no_raman(fileutil.listdir(gphotofiledirectory))
    datafiles= fileutil.match_files(gphotofiles, datafiles_temp, '_RamanSpectra')
    min_input=min_value
    max_input=max_value
    fig = plt.figure()
    ax = fig.add_subplot(111)
    for datafile,gphotofile in zip(datafiles,gphotofiles):
        plotlabel=path.splitext(path.basename(datafile))[0]
        try:
            ax.cla()  # TODO plots like shit
            min_value=min_input
            max_value=max_input
            raman_array, header = gphoto_ramanspectra_data.get_ramanspectra_array(datafile, gphotofile,
                                                                                  startwavelength, endwavelength)
            if max_value<=1: #TODO this doesn't work
                min_value = np.sort(raman_array, axis=None)[int(np.rint(min_value * (np.size(raman_array) - 1)))]
                max_value = np.sort(raman_array, axis=None)[int(np.rint(max_value * (np.size(raman_array) - 1)))]
            plot_title = plotlabel + ' Raman' + '\nPolarization: ' + str(
                math.floor(header['Polarization'])) + ' degrees'


            im = ax.imshow(raman_array, cmap='coolwarm', interpolation='none', vmin=min_value, vmax=max_value)
            ax.set_title(plot_title)
            plt.xlabel('x')
            plt.ylabel('y')
            clb = plt.colorbar(orientation='vertical')
            #clb.set_label('clb', rotation=270, labelpad=20)
            #im.set_clim(min_value, max_value)
            #gphoto_raman_plot.plot_raman_map(ax, raman_array, plotlabel, header, min_value, max_value)
            plotting.save_figure(plotlabel, figuredirectory, format_type)
            plotting.save_figure()
            fig.clf()
        except:
            errors.append(plotlabel)
            pass
    return errors


