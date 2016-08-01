import sys
import time
import signal
import dbus
import dbus.service
import dbus.mainloop.glib
from dbus.mainloop.glib import DBusGMainLoop
from PyQt4 import QtCore, QtGui


# fast fix import error
import os
sys.path.append(os.path.dirname(__file__))

from modules import form
from modules import dialog
from modules import config
from modules import state
from modules import utils


# TODO убрать notify из модели
class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = form.Ui_MainWindow()
        self.ui.setupUi(self)
        self.fms = state.LogicFMS()

        self.dialog = DialogWindow(self)
        self.dialog.update_time()

        # init show window
        self.setWindowTitle("Tomacco")
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.set_position()
        self.ui.btn_lpause.hide()
        self.ui.btn_spause.hide()
        self.ui.btn_stop.hide()

        # timer
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_app)

        # lcd
        self.ui.lcd.display('00:00')

        # tray
        self.create_tray_icon()
        self.trayIcon.activated.connect(self.on_trayicon_activated)
        self.trayIcon.show()

        # connect
        self.ui.btn_start.clicked.connect(self.on_btn_start)
        self.ui.btn_stop.clicked.connect(self.on_btn_stop)
        self.ui.btn_spause.clicked.connect(self.on_btn_spause)
        self.ui.btn_lpause.clicked.connect(self.on_btn_lpause)

    def on_btn_start(self):
        icon = utils.image_tray('red-tomat.png')
        enable_start = config.read_conf('run_commands', 'active_before')
        if enable_start == 1:
            utils.run('before')
        self.trayIcon.setIcon(icon)
        self.fms.next_state(state.StartEvent, time.time())
        self.timer.start(100)

    def on_btn_stop(self):
        enable_finish = config.read_conf('run_commands', 'active_after')
        if enable_finish == 1 and \
                isinstance(self.fms.state, state.TomatoState):
            utils.run('after')
        icon = utils.image_tray('init-tomat.png')
        self.trayIcon.setIcon(icon)
        self.fms.next_state(state.StopEvent(), time.time())

    def on_btn_spause(self):
        icon = utils.image_tray('short-tomat.png')
        self.trayIcon.setIcon(icon)
        self.fms.next_state(state.ShortEvent(), time.time())
        self.timer.start(100)

    def on_btn_lpause(self):
        icon = utils.image_tray('long-tomat.png')
        self.trayIcon.setIcon(icon)
        self.fms.next_state(state.LongEvent(), time.time())
        self.timer.start(100)

    def update_app(self):
        t = time.time()
        self.evt = state.TickEvent()
        self.fms.next_state(self.evt, t)
        self.update_window()

    def view_time(self, stime):
        amount = self.fms.remining_time(self.evt, time.time())
        remining_time = time.strftime("%M:%S",
                                      time.gmtime(stime - amount))
        return str(remining_time)

    def tomacco_label(self):
        return "Tomacco - " + str(self.fms.tomacco)

    def update_window(self):
        if isinstance(self.fms.state, state.InitState):
            self.timer.stop()
            icon = utils.image_tray('init-tomat.png')
            self.trayIcon.setIcon(icon)
            self.trayIcon.setToolTip(self.tomacco_label())
            self.ui.status_bar.showMessage("Tomacco - " +
                                           str(self.fms.tomacco))
            self.ui.lcd.display(str('00:00'))
            self.ui.btn_start.show()
            self.ui.btn_stop.hide()
            self.ui.btn_lpause.hide()
            self.ui.btn_spause.hide()
            self.startAction.setDisabled(False)
            self.stopAction.setDisabled(True)
            self.shortAction.setDisabled(True)
            self.longAction.setDisabled(True)

        elif isinstance(self.fms.state, state.TomatoState):
            self.ui.btn_stop.setText('Stop \n Tomacco')
            self.ui.status_bar.showMessage(self.tomacco_label() +
                                           ' Counting...')
            self.ui.lcd.display(self.view_time(self.fms.tomat))
            self.trayIcon.setToolTip(self.tomacco_label() +
                                     '\n' +
                                     self.view_time(self.fms.tomat))
            self.ui.btn_start.hide()
            self.ui.btn_stop.show()
            self.stopAction.setDisabled(False)
            self.startAction.setDisabled(True)
            self.shortAction.setDisabled(True)
            self.longAction.setDisabled(True)

        elif isinstance(self.fms.state, state.SelectState):
            self.timer.stop()
            icon = utils.image_tray('init-tomat.png')
            self.trayIcon.setIcon(icon)
            self.trayIcon.setToolTip(self.tomacco_label())
            self.ui.status_bar.showMessage(self.tomacco_label() +
                                           " Select Pause")
            self.ui.lcd.display(str('--:--'))
            self.ui.btn_start.hide()
            self.ui.btn_stop.hide()
            self.ui.btn_lpause.show()
            self.ui.btn_spause.show()
            self.stopAction.setDisabled(True)
            self.startAction.setDisabled(True)
            self.shortAction.setDisabled(False)
            self.longAction.setDisabled(False)

        elif isinstance(self.fms.state, state.ShortState):
            self.ui.status_bar.showMessage(self.tomacco_label() +
                                           " Short Pause")
            self.ui.lcd.display(self.view_time(self.fms.spause))
            self.trayIcon.setToolTip(self.tomacco_label() +
                                     '\n' +
                                     self.view_time(self.fms.spause))
            self.ui.btn_lpause.hide()
            self.ui.btn_spause.hide()
            self.ui.btn_start.hide()
            self.ui.btn_stop.show()
            self.ui.btn_stop.setText('Stop \n Short Pause')
            self.stopAction.setDisabled(False)
            self.startAction.setDisabled(True)
            self.shortAction.setDisabled(True)
            self.longAction.setDisabled(True)

        elif isinstance(self.fms.state, state.LongState):
            self.ui.status_bar.showMessage(self.tomacco_label() +
                                           " Long Pause")
            self.ui.lcd.display(self.view_time(self.fms.lpause))
            self.trayIcon.setToolTip(self.tomacco_label() +
                                     '\n' +
                                     self.view_time(self.fms.lpause))
            self.ui.btn_lpause.hide()
            self.ui.btn_spause.hide()
            self.ui.btn_start.hide()
            self.ui.btn_stop.show()
            self.ui.btn_stop.setText('Stop \n Long Pause')
            self.stopAction.setDisabled(False)
            self.startAction.setDisabled(True)
            self.shortAction.setDisabled(True)
            self.longAction.setDisabled(True)

    def forse_stop(self):
        self.fms.tomacco = 0
        self.fms.set_state(state.InitState())
        self.update_window()

    def set_position(self):
        self.width = config.read_conf("Settings", "width")
        self.height = config.read_conf("Settings", "height")
        self.move(self.width, self.height)

    def create_tray_icon(self):
        icon = utils.image_tray('init-tomat.png')
        menu = QtGui.QMenu(self)

        self.startAction = menu.addAction("Start Tomacco")
        self.startAction.triggered.connect(self.start_tray)

        self.stopAction = menu.addAction("Stop")
        self.stopAction.triggered.connect(self.stop_tray)

        self.shortAction = menu.addAction("Short Pause")
        self.shortAction.triggered.connect(self.short_tray)

        self.longAction = menu.addAction("Long Pause")
        self.longAction.triggered.connect(self.long_tray)

        menu.addSeparator()

        self.forceTomacco = menu.addAction("Force Tomacco")
        self.forceTomacco.triggered.connect(self.start_tray)

        self.forceShort = menu.addAction("Force Short")
        self.forceShort.triggered.connect(self.short_tray)

        self.forceLong = menu.addAction("Force Long")
        self.forceLong.triggered.connect(self.long_tray)

        resetAction = menu.addAction("Reset Tomacco")
        resetAction.triggered.connect(self.forse_stop)
        menu.addSeparator()

        settingAction = menu.addAction("Settings")
        settingAction.triggered.connect(self.dialog.show)
        exitAction = menu.addAction("Quit")
        exitAction.triggered.connect(self.quit_app)

        self.trayIcon = QtGui.QSystemTrayIcon(self)
        self.trayIcon.setContextMenu(menu)
        self.trayIcon.setIcon(icon)

    def quit_app(self):
        config.write_conf("Settings", "width",
                          self.x())
        config.write_conf("Settings", "height",
                          self.y())
        QtGui.qApp.quit()

    def start_tray(self):
        self.on_btn_start()
        if self.isHidden():
            config.notify('Tomacco Start')

    def stop_tray(self):
        self.on_btn_stop()
        if self.isHidden():
            config.notify('Tomacco Stop')

    def short_tray(self):
        self.on_btn_spause()
        if self.isHidden():
            config.notify('Short Pause Start')

    def long_tray(self):
        self.on_btn_lpause()
        if self.isHidden():
            config.notify('Long Pause Start')

    def on_trayicon_activated(self, reason):
        if reason == QtGui.QSystemTrayIcon.Trigger:
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

        self.spinTomat.setValue(self.read_settings('ttime'))
        self.spinLong.setValue(self.read_settings('lpause'))
        self.spinShort.setValue(self.read_settings('spause'))

        self.start_edit.setText(config.read_conf('run_commands', 'before', True))
        self.finish_edit.setText(config.read_conf('run_commands', 'after', True))

        enable_start = config.read_conf('run_commands', 'active_before')
        enable_finish = config.read_conf('run_commands', 'active_after')

        if enable_start == 1:
            self.start_run.setChecked(True)

        if enable_finish == 1:
            self.finish_run.setChecked(True)

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

        config.write_conf('run_commands', 'before',
                          self.start_edit.text())
        config.write_conf('run_commands', 'after',
                          self.finish_edit.text())
        if self.start_edit.isEnabled():
            config.write_conf('run_commands', 'active_before', '1')
        else:
            config.write_conf('run_commands', 'active_before', '0')
        if self.finish_edit.isEnabled():
            config.write_conf('run_commands', 'active_after', '1')
        else:
            config.write_conf('run_commands', 'active_after', '0')

        self.update_time()

    def update_time(self):
        self.app.fms.tomat = config.read_conf("Settings", 'ttime') * 60
        self.app.fms.lpause = config.read_conf("Settings", 'lpause') * 60
        self.app.fms.spause = config.read_conf("Settings", 'spause') * 60

    def btn_ok_click(self):
        self.write_settings()
        self.hide()

    def btn_cnl_click(self):
        self.hide()


class DbusService(dbus.service.Object):
    def __init__(self, frame):
        self.frame = frame
        bus_name = dbus.service.BusName('org.prog.tomacco', bus=dbus.SessionBus())
        dbus.service.Object.__init__(self, bus_name, '/org/prog/tomacco')

    @dbus.service.method('org.prog.tomacco')
    def start(self):
        self.frame.on_btn_start()

    @dbus.service.method('org.prog.tomacco')
    def stop(self):
        self.frame.on_btn_stop()

    @dbus.service.method('org.prog.tomacco')
    def spause(self):
        self.frame.on_btn_spause()

    @dbus.service.method('org.prog.tomacco')
    def lpause(self):
        self.frame.on_btn_lpause()

    @dbus.service.method('org.prog.tomacco')
    def show(self):
        self.frame.show()

    @dbus.service.method('org.prog.tomacco')
    def hide(self):
        self.frame.hide()


def main():
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('TomaccoTimer')

    DBusGMainLoop(set_as_default=True)

    window = MainWindow()
    service=DbusService(window)
    window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
