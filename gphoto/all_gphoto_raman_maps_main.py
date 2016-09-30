from gphoto import gphoto_raman_top

# CHANGE THESE VALUES


datadirectory= 'C:\\DOCUMENTS\\Projects\\Gratings\\Data\\2016\\Sept 21\\Gphoto'
figuredirectory= 'C:\\DOCUMENTS\\Projects\\Testing All the Raman'
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
    errors=gphoto_raman_top.plot_all_gphoto_raman_maps(datadirectory, figuredirectory, format_type, min_value, max_value,
                                                       explicit_value_boolean)
    print('Errors: ' + str(errors))