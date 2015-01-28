# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Wed Jan 21 16:35:26 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(260, 100)
        self.btn_lpause = QtGui.QPushButton(Dialog)
        self.btn_lpause.setGeometry(QtCore.QRect(170, 40, 81, 26))
        self.btn_lpause.setObjectName("btn_lpause")
        self.btn_start = QtGui.QPushButton(Dialog)
        self.btn_start.setEnabled(True)
        self.btn_start.setGeometry(QtCore.QRect(170, 10, 81, 50))
        self.btn_start.setObjectName("btn_start")
        self.btn_spause = QtGui.QPushButton(Dialog)
        self.btn_spause.setGeometry(QtCore.QRect(170, 10, 81, 26))
        self.btn_spause.setObjectName("btn_spause")
        self.lcd = QtGui.QLCDNumber(Dialog)
        self.lcd.setGeometry(QtCore.QRect(10, 10, 151, 75))
        self.lcd.setObjectName("lcd")
        self.btn_stop = QtGui.QPushButton(Dialog)
        self.btn_stop.setGeometry(QtCore.QRect(170, 10, 81, 50))
        self.btn_stop.setObjectName("btn_stop")
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(170, 70, 81, 16))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_lpause.setText(QtGui.QApplication.translate("Dialog", "Long Pause", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_start.setText(QtGui.QApplication.translate("Dialog", "Start Pomido", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_spause.setText(QtGui.QApplication.translate("Dialog", "Short Pause", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_stop.setText(QtGui.QApplication.translate("Dialog", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "", None, QtGui.QApplication.UnicodeUTF8))

