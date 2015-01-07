import sys
import time
from PySide import QtCore, QtGui

import state

class MainWindow(QtGui.QWidget):
    def __init__(self, controller):
        super().__init__()

        self.resize(130, 50)
        self.setWindowTitle('TomatoTimer')

        self.btn_start = QtGui.QPushButton("Start", self)
        self.btn_lpause = QtGui.QPushButton("Long Pause", self)
        self.btn_spause = QtGui.QPushButton("Short Pause", self)
        self.widget = QtGui.QLabel(str("25:00"), self)
        self.countPomidoro = QtGui.QLabel(str("1"), self)

        self.control = controller

        # timer
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_label)
        self.timer.start(1000)

        # self.control.btn_start_click(self)

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

        # connect
        self.btn_start.clicked.connect(self.on_button)

    def on_button(self):
        self.control.btn_start_click(self)

    def update_label(self):
        tick = state.TickEvent(time.time())
        if not self.control.st.get_state == 'init':
            label_time = time.strftime("%M:%S", time.gmtime(tick.get_time()))
            self.widget.setText(str(label_time))
        self.control.st.next_state(tick)
        print (self.control.st.get_state)

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


class Controller():

    def __init__(self):
        self.st = state.LogicFMS()

    def btn_start_click(self, app):

        if self.st.state.name == 'init':
            app.btn_start.setText("Stop")
            icon = QtGui.QIcon('images/red-tomat.png')
            app.trayIcon.setIcon(icon)
            self.st.next_state(state.StartEvent, time.time())
        else:
            app.btn_start.setText("Start")
            icon = QtGui.QIcon('images/black-tomat.png')
            app.trayIcon.setIcon(icon)
            self.st.next_state(state.StopEvent)
        # if not app.timer.isActive():
            # app.btn_start.setText("Stop")
            # icon = QtGui.QIcon('images/red-tomat.png')
            # app.trayIcon.setIcon(icon)
            # app.timer.start(1000)
        # else:
            # app.btn_start.setText("Start")
            # app.timer.stop()
            # icon = QtGui.QIcon('images/black-tomat.png')
            # app.trayIcon.setIcon(icon)



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('TomatoTimer')

    control = Controller()
    main = MainWindow(control)
    main.show()

    sys.exit(app.exec_())
