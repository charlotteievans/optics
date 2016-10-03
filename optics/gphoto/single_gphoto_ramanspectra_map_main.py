from optics.gphoto import gphoto_ramanspectra_top


# CHANGE THESE VALUES

startwavelength=817
endwavelength=819
gphotofilepath='C:\\DOCUMENTS\\Projects\\Gratings\\Data\\2016\\Sept 21\\Gphoto\\2_1_10.txt'
filepath='C:\\DOCUMENTS\\Projects\\Gratings\\Data\\2016\\Sept 21\\Gphoto\\2_1_10_RamanSpectra.txt'
figuredirectory= 'C:\\DOCUMENTS\\Projects\\Test'
format_type='png'
min_value=0
max_value=1
explicit_value_boolean=False


# DON'T CHANGE THE CODE BELOW


supported_formats=['emf','eps','pdf','png','ps','raw','rgba','svg','svgz']

if format_type not in supported_formats:
    print('Format type must be supported. Use ' + str(supported_formats))
else:
    gphoto_ramanspectra_top.plot_single_ramanspectra_map(filepath, gphotofilepath, figuredirectory, startwavelength,
                                                         endwavelength, format_type, min_value, max_value,
                                                         explicit_value_boolean)