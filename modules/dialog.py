# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created: Fri Feb  6 15:16:50 2015
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(177, 131)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.ttime = QtWidgets.QLabel(Dialog)
        self.ttime.setGeometry(QtCore.QRect(10, 10, 101, 16))
        self.ttime.setObjectName("ttime")
        self.lptime = QtWidgets.QLabel(Dialog)
        self.lptime.setGeometry(QtCore.QRect(10, 40, 101, 16))
        self.lptime.setObjectName("lptime")
        self.sptime = QtWidgets.QLabel(Dialog)
        self.sptime.setGeometry(QtCore.QRect(10, 70, 101, 16))
        self.sptime.setObjectName("sptime")
        self.spinTomat = QtWidgets.QSpinBox(Dialog)
        self.spinTomat.setGeometry(QtCore.QRect(128, 10, 41, 22))
        self.spinTomat.setMinimum(1)
        self.spinTomat.setObjectName("spinTomat")
        self.spinShort = QtWidgets.QSpinBox(Dialog)
        self.spinShort.setGeometry(QtCore.QRect(128, 70, 41, 22))
        self.spinShort.setMinimum(1)
        self.spinShort.setObjectName("spinShort")
        self.spinLong = QtWidgets.QSpinBox(Dialog)
        self.spinLong.setGeometry(QtCore.QRect(128, 40, 41, 22))
        self.spinLong.setMinimum(1)
        self.spinLong.setObjectName("spinLong")
        self.btnCnl = QtWidgets.QPushButton(Dialog)
        self.btnCnl.setGeometry(QtCore.QRect(10, 100, 75, 26))
        self.btnCnl.setObjectName("btnCnl")
        self.btnOk = QtWidgets.QPushButton(Dialog)
        self.btnOk.setGeometry(QtCore.QRect(90, 100, 75, 26))
        self.btnOk.setObjectName("btnOk")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.spinTomat, self.spinLong)
        Dialog.setTabOrder(self.spinLong, self.spinShort)
        Dialog.setTabOrder(self.spinShort, self.btnOk)
        Dialog.setTabOrder(self.btnOk, self.btnCnl)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.ttime.setText(_translate("Dialog", "Tomato Time"))
        self.lptime.setText(_translate("Dialog", "Long Pause Time"))
        self.sptime.setText(_translate("Dialog", "Short Pause Time"))
        self.btnCnl.setText(_translate("Dialog", "Cancel"))
        self.btnOk.setText(_translate("Dialog", "Ok"))

