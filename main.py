import sys
import time
from PySide import QtCore, QtGui

from modules import form
from modules import dialog
from modules import config
import state


class MainWindow(QtGui.QWidget, form.Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.fms = state.LogicFMS()

        self.dialog = DialogWindow(self)
        self.dialog.update_time()

        # init show window
        self.setFixedSize(self.size())
        self.set_position()
        self.btn_lpause.hide()
        self.btn_spause.hide()
        self.btn_stop.hide()

        # timer
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_label)
        self.timer.start(100)

        # lcd
        self.lcd.display('00:00')

        # tray
        self.create_tray_icon()
        self.trayIcon.activated.connect(self.on_trayicon_activated)
        self.trayIcon.show()

        # connect
        self.btn_start.clicked.connect(self.on_btn_start)
        self.btn_stop.clicked.connect(self.on_btn_stop)
        self.btn_spause.clicked.connect(self.on_btn_spause)
        self.btn_lpause.clicked.connect(self.on_btn_lpause)

    def on_btn_start(self):
        icon = QtGui.QIcon('images/red-tomat.png')
        self.trayIcon.setIcon(icon)
        self.fms.next_state(state.StartEvent, time.time())

    def on_btn_stop(self):
        icon = QtGui.QIcon('images/black-tomat.png')
        self.trayIcon.setIcon(icon)
        #XXX dont work state.StopEvent, only state.StopEvent()
        self.fms.next_state(state.StopEvent(), time.time())

    def on_btn_spause(self):
        icon = QtGui.QIcon('images/short-tomat.png')
        self.trayIcon.setIcon(icon)
        self.fms.next_state(state.ShortEvent(), time.time())

    def on_btn_lpause(self):
        icon = QtGui.QIcon('images/long-tomat.png')
        self.trayIcon.setIcon(icon)
        self.fms.next_state(state.LongEvent(), time.time())

    def update_label(self):
        t = time.time()
        self.evt = state.TickEvent()
        self.fms.next_state(self.evt, t)
        self.update_windonw()

    def update_windonw(self):
        if isinstance(self.fms.state, state.InitState):
            icon = QtGui.QIcon('images/black-tomat.png')
            self.trayIcon.setIcon(icon)
            self.label.setText("Tomat - " + str(self.fms.pomidor))
            self.lcd.display(str('00:00'))
            self.btn_start.show()
            self.btn_stop.hide()
            self.startAction.setDisabled(False)
            self.stopAction.setDisabled(True)
            self.shortAction.setDisabled(True)
            self.longAction.setDisabled(True)

        elif isinstance(self.fms.state, state.TomatoState):
            lcd_time = self.fms.remining_time(self.evt, time.time())
            self.label.setText('Counting...')
            self.lcd.display(str(lcd_time))
            self.btn_start.hide()
            self.btn_stop.show()
            self.stopAction.setDisabled(False)
            self.startAction.setDisabled(True)
            self.shortAction.setDisabled(True)
            self.longAction.setDisabled(True)

        elif isinstance(self.fms.state, state.SelectState):
            self.label.setText('Select Pause')
            self.lcd.display(str('00:00'))
            self.btn_start.hide()
            self.btn_stop.hide()
            self.btn_lpause.show()
            self.btn_spause.show()
            self.stopAction.setDisabled(True)
            self.startAction.setDisabled(True)

        elif isinstance(self.fms.state, state.ShortState):
            label_time = self.fms.remining_time(self.evt, time.time())
            self.label.setText('Short Pause')
            self.lcd.display(str(label_time))
            self.btn_lpause.hide()
            self.btn_spause.hide()
            self.btn_stop.show()
            self.stopAction.setDisabled(False)
            self.startAction.setDisabled(True)
            self.shortAction.setDisabled(True)
            self.longAction.setDisabled(True)

        elif isinstance(self.fms.state, state.LongState):
            label_time = self.fms.remining_time(self.evt, time.time())
            self.label.setText('Long Pause')
            self.lcd.display(str(label_time))
            self.btn_lpause.hide()
            self.btn_spause.hide()
            self.btn_stop.show()
            self.stopAction.setDisabled(False)
            self.startAction.setDisabled(True)
            self.shortAction.setDisabled(True)
            self.longAction.setDisabled(True)

    def force_stop(self):
        self.fms.next_state(state.StopEvent(), time.time())

    def set_position(self):
        ''' temp method need read data from config '''
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(screen.width() - size.width(),
                  screen.height() - (size.height()*4))

    def create_tray_icon(self):
        icon = QtGui.QIcon('images/black-tomat.png')
        menu = QtGui.QMenu(self)

        self.startAction = menu.addAction("Start Pomidoro")
        self.startAction.triggered.connect(self.start_tray)

        self.stopAction = menu.addAction("Stop Pomidoro")
        self.stopAction.triggered.connect(self.stop_tray)

        self.shortAction = menu.addAction("Short Pause")
        self.shortAction.triggered.connect(self.short_tray)

        self.longAction = menu.addAction("Long Pause")
        self.longAction.triggered.connect(self.long_tray)

        menu.addSeparator()

        self.forcePomidor = menu.addAction("Force Pomidor")
        self.forcePomidor.triggered.connect(self.start_tray)

        self.forceShort = menu.addAction("Force Short")
        self.forceShort.triggered.connect(self.short_tray)

        self.forceLong = menu.addAction("Force Long")
        self.forceLong.triggered.connect(self.long_tray)

        resetAction = menu.addAction("Reset Pomidoro")
        resetAction.triggered.connect(self.force_stop)
        menu.addSeparator()

        settingAction = menu.addAction("Settings")
        settingAction.triggered.connect(self.dialog.show)
        exitAction = menu.addAction("Quit")
        exitAction.triggered.connect(QtGui.qApp.quit)
        self.trayIcon = QtGui.QSystemTrayIcon(self)
        self.trayIcon.setContextMenu(menu)
        self.trayIcon.setIcon(icon)

    def start_tray(self):
        self.on_btn_start()
        if self.isHidden():
            config.notify('Pomidoro Start')

    def stop_tray(self):
        self.on_btn_stop()
        if self.isHidden():
            config.notify('Pomidoro Stop')

    def short_tray(self):
        self.on_btn_spause()
        if self.isHidden():
            config.notify('Short Pause Start')

    def long_tray(self):
        self.on_btn_lpause()
        if self.isHidden():
            config.notify('Long Pause Start')

    def on_trayicon_activated(self, reason):
        if reason == QtGui.QSystemTrayIcon.DoubleClick:
            if self.isHidden():
                self.show()
            else:
                self.hide()

    def closeEvent(self, event):
        event.ignore()
        self.hide()


class DialogWindow(QtGui.QDialog, dialog.Ui_Dialog):
    def __init__(self, window, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.setWindowTitle("Settings")
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.setFixedSize(self.size())

        self.spinTomat.setValue(int(self.read_settings('ttime')))
        self.spinLong.setValue(int(self.read_settings('lpause')))
        self.spinShort.setValue(int(self.read_settings('spause')))

        self.btnOk.clicked.connect(self.btn_ok_click)
        self.btnCnl.clicked.connect(self.btn_cnl_click)
        self.app = window

    def read_settings(self, key):
        value = config.read_conf("Settings", key)
        return value

    def write_settings(self):
        section = "Settings"
        config.write_conf(section, 'ttime',
                            self.spinTomat.value())
        config.write_conf(section, 'lpause',
                            self.spinLong.value())
        config.write_conf(section, 'spause',
                            self.spinShort.value())
        self.update_time()

    def update_time(self):
        self.app.fms.tomat = int(config.read_conf("Settings", 'ttime')) * 60
        self.app.fms.lpause = int(config.read_conf("Settings", 'lpause')) * 60
        self.app.fms.spause = int(config.read_conf("Settings", 'spause')) * 60

    def btn_ok_click(self):
        self.write_settings()
        self.hide()

    def btn_cnl_click(self):
        self.hide()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('TomatoTimer')

    main = MainWindow()
    main.show()

    sys.exit(app.exec_())
