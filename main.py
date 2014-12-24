import sys
from PySide import QtCore, QtGui


class MainWindow(QtGui.QWidget):
    def __init__(self):
        super().__init__()

        self.resize(130, 50)
        self.setWindowTitle('TomatoTimer')

        self.btn_start = QtGui.QPushButton("Start", self)
        self.btn_lpause = QtGui.QPushButton("Long Pause", self)
        self.btn_spause = QtGui.QPushButton("Short Pause", self)
        self.widget = QtGui.QLabel(str("25:00"), self)
        self.countPomidoro = QtGui.QLabel(str("1"), self)

        # layout
        self.layoutVertical = QtGui.QVBoxLayout(self)
        self.layoutVertical.addWidget(self.countPomidoro)
        self.layoutVertical.addWidget(self.widget)
        self.layoutVertical.addWidget(self.btn_start)
        self.layoutVertical.addWidget(self.btn_lpause)
        self.layoutVertical.addWidget(self.btn_spause)

        # tray
        self.create_tray_icon()
        self.trayIcon.activated.connect(self.on_trayicon_activated)
        self.trayIcon.show()

        self.btn_lpause.hide()
        self.btn_spause.hide()

    def create_tray_icon(self):
        icon = QtGui.QIcon('images/black-tomat.png')
        menu = QtGui.QMenu(self)
        resetAction = menu.addAction("Reset Pomidoro")
        # resetAction.triggered.connect(self.resetPomidoro)
        settingAction = menu.addAction("Settings")
        # settingAction.triggered.connect(self.dialog)
        settingAction.setDisabled(True)
        menu.addSeparator()
        exitAction = menu.addAction("Quit")
        exitAction.triggered.connect(QtGui.qApp.quit)
        self.trayIcon = QtGui.QSystemTrayIcon(self)
        self.trayIcon.setContextMenu(menu)
        self.trayIcon.setIcon(icon)

    def on_trayicon_activated(self, reason):
        if reason == QtGui.QSystemTrayIcon.DoubleClick:
            if self.isHidden():
                self.show()
            else:
                self.hide()

    def change_event(self, event):
        if event.type() == QtCore.QEvent.Close:
            event.ignore()
            self.close()
            return
        super().changeEvent(event)

    def close_event(self, event):
        even.ignore()
        self.hide()

    def open_dialog(self):
        dialog = Dialog(self)
        dialog.show()


class Dialog(QtGui.QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Settings")
        self.setWindowModality(QtCore.Qt.WindowModal)

        self.ttime = QtGui.QLabel(self)
        self.ttime.setText("Tomato Time")
        self.lpause = QtGui.QLabel(self)
        self.lpause.setText("Long Pause")
        self.spause = QtGui.QLabel(self)
        self.spause.setText("Short Pause")

        self.tt_spin = QtGui.QSpinBox()
        self.lp_spin = QtGui.QSpinBox()
        self.sp_spin = QtGui.QSpinBox()

        btnOk = QtGui.QPushButton("Ok")
        btnCancel = QtGui.QPushButton("Cancel")

        layout = QtGui.QGridLayout()
        layout.addWidget(self.ttime, 0, 0)
        layout.addWidget(self.lpause, 1, 0)
        layout.addWidget(self.spause, 2, 0)
        layout.addWidget(self.tt_spin, 0, 1)
        layout.addWidget(self.lp_spin, 1, 1)
        layout.addWidget(self.sp_spin, 2, 1)
        layout.addWidget(btnOk)
        layout.addWidget(btnCancel)
        self.setLayout(layout)

        btnCancel.clicked.connect(self.hide)

    def change_event(self, event):
        if event.type() == QtCore.QEvent.Quit:
            event.ignore()
            self.close()
            return
        super().changeEvent(event)

    def close_event(self, event):
        event.ignore()
        self.hide()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('TomatoTimer')

    main = MainWindow()
    main.show()

    sys.exit(app.exec_())
