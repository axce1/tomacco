# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/dialog.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(178, 275)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.ttime = QtGui.QLabel(Dialog)
        self.ttime.setGeometry(QtCore.QRect(10, 10, 101, 16))
        self.ttime.setObjectName(_fromUtf8("ttime"))
        self.lptime = QtGui.QLabel(Dialog)
        self.lptime.setGeometry(QtCore.QRect(10, 40, 101, 16))
        self.lptime.setObjectName(_fromUtf8("lptime"))
        self.sptime = QtGui.QLabel(Dialog)
        self.sptime.setGeometry(QtCore.QRect(10, 70, 101, 16))
        self.sptime.setObjectName(_fromUtf8("sptime"))
        self.spinTomat = QtGui.QSpinBox(Dialog)
        self.spinTomat.setGeometry(QtCore.QRect(128, 10, 41, 22))
        self.spinTomat.setMinimum(1)
        self.spinTomat.setObjectName(_fromUtf8("spinTomat"))
        self.spinShort = QtGui.QSpinBox(Dialog)
        self.spinShort.setGeometry(QtCore.QRect(128, 70, 41, 22))
        self.spinShort.setMinimum(1)
        self.spinShort.setObjectName(_fromUtf8("spinShort"))
        self.spinLong = QtGui.QSpinBox(Dialog)
        self.spinLong.setGeometry(QtCore.QRect(128, 40, 41, 22))
        self.spinLong.setMinimum(1)
        self.spinLong.setObjectName(_fromUtf8("spinLong"))
        self.btnCnl = QtGui.QPushButton(Dialog)
        self.btnCnl.setGeometry(QtCore.QRect(10, 240, 75, 26))
        self.btnCnl.setObjectName(_fromUtf8("btnCnl"))
        self.btnOk = QtGui.QPushButton(Dialog)
        self.btnOk.setGeometry(QtCore.QRect(90, 240, 75, 26))
        self.btnOk.setObjectName(_fromUtf8("btnOk"))
        self.run_label = QtGui.QLabel(Dialog)
        self.run_label.setGeometry(QtCore.QRect(10, 100, 91, 16))
        self.run_label.setObjectName(_fromUtf8("run_label"))
        self.start_run = QtGui.QCheckBox(Dialog)
        self.start_run.setGeometry(QtCore.QRect(10, 120, 121, 20))
        self.start_run.setObjectName(_fromUtf8("start_run"))
        self.finish_run = QtGui.QCheckBox(Dialog)
        self.finish_run.setGeometry(QtCore.QRect(10, 170, 131, 20))
        self.finish_run.setObjectName(_fromUtf8("finish_run"))
        self.start_edit = QtGui.QLineEdit(Dialog)
        self.start_edit.setEnabled(False)
        self.start_edit.setGeometry(QtCore.QRect(30, 140, 141, 22))
        self.start_edit.setObjectName(_fromUtf8("start_edit"))
        self.finish_edit = QtGui.QLineEdit(Dialog)
        self.finish_edit.setEnabled(False)
        self.finish_edit.setGeometry(QtCore.QRect(30, 200, 141, 22))
        self.finish_edit.setObjectName(_fromUtf8("finish_edit"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.start_run, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.start_edit.setEnabled)
        QtCore.QObject.connect(self.finish_run, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.finish_edit.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.spinTomat, self.spinLong)
        Dialog.setTabOrder(self.spinLong, self.spinShort)
        Dialog.setTabOrder(self.spinShort, self.btnOk)
        Dialog.setTabOrder(self.btnOk, self.btnCnl)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.ttime.setText(_translate("Dialog", "Tomato Time", None))
        self.lptime.setText(_translate("Dialog", "Long Pause Time", None))
        self.sptime.setText(_translate("Dialog", "Short Pause Time", None))
        self.btnCnl.setText(_translate("Dialog", "Cancel", None))
        self.btnOk.setText(_translate("Dialog", "Ok", None))
        self.run_label.setText(_translate("Dialog", "Run commands", None))
        self.start_run.setText(_translate("Dialog", "with start pomidor", None))
        self.finish_run.setText(_translate("Dialog", "when finish pomidor", None))

