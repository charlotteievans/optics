from gphoto import gphoto_reader
from gphoto import gphoto_ramanspectra_reader
from general import conversions
import numpy as np
import scipy.integrate

def get_ramanspectra_array(filepath, gphotofilepath, startwavelength, endwavelength):
    wavelength, raman_scans = gphoto_ramanspectra_reader.read(filepath)
    startindex=conversions.find_nearest(wavelength,startwavelength)
    endindex=conversions.find_nearest(wavelength,endwavelength)
    header, _=gphoto_reader.read(gphotofilepath)
    pixels=header['Scan Density (pixel/line)']
    integratedvalues=np.zeros(raman_scans.shape[0])
    integratedwavelengths=np.array([wavelength[i] for i in range(startindex,endindex)])
    for i, raman_scan in enumerate(raman_scans):
        integratedvalues[i] = scipy.integrate.trapz([raman_scan[n] for n in range(startindex, endindex)],
                                                    integratedwavelengths)
    raman_array = np.reshape(integratedvalues, (pixels, pixels))
    return raman_array, header





