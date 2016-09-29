# -*- coding: utf-8 -*-
"""
Created on 2016-09-29

Plots and saves a single heat map

@author: cie1
"""

from heating import heating_main

# CHANGE THESE VALUES

rtfilepath='C:\\DOCUMENTS\\Projects\\Gratings\\Data\\2016\\Sept 21\\rvst.txt'
gphotofilepath='C:\\DOCUMENTS\\Projects\\Gratings\\Data\\2016\\Sept 21\\Gphoto\\2_1_1.txt'
figurepath='C:\\DOCUMENTS\\Projects\\Test'
substrate_temperature=40.5
max_value_percent=1 #must be decimal less than or equal to one

# DON'T CHANGE THE CODE BELOW

if max_value_percent>1:
    print('max_val_percent must be a decimal less than or equal to 1')
else:
    heating_main.plot_single_heating_map(rtfilepath, gphotofilepath, figurepath, substrate_temperature,
                                        max_value_percent)