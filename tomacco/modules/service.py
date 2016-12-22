import dbus
import dbus.service


class DbusService(dbus.service.Object):
    def __init__(self, frame):
        self.frame = frame
        bus_name = dbus.service.BusName('org.prog.tomacco',
                                        bus=dbus.SessionBus())
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
