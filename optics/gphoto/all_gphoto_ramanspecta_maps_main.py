from optics.gphoto import gphoto_ramanspectra_top


# CHANGE THESE VALUES

startwavelength=817
endwavelength=819
gphotofilepath='C:\\DOCUMENTS\\Projects\\Gratings\\Data\\2016\\Sept 21\\Gphoto'
datadirectory= 'C:\\DOCUMENTS\\Projects\\Gratings\\Data\\2016\\Sept 21\\Gphoto'
figuredirectory='C:\\DOCUMENTS\\Projects\\Janky Test'
format_type='png'
min_value=0
max_value=1
explicit_value_boolean=False


# DON'T CHANGE THE CODE BELOW


supported_formats=['emf','eps','pdf','png','ps','raw','rgba','svg','svgz']

if format_type not in supported_formats:
    print('Format type must be supported. Use ' + str(supported_formats))
else:
    errors= gphoto_ramanspectra_top.plot_all_ramanspectra_maps(datadirectory, gphotofilepath, figuredirectory,
                                                               startwavelength, endwavelength, format_type, min_value,
                                                               max_value, explicit_value_boolean)
    print('Errors: ' + str(errors))
    print(len(errors))