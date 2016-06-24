# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/form.ui'
#
# Created by: PyQt4 UI code generator 4.12.dev1606101416
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(360, 201)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lcd = QtGui.QLCDNumber(self.centralwidget)
        self.lcd.setObjectName(_fromUtf8("lcd"))
        self.horizontalLayout.addWidget(self.lcd)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.btn_start = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_start.sizePolicy().hasHeightForWidth())
        self.btn_start.setSizePolicy(sizePolicy)
        self.btn_start.setObjectName(_fromUtf8("btn_start"))
        self.verticalLayout.addWidget(self.btn_start)
        self.btn_stop = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_stop.sizePolicy().hasHeightForWidth())
        self.btn_stop.setSizePolicy(sizePolicy)
        self.btn_stop.setObjectName(_fromUtf8("btn_stop"))
        self.verticalLayout.addWidget(self.btn_stop)
        self.btn_spause = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.btn_spause.sizePolicy().hasHeightForWidth())
        self.btn_spause.setSizePolicy(sizePolicy)
        self.btn_spause.setObjectName(_fromUtf8("btn_spause"))
        self.verticalLayout.addWidget(self.btn_spause)
        self.btn_lpause = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.btn_lpause.sizePolicy().hasHeightForWidth())
        self.btn_lpause.setSizePolicy(sizePolicy)
        self.btn_lpause.setObjectName(_fromUtf8("btn_lpause"))
        self.verticalLayout.addWidget(self.btn_lpause)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(0, 10)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.status_bar = QtGui.QStatusBar(MainWindow)
        self.status_bar.setObjectName(_fromUtf8("status_bar"))
        MainWindow.setStatusBar(self.status_bar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.btn_start.setText(_translate("MainWindow", "Start \n"
"Tomacco", None))
        self.btn_stop.setText(_translate("MainWindow", "Stop \n"
"Tomacco", None))
        self.btn_spause.setText(_translate("MainWindow", "Short Pause", None))
        self.btn_lpause.setText(_translate("MainWindow", "Long Pause", None))

