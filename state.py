import time

State = type("State", (), {})


class TickEvent():

    def __init__(self, ctime):
        """
        ctime - current time
        """
        self.ctime = ctime

    def get_time(self):
        return self.ctime


class StartEvent:
    ''' push start button '''
    pass


class StopEvent:
    ''' push stop button '''
    pass


class ShortEvent:
    ''' push short pause button '''
    pass


class LongEvent:
    ''' push long pause button '''
    pass


class InitState(State):

    def __init__(self):
        self.name = 'init'


class SelectState(State):

    def __init__(self):
        self.name = 'select'


class TomatoState(State):

    def __init__(self, stime):
        """
        stime - state start time
        """
        self.stime = stime
        self.name = 'tomato'

    def get_time(self):
        return self.stime


class ShortState(State):

    def __init__(self, stime):
        self.stime = stime
        self.name = 'short'

    def get_time(self):
        return self.stime


class LongState(State):

    def __init__(self, stime):
        self.stime = stime
        self.name = 'long'

    def get_time(self):
        return self.stime


class LogicFMS():
    def __init__(self):
        self.state = InitState()

    def set_state(self, name):
        self.state = name

    @property
    def get_state(self):
        return self.state.name

    def next_state(self, event, stime=None):

        if isinstance(self.state, InitState):
            if event == StartEvent:
                self.state = TomatoState(stime)

        elif isinstance(self.state, TomatoState):
            if event == TickEvent:
                if 6 == int(TickEvent.get_time(self) - self.state.get_time()):
                    self.state = SelectState()
            elif event == StopEvent:
                self.state = InitState()

        elif isinstance(self.state, SelectState):
            if event == ShortEvent:
                self.state = ShortState()
            elif event == LongEvent:
                self.state = LongState()

        elif isinstance(self.state, ShortState):
            if event == TickEvent:
                if 6 == (TickEvent.get_time - ShortState.get_time):
                    self.state = SelectState()
            elif event == StopEvent():
                self.state = InitState()

        elif isinstance(self, LongState):
            if event == TickEvent:
                if 6 == (TickEvent.get_time - LongState.get_time):
                    self.state = SelectState()
            elif event == StopEvent:
                self.state = InitState()
