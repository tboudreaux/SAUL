from astropy.io import fits
import numpy as np
from General import Mathamatics
import math
run = [False]

log = open('log.log', 'w')

class PlotFunctionality(object):

    @staticmethod
    def plot(name, start, showfit, shouldfit, degree, fig,):
        name = str(name)
        sp = fits.open(name)

        wavelength = np.float64(sp[0].data[start, :, 0])
        flux = np.float64(sp[0].data[start, :, 1])

        if showfit is True:
            spect = fig.add_subplot(1, 2, 2)
        else:
            spect = fig.add_subplot(1, 1, 1)

        if shouldfit:
            fitresults = PlotFunctionality.fitfunction(degree, wavelength, flux)
            spect.plot(wavelength, fitresults['y_new'])

            if showfit is True:
                PlotFunctionality.fitshower(fig, wavelength, flux, fitresults['y_poly'])
        else:
            spect.plot(wavelength, flux)

        while run[0] is False:
            spect.set_xlabel('Wavelength (Angstroms)')
            spect.set_ylabel('Flux')
            spect.set_title('Single Order 1-D Spectra | Order number: ' + str(start))
            run[0] = True

    @staticmethod
    def fitshower(fig, wavelength, flux, y_poly):
        fitfig = fig.add_subplot(1, 2, 1)
        fitfig.plot(wavelength, flux)
        fitfig.plot(wavelength, y_poly, color='black', linewidth=2)
        fitfig.set_xlabel('Wavelength (Angstroms)')
        fitfig.set_ylabel('Flux')
        fitfig.set_title('Spectra with Function Fit')

    @staticmethod
    def fitfunction(degree, wavelength, flux):
        degree = int(degree)
        z = np.polyfit(wavelength, flux, degree)
        f = np.poly1d(z)
        y_poly = f(wavelength)
        y_new = flux - y_poly
        return {'y_poly': y_poly, 'y_new': y_new}

    @staticmethod
    def wfextract(path, order):
        path = str(path)
        sp=fits.open(path)

        wavelength = np.float64(sp[0].data[order, :, 0])
        flux = np.float64(sp[0].data[order, :, 1])

        return {'wavelength': wavelength, 'flux': flux}

class AdvancedPlotting(PlotFunctionality):

    @staticmethod
    def ccor(targetpath, templatepath, degree, order):
        targetflux = []
        correlation =[]
        corwave = []
        targetdata = PlotFunctionality.wfextract(targetpath, order)
        templatedata = PlotFunctionality.wfextract(templatepath, order)
        largest = Mathamatics.largest(targetdata['wavelength'])
        smallest = Mathamatics.smallest(targetdata['wavelength'])
        diff = largest - smallest
        diff = int(math.ceil(diff))
        targetflux.append(PlotFunctionality.fitfunction(degree, targetdata['wavelength'], targetdata['flux'])['y_new'])
        for i in range(2 * diff):
            templateflux = []
            wshift = [x + diff - i for x in templatedata['wavelength']]
            templateflux.append(PlotFunctionality.fitfunction(degree, wshift, templatedata['flux'])['y_new'])
            correlation.append(np.correlate(targetflux[0], templateflux[0]))
            corwave.append(diff-i)
        return {'correlation': correlation, 'corwave': corwave}

    @staticmethod
    def listcomp(list1, list2):
        same = False
        if len(list1) == len(list2):
            same = True
        return same

    @staticmethod
    def openlist(filename):
        listactual = open(filename, 'rb')
        listarray = []
        for line in listactual:
            listarray.append(line)
        return listarray
