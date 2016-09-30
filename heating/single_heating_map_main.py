# -*- coding: utf-8 -*-
"""
Created on 2016-09-29

Plots and saves a single heat map

@author: cie1
"""

from heating import heating_top

# CHANGE THESE VALUES

rtfilepath='C:\\DOCUMENTS\\Projects\\Gratings\\Data\\2016\\Sept 21\\rvst.txt'
gphotofilepath='C:\\DOCUMENTS\\Projects\\Gratings\\Data\\2016\\Sept 21\\Gphoto\\2_1_1.txt'
figuredirectory='C:\\DOCUMENTS\\Projects\\Test'
substrate_temperature=40.5
format_type='png' #Supported formats: emf, eps, pdf, png, ps, raw, rgba, svg, svgz
min_value=0
max_value=1
explicit_value_boolean=False
#if set to false, the min and max values are the percentile of data that will be plotted
#on the colormap. 0 would be the minimum array value and 1 would be the maximum array value

# DON'T CHANGE THE CODE BELOW

supported_formats=['emf','eps','pdf','png','ps','raw','rgba','svg','svgz']

if format_type not in supported_formats:
    print('Format type must be supported. Use ' + str(supported_formats))
else:
    heating_top.plot_single_heating_map(rtfilepath, gphotofilepath, figuredirectory, substrate_temperature,
                                        format_type, min_value, max_value, explicit_value_boolean)