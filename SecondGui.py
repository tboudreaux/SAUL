# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SecondGui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Header(object):
    def setupUi(self, Header):
        Header.setObjectName(_fromUtf8("Header"))
        Header.resize(554, 774)
        self.stackIm = QtGui.QCheckBox(Header)
        self.stackIm.setGeometry(QtCore.QRect(0, 10, 111, 22))
        self.stackIm.setObjectName(_fromUtf8("stackIm"))
        self.pathListInput = QtGui.QTextEdit(Header)
        self.pathListInput.setGeometry(QtCore.QRect(10, 50, 361, 31))
        self.pathListInput.setObjectName(_fromUtf8("pathListInput"))
        self.pathListLabel = QtGui.QLabel(Header)
        self.pathListLabel.setGeometry(QtCore.QRect(10, 30, 161, 17))
        self.pathListLabel.setObjectName(_fromUtf8("pathListLabel"))
        self.singleFileLabel = QtGui.QLabel(Header)
        self.singleFileLabel.setGeometry(QtCore.QRect(10, 90, 121, 17))
        self.singleFileLabel.setObjectName(_fromUtf8("singleFileLabel"))
        self.singleFileInput = QtGui.QTextEdit(Header)
        self.singleFileInput.setGeometry(QtCore.QRect(10, 110, 361, 31))
        self.singleFileInput.setObjectName(_fromUtf8("singleFileInput"))
        self.numStack = QtGui.QSpinBox(Header)
        self.numStack.setGeometry(QtCore.QRect(390, 50, 61, 31))
        self.numStack.setMinimum(1)
        self.numStack.setObjectName(_fromUtf8("numStack"))
        self.allStack = QtGui.QCheckBox(Header)
        self.allStack.setGeometry(QtCore.QRect(470, 50, 51, 22))
        self.allStack.setObjectName(_fromUtf8("allStack"))
        self.generatePathFiles = QtGui.QPushButton(Header)
        self.generatePathFiles.setGeometry(QtCore.QRect(10, 150, 151, 27))
        self.generatePathFiles.setObjectName(_fromUtf8("generatePathFiles"))
        self.quitBut = QtGui.QPushButton(Header)
        self.quitBut.setGeometry(QtCore.QRect(470, 360, 71, 27))
        self.quitBut.setObjectName(_fromUtf8("quitBut"))
        self.plotBut = QtGui.QPushButton(Header)
        self.plotBut.setGeometry(QtCore.QRect(470, 330, 71, 27))
        self.plotBut.setObjectName(_fromUtf8("plotBut"))
        self.startOrd = QtGui.QSpinBox(Header)
        self.startOrd.setGeometry(QtCore.QRect(390, 110, 61, 31))
        self.startOrd.setMinimum(1)
        self.startOrd.setMaximum(62)
        self.startOrd.setObjectName(_fromUtf8("startOrd"))
        self.label_4 = QtGui.QLabel(Header)
        self.label_4.setGeometry(QtCore.QRect(390, 90, 161, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.StackNumberLabel = QtGui.QLabel(Header)
        self.StackNumberLabel.setGeometry(QtCore.QRect(380, 30, 161, 17))
        self.StackNumberLabel.setObjectName(_fromUtf8("StackNumberLabel"))
        self.PathFileProgress = QtGui.QProgressBar(Header)
        self.PathFileProgress.setGeometry(QtCore.QRect(10, 180, 151, 31))
        self.PathFileProgress.setProperty("value", 0)
        self.PathFileProgress.setObjectName(_fromUtf8("PathFileProgress"))
        self.listWidget = QtGui.QListWidget(Header)
        self.listWidget.setGeometry(QtCore.QRect(0, 231, 461, 161))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.label = QtGui.QLabel(Header)
        self.label.setGeometry(QtCore.QRect(0, 210, 111, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.FunctionFit = QtGui.QCheckBox(Header)
        self.FunctionFit.setGeometry(QtCore.QRect(190, 150, 121, 22))
        self.FunctionFit.setObjectName(_fromUtf8("FunctionFit"))
        self.Secret = QtGui.QPushButton(Header)
        self.Secret.setGeometry(QtCore.QRect(470, 300, 71, 27))
        self.Secret.setObjectName(_fromUtf8("Secret"))
        self.line = QtGui.QFrame(Header)
        self.line.setGeometry(QtCore.QRect(0, 140, 551, 16))
        self.line.setAccessibleName(_fromUtf8(""))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.amplitude = QtGui.QTextEdit(Header)
        self.amplitude.setGeometry(QtCore.QRect(200, 190, 101, 31))
        self.amplitude.setToolTip(_fromUtf8(""))
        self.amplitude.setStatusTip(_fromUtf8(""))
        self.amplitude.setWhatsThis(_fromUtf8(""))
        self.amplitude.setAccessibleName(_fromUtf8(""))
        self.amplitude.setAccessibleDescription(_fromUtf8(""))
        self.amplitude.setDocumentTitle(_fromUtf8(""))
        self.amplitude.setObjectName(_fromUtf8("amplitude"))
        self.line_3 = QtGui.QFrame(Header)
        self.line_3.setGeometry(QtCore.QRect(170, 150, 20, 81))
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.info = QtGui.QPushButton(Header)
        self.info.setGeometry(QtCore.QRect(470, 270, 71, 27))
        self.info.setObjectName(_fromUtf8("info"))
        self.label_2 = QtGui.QLabel(Header)
        self.label_2.setGeometry(QtCore.QRect(200, 170, 91, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.line_4 = QtGui.QFrame(Header)
        self.line_4.setGeometry(QtCore.QRect(320, 150, 20, 81))
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.Reset = QtGui.QPushButton(Header)
        self.Reset.setGeometry(QtCore.QRect(470, 240, 71, 27))
        self.Reset.setObjectName(_fromUtf8("Reset"))
        self.line_2 = QtGui.QFrame(Header)
        self.line_2.setGeometry(QtCore.QRect(-10, 400, 551, 16))
        self.line_2.setAccessibleName(_fromUtf8(""))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.consol = QtGui.QTextBrowser(Header)
        self.consol.setGeometry(QtCore.QRect(10, 431, 521, 291))
        self.consol.setObjectName(_fromUtf8("consol"))
        self.label_3 = QtGui.QLabel(Header)
        self.label_3.setGeometry(QtCore.QRect(220, 410, 111, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_5 = QtGui.QLabel(Header)
        self.label_5.setGeometry(QtCore.QRect(10, 730, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.consolinput = QtGui.QLineEdit(Header)
        self.consolinput.setGeometry(QtCore.QRect(30, 730, 501, 31))
        self.consolinput.setObjectName(_fromUtf8("consolinput"))
        self.tabWidget = QtGui.QTabWidget(Header)
        self.tabWidget.setGeometry(QtCore.QRect(320, 150, 231, 80))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.Operation = QtGui.QWidget()
        self.Operation.setObjectName(_fromUtf8("Operation"))
        self.function2 = QtGui.QPushButton(self.Operation)
        self.function2.setGeometry(QtCore.QRect(0, 30, 101, 20))
        self.function2.setObjectName(_fromUtf8("function2"))
        self.function4 = QtGui.QPushButton(self.Operation)
        self.function4.setGeometry(QtCore.QRect(120, 30, 101, 20))
        self.function4.setObjectName(_fromUtf8("function4"))
        self.function1 = QtGui.QPushButton(self.Operation)
        self.function1.setGeometry(QtCore.QRect(0, 0, 101, 21))
        self.function1.setObjectName(_fromUtf8("function1"))
        self.function3 = QtGui.QPushButton(self.Operation)
        self.function3.setGeometry(QtCore.QRect(120, 0, 101, 21))
        self.function3.setObjectName(_fromUtf8("function3"))
        self.tabWidget.addTab(self.Operation, _fromUtf8(""))
        self.UserFunctions = QtGui.QWidget()
        self.UserFunctions.setObjectName(_fromUtf8("UserFunctions"))
        self.UserFunction2 = QtGui.QPushButton(self.UserFunctions)
        self.UserFunction2.setGeometry(QtCore.QRect(0, 30, 101, 20))
        self.UserFunction2.setObjectName(_fromUtf8("UserFunction2"))
        self.UseFunction1 = QtGui.QPushButton(self.UserFunctions)
        self.UseFunction1.setGeometry(QtCore.QRect(0, 0, 101, 20))
        self.UseFunction1.setObjectName(_fromUtf8("UseFunction1"))
        self.UserFuntion3 = QtGui.QPushButton(self.UserFunctions)
        self.UserFuntion3.setGeometry(QtCore.QRect(120, 0, 101, 20))
        self.UserFuntion3.setObjectName(_fromUtf8("UserFuntion3"))
        self.userFuntion4 = QtGui.QPushButton(self.UserFunctions)
        self.userFuntion4.setGeometry(QtCore.QRect(120, 30, 101, 20))
        self.userFuntion4.setObjectName(_fromUtf8("userFuntion4"))
        self.tabWidget.addTab(self.UserFunctions, _fromUtf8(""))

        self.retranslateUi(Header)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Header)

    def retranslateUi(self, Header):
        Header.setWindowTitle(_translate("Header", "Basic Spectral Plotter", None))
        self.stackIm.setText(_translate("Header", "Stack Images", None))
        self.pathListLabel.setText(_translate("Header", "Path List File Name", None))
        self.singleFileLabel.setText(_translate("Header", "Single File Name", None))
        self.allStack.setText(_translate("Header", "All", None))
        self.generatePathFiles.setText(_translate("Header", "Generate Path Files", None))
        self.quitBut.setText(_translate("Header", "Quit", None))
        self.plotBut.setText(_translate("Header", "Plot", None))
        self.label_4.setText(_translate("Header", "Starting Order Number", None))
        self.StackNumberLabel.setText(_translate("Header", "Stack How Many?", None))
        self.label.setText(_translate("Header", "Path Files List", None))
        self.FunctionFit.setText(_translate("Header", "Fit a Function", None))
        self.Secret.setText(_translate("Header", "Answer", None))
        self.info.setText(_translate("Header", "Info", None))
        self.label_2.setText(_translate("Header", "Degree:", None))
        self.Reset.setText(_translate("Header", "Reset", None))
        self.label_3.setText(_translate("Header", "Console Logger", None))
        self.label_5.setText(_translate("Header", ">", None))
        self.function2.setText(_translate("Header", "C-Correlation", None))
        self.function4.setText(_translate("Header", "G-Fit", None))
        self.function1.setText(_translate("Header", "Show Fit", None))
        self.function3.setText(_translate("Header", "LS", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Operation), _translate("Header", "Operations", None))
        self.UserFunction2.setText(_translate("Header", "Function 2", None))
        self.UseFunction1.setText(_translate("Header", "Function 1", None))
        self.UserFuntion3.setText(_translate("Header", "Function 3", None))
        self.userFuntion4.setText(_translate("Header", "Function 4", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.UserFunctions), _translate("Header", "User Functions", None))

