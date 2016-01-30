from astropy.io import fits
import numpy as np
from General import Mathamatics
import math
run = [False]

log = open('log.log', 'w')

class PlotFunctionality(object):

    @staticmethod
    def plot(name, start, showfit, shouldfit, degree, fig, offsety):
        name = str(name)
        sp = fits.open(name)

        wavelength = np.float64(sp[0].data[start-1, :, 0])
        flux = np.float64(sp[0].data[start-1, :, 1])

        if showfit is True:
            spect = fig.add_subplot(1, 2, 2)
        else:
            spect = fig.add_subplot(1, 1, 1)

        if shouldfit:
            fitresults = PlotFunctionality.fitfunction(degree, wavelength, flux, offsety)
            spect.plot(fitresults['wave'], fitresults['y_new'])

            if showfit is True:
                PlotFunctionality.fitshower(fig, wavelength, flux, fitresults['y_poly'])
        else:
            spect.plot(wavelength, flux)

        spect.set_xlabel('Wavelength (Angstroms)')
        spect.set_ylabel('Flux')
        spect.set_title('Single Order 1-D Spectra | Order number: ' + str(start))


    @staticmethod
    def fitshower(fig, wavelength, flux, y_poly):
        fitfig = fig.add_subplot(1, 2, 1)
        fitfig.plot(wavelength, flux)
        fitfig.plot(wavelength, y_poly, color='black', linewidth=2)
        fitfig.set_xlabel('Wavelength (Angstroms)')
        fitfig.set_ylabel('Flux')
        fitfig.set_title('Spectra with Function Fit')

    @staticmethod
    def fitfunction(degree, wavelength, flux, offset):
        newwave = []
        newflux = []
        for j in range(len(wavelength)):
            if (wavelength[j] >= 4855 and wavelength[j] <= 4867) or (wavelength[j] >= 6554 and wavelength[j] <= 6570):
                pass
            else:
                newwave.append(wavelength[j])
                newflux.append(flux[j])
        degree = int(degree)
        z = np.polyfit(newwave, newflux, degree)
        f = np.poly1d(z)
        y_poly = f(newwave)
        y_new = newflux / y_poly
        y_fit = y_new
        fluxstdev = np.std(y_new)
        mean = np.mean(y_new)
        forrange = len(y_new)
        for i in range(forrange):
            if y_new[i] >= (3 * fluxstdev) + mean:
                y_new[i] = mean
                y_fit[i] = mean
            if y_new[i] <= mean - (3 * fluxstdev):
                y_fit[i] = mean
        flux2 = y_fit * y_poly
        z = np.polyfit(newwave, flux2, degree)
        f = np.poly1d(z)
        y_poly = f(wavelength)
        y_new = flux / y_poly
        for i in range(forrange):
            if y_new[i] >= (3 * fluxstdev) + mean:
                y_new[i] = mean
        if offset != 0:
            for j in range(len(y_new)):
                y_new[j] += offset
        return {'y_poly': y_poly, 'y_new': y_new, 'wave': wavelength}

    @staticmethod
    def wfextract(path, order):
        path = str(path)
        sp=fits.open(path)

        wavelength = np.float64(sp[0].data[order, :, 0])
        flux = np.float64(sp[0].data[order, :, 1])

        return {'wavelength': wavelength, 'flux': flux}

class AdvancedPlotting(PlotFunctionality):

    @staticmethod
    def ccor(targetpath, templatepath, degree, order, numberignore, largerwave, smallerwave):
        targetflux = []
        correlation =[]
        corwave = []
        targetdata = PlotFunctionality.wfextract(targetpath, order)
        templatedata = PlotFunctionality.wfextract(templatepath, order)
        newtargetwave = []
        newtargetflux = []
        newtemplatewave = []
        newtemplateflux = []
        largest = Mathamatics.largest(targetdata['wavelength'])
        smallest = Mathamatics.smallest(targetdata['wavelength'])
        for n in range(numberignore):
            if smallest < smallerwave[n] < largest:
                if smallest < largerwave[n] < largest:
                    for j in range(len(targetdata['wavelength'])):
                        if smallerwave[n] <= targetdata['wavelength'][j] <= largerwave[n]:
                            pass
                        else:
                            newtargetwave.append(targetdata['wavelength'][j])
                            newtargetflux.append(targetdata['flux'][j])
                            newtemplatewave.append(templatedata['wavelength'][j])
                            newtemplateflux.append(templatedata['flux'][j])
                else:
                    for j in range(len(targetdata['wavelength'])):
                        if smallerwave[n] <= targetdata['wavelength'][j] <= largest:
                            pass
                        else:
                            newtargetwave.append(targetdata['wavelength'][j])
                            newtargetflux.append(targetdata['flux'][j])
                            newtemplatewave.append(templatedata['wavelength'][j])
                            newtemplateflux.append(templatedata['flux'][j])
            elif smallest < largerwave[n] < largest:
                for j in range(len(targetdata['wavelength'])):
                    if smallest <= targetdata['wavelength'][j] <= largerwave[n]:
                        newtargetwave.append(targetdata['wavelength'][j])
                        newtargetflux.append(targetdata['flux'][j])
                        newtemplatewave.append(templatedata['wavelength'][j])
                        newtemplateflux.append(templatedata['flux'][j])
            else:
                newtargetwave = targetdata['wavelength'].tolist()
                newtargetflux = targetdata['flux'].tolist()
                newtemplatewave = templatedata['wavelength'].tolist()
                newtemplateflux = templatedata['flux'].tolist()
        diff = largest - smallest
        diff = int(math.ceil(diff))
        targetflux.append(PlotFunctionality.fitfunction(degree, newtargetwave, newtargetflux, 0)['y_new'])
        for i in range(2*diff):
            templateflux = []
            usetemplateflux = []
            usetargetflux = []
            wshift = [x + diff - i + 1 for x in newtemplatewave]
            start = Mathamatics.smallest(wshift)
            templateflux.append(PlotFunctionality.fitfunction(degree, wshift, newtemplateflux, 0)['y_new'])

            if Mathamatics.smallest(wshift) > Mathamatics.smallest(newtargetwave):
                for k in range(len(newtargetwave)):
                    if newtargetwave[k] < start:
                        pass
                    else:
                        usetemplateflux.append(templateflux[0][k])
                        usetargetflux.append(targetflux[0][k])
            elif Mathamatics.smallest(wshift) == Mathamatics.smallest(newtargetwave):
                pass
            else:
                for k in range(len(newtargetwave)):
                    if wshift[k] < start:
                        pass
                    else:
                        usetargetflux.append(targetflux[0][k])
                        usetemplateflux.append(templateflux[0][k])
            correlation.append(np.correlate(usetargetflux, usetemplateflux))
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

