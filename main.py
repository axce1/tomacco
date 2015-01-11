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
        self.btn_stop = QtGui.QPushButton("Stop", self)
        self.btn_lpause = QtGui.QPushButton("Long Pause", self)
        self.btn_spause = QtGui.QPushButton("Short Pause", self)
        self.widget = QtGui.QLabel(str("Press Start"), self)
        self.countPomidoro = QtGui.QLabel(str("1"), self)

        self.control = controller

        # timer
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_label)
        self.timer.start(100)

        # self.control.btn_start_click(self)

        # lcd
        self.lcd = QtGui.QLCDNumber()
        self.lcd.setDigitCount(5)
        self.lcd.display('00:00')
        blue = "#0000ff"
        style_str = "QWidget {background-color: %s}"
        self.lcd.setStyleSheet(style_str % blue)

        # layout
        self.layoutVertical = QtGui.QVBoxLayout(self)
        self.layoutVertical.addWidget(self.countPomidoro)
        self.layoutVertical.addWidget(self.lcd)
        self.layoutVertical.addWidget(self.btn_start)
        self.layoutVertical.addWidget(self.btn_stop)
        self.layoutVertical.addWidget(self.btn_lpause)
        self.layoutVertical.addWidget(self.btn_spause)

        # tray
        self.create_tray_icon()
        self.trayIcon.activated.connect(self.on_trayicon_activated)
        self.trayIcon.show()

        self.btn_stop.hide()
        self.btn_lpause.hide()
        self.btn_spause.hide()

        # connect
        self.btn_start.clicked.connect(self.on_btn_start)
        self.btn_stop.clicked.connect(self.on_btn_stop)
        self.btn_spause.clicked.connect(self.on_btn_spause)
        self.btn_lpause.clicked.connect(self.on_btn_lpause)

    def on_btn_start(self):
        self.control.btn_start_click(self)

    def on_btn_stop(self):
        self.control.btn_stop_click(self)

    def on_btn_spause(self):
        self.control.btn_spause_click(self)

    def on_btn_lpause(self):
        self.control.btn_lpause_click(self)

    def update_label(self):
        t = time.time()
        self.evt = state.TickEvent(t)
        self.control.st.next_state(self.evt)
        self.update_windonw()

    def update_windonw(self):
        if isinstance(self.control.st.state, state.InitState):
            self.widget.setText('Press Start')
            self.lcd.display(str('00:00'))
            self.btn_start.show()
            self.btn_stop.hide()

        elif isinstance(self.control.st.state, state.TomatoState):
            label_time = self.control.st.remining_time(self.evt)
            self.widget.setText('Counting Pomidoro')
            self.lcd.display(str(label_time))
            self.btn_start.hide()
            self.btn_stop.show()

        elif isinstance(self.control.st.state, state.SelectState):
            self.widget.setText('Select Pause')
            self.lcd.display(str('00:00'))
            self.btn_start.hide()
            self.btn_stop.hide()
            self.btn_lpause.show()
            self.btn_spause.show()

        elif isinstance(self.control.st.state, state.ShortState):
            label_time = self.control.st.remining_time(self.evt)
            self.widget.setText('Counting Short Pause')
            self.lcd.display(str(label_time))
            self.btn_lpause.hide()
            self.btn_spause.hide()
            self.btn_stop.show()

        elif isinstance(self.control.st.state, state.LongState):
            label_time = self.control.st.remining_time(self.evt)
            self.widget.setText('Counting Long Pause')
            self.lcd.display(str(label_time))
            self.btn_lpause.hide()
            self.btn_spause.hide()
            self.btn_stop.show()


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
        app.update_windonw()
        icon = QtGui.QIcon('images/red-tomat.png')
        app.trayIcon.setIcon(icon)
        self.st.next_state(state.StartEvent, time.time())

    def btn_stop_click(self, app):
        app.update_windonw()
        icon = QtGui.QIcon('images/black-tomat.png')
        app.trayIcon.setIcon(icon)
        self.st.next_state(state.StopEvent)

    def btn_spause_click(self, app):
        app.update_windonw()
        icon = QtGui.QIcon('images/short-tomat.png')
        app.trayIcon.setIcon(icon)
        self.st.next_state(state.ShortEvent, time.time())

    def btn_lpause_click(self, app):
        app.update_windonw()
        icon = QtGui.QIcon('images/long-tomat.png')
        app.trayIcon.setIcon(icon)
        self.st.next_state(state.LongEvent, time.time())


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('TomatoTimer')

    control = Controller()
    main = MainWindow(control)
    main.show()

    sys.exit(app.exec_())
