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
figurepath='C:\\DOCUMENTS\\Projects\\Test'
substrate_temperature=40.5
max_value_percent=1 #must be decimal less than or equal to one
format_type='png' #Supported formats: emf, eps, pdf, png, ps, raw, rgba, svg, svgz

# DON'T CHANGE THE CODE BELOW

supported_formats=['emf','eps','pdf','png','ps','raw','rgba','svg','svgz']

if max_value_percent>1:
    print('max_val_percent must be a decimal less than or equal to 1')
elif format_type not in supported_formats:
    print('Format type must be supported. Use ' + str(supported_formats))
else:
    heating_top.plot_single_heating_map(rtfilepath, gphotofilepath, figurepath, substrate_temperature,
                                        max_value_percent, format_type)