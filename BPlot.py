# Echel Spectra viewer
# Paddy Clancy and Thomas Boudreaux
from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
import platform
import sys
import os
from PyQt4 import QtGui
from SecondGui import Ui_Header
from astropy.modeling import models, fitting
import webbrowser

operatings = platform.system()
print('Checking Operating System')
if operatings == 'Windows':
    print('Program does not run on Windows machines, please use a UNIX Like system to run program')
    exit()
else:
    print('OS OK')

inputArray = []
useArray = [False, False]
fit = [False]

class General(object):

    @staticmethod
    def smallest(array):
        smallestnum = array[0]
        for i in range(len(array)):
            if array[i] < smallestnum:
                smallestnum = array[i]
        return smallestnum

    @staticmethod
    def largest(array):
        largestnum = array[0]
        for i in range(len(array)):
            if array[i] > largestnum:
                largestnum = array[i]
        return largestnum


class Plotter(object):

    @staticmethod
    def stackplot(stackfile, allimages, num, start):
        pathList = open(stackfile, 'rb')
        pathArray = []
        for line in pathList:
            pathArray.append(line)
        if allimages is True:
            stackNum = len(pathArray)
        else:
            if num > len(pathArray):
                num = len(pathArray)
            stackNum = num


        for i in range(stackNum):
            name = pathArray[i]
            name = name[:-1]
            sp = fits.open(name)
            hdu = sp[0].header

            ordernum = start

            dateobs = (hdu['DATE-OBS'])
            objName = (hdu['OBJECT'])
            wavelength = np.float64(sp[0].data[ordernum, :, 0])
            flux = np.float64(sp[0].data[ordernum, :, 1])

            plt.plot(wavelength, flux)

        plt.xlabel('Wavelength (Angstroms)')
        plt.ylabel('Flux')
        plt.title('Single Order 1-D Spectra for ' + str(stackNum) + ' Stars | Order number: ' + str(start))
        plt.show()

    @staticmethod
    def nstackplot(name, start, degree, shouldfit):
        degree = int(degree)

        filename = str(name)
        # opens file as a fits file using the fits function set from astropy
        sp = fits.open(filename)

        # Opens the Header file as a object hdu
        hdu = sp[0].header

        # Order number Changer (Change this to look at different orders)
        ordernum = start
        # Pulls the date from the fits header
        dateobs = (hdu['DATE-OBS'])

        # Pulls the wavelength and flux values for a given order number, stores as a numpy array
        wavelength = np.float64(sp[0].data[ordernum, :, 0])
        flux = np.float64(sp[0].data[ordernum, :, 1])
        if shouldfit:
            z = np.polyfit(wavelength, flux, degree)
            f = np.poly1d(z)
            y_poly = f(wavelength)
            y_new = flux - y_poly
            plt.plot(wavelength, y_new, color='green')
            plt.xlabel('wavelength (Angstroms)')
            plt.ylabel('Flux')

        else:
            plt.plot(wavelength, flux)
            plt.xlabel('Wavelength')
            plt.ylabel('Flux')
            plt.title('Single Order 1-D Spectra | Order number: ' + str(start))

        # Initializes X11 window
        plt.show()


class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Header()
        self.ui.setupUi(self)

        self.ui.generatePathFiles.clicked.connect(self.search)
        self.ui.quitBut.clicked.connect(self.end)
        self.ui.stackIm.stateChanged.connect(self.stackinput)
        self.ui.allStack.stateChanged.connect(self.allinput)
        self.ui.plotBut.clicked.connect(self.plot)
        self.ui.Secret.clicked.connect(self.secret)
        self.ui.FunctionFit.stateChanged.connect(self.fitter)



    @staticmethod
    def end():
        exit()

    @staticmethod
    def secret():
        webbrowser.open('http://d.justpo.st/images/2013/04/b83fb1b7222c18934e59c5b1bd2f43bd.jpg')

    @staticmethod
    def stackinput():
        useArray[0] = not useArray[0]

    @staticmethod
    def allinput():
        useArray[1] = not useArray[1]

    @staticmethod
    def fitter():
        fit[0] = not fit[0]

    def search(self):
        count = 0
        namearray = []
        for root, dirs, files in os.walk('.', topdown=True):
            for file in files:
                if 'achi' in file:
                    filename = os.path.join(root, file)
                    sp = fits.open(filename)
                    hdu = sp[0].header
                    objname = (hdu['OBJECT'])
                    if objname not in namearray:
                        namearray.append(objname)
        for i in range(len(namearray)):
            starname = namearray[i]
            self.ui.listWidget.addItem('Star name: ' + starname)
            self.ui.listWidget.addItem('File name: PathTo' + starname)
            nameforfile = 'PathTo' + starname
            printlist = open(nameforfile, 'w')
            for root, dirs, files in os.walk('.', topdown=True):
                for file in files:
                    if 'achi' in file:
                        name = os.path.join(root, file)
                        sp = fits.open(name)
                        hdu = sp[0].header
                        objname1 = (hdu['OBJECT'])
                        if starname in objname1:
                            print >>printlist, name
                            self.ui.listWidget.addItem(name)
                            count += 1
                            progress = (count/len(namearray))*100
                            self.ui.PathFileProgress.setValue(progress)
        self.ui.generatePathFiles.setStyleSheet("background-color: green; color: white")

    def plot(self):
        if useArray[0] is True:
            pathfilename = self.ui.pathListInput.toPlainText()
            numToStack = self.ui.numStack.value()
            order = self.ui.startOrd.value()
            Plotter.stackplot(pathfilename, useArray[1], numToStack, order)
        else:
            filename = self.ui.singleFileInput.toPlainText()
            degree = self.ui.amplitude.toPlainText()
            order = self.ui.startOrd.value()
            Plotter.nstackplot(filename, order, degree, fit[0])

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())