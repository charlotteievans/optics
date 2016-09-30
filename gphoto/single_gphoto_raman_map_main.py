from gphoto import gphoto_raman_top


# CHANGE THESE VALUES


gphotofilepath='C:\\DOCUMENTS\\Projects\\Gratings\\Data\\2016\\Sept 21\\Gphoto\\2_1_10.txt'
figuredirectory='C:\\DOCUMENTS\\Projects\\Test'
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
    gphoto_raman_top.plot_single_gphoto_raman_map(gphotofilepath, figuredirectory, format_type, min_value,
                                                  max_value, explicit_value_boolean)
