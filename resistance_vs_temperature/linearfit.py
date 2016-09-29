import numpy as np
from scipy.optimize import curve_fit
from general.goodnessoffit import redchisqg
from general.curvefitfunctions import functions import linear
import heating.conversions as conv

def rtlinearfit(t,r):
    #I only want to fit the linear regime, where T>40 K -Joey's heating paper
    valuesforfit = np.array([(t[i],r[i]) for i in range(t.size) if t[i]>35])
    p, pcov = curve_fit(linear,valuesforfit[:,0],valuesforfit[:,1])
    #p is the parameters, m and b, and pcov is an array containing error info
    error = np.sqrt(np.diag(pcov))
    #the square root of the diags give standard error for fit paramters
    drdt = p[0] #bookkeeping
    drdterror = error[0] #bookkeeping
    redchi = redchisqg(valuesforfit[:,1],linear(valuesforfit[:,0],drdt,p[1]),deg=2,sd=None)
    equation = 'y = ({:.4f}±{:.4f})x + ({:.4f}±{:.4f}) \nChi Square: {:.4f}'.format(
        drdt, drdterror, p[1], error[1], redchi)
    return drdt,p[1],equation