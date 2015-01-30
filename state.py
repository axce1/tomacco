import time
import os

from modules import config


State = type("State", (), {})


class TickEvent:
    ''' tick event '''
    pass


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
        self.pomidor = 0

    def set_state(self, name):
        self.state = name

    @property
    def get_state(self):
        return self.state.name

    def remining_time(self, event, stime):
        if isinstance(event, TickEvent):
            count = stime - self.state.get_time()
            remining_time = time.strftime("%M:%S", time.gmtime(count))
            return remining_time

    def next_state(self, event, stime):
        if isinstance(self.state, InitState):
            if event == StartEvent:
                self.state = TomatoState(stime)

        elif isinstance(self.state, TomatoState):
            if isinstance(event, TickEvent):
                if self.tomat <= int(stime - self.state.get_time()):
                    self.state = SelectState()
                    self.pomidor += 1
                    config.notify('Count Tomat Stop')
            elif isinstance(event, StopEvent):
                self.state = InitState()
            elif isinstance(event, LongEvent):
                self.state = LongState(stime)
            elif isinstance(event, ShortEvent):
                self.state = ShortState(stime)

        elif isinstance(self.state, SelectState):
            if isinstance(event, ShortEvent):
                self.state = ShortState(stime)
            elif isinstance(event, LongEvent):
                self.state = LongState(stime)

        elif isinstance(self.state, ShortState):
            if isinstance(event, TickEvent):
                if self.spause <= int(stime - self.state.get_time()):
                    self.state = InitState()
                    config.notify('Short Pause Stop')
            elif isinstance(event, StopEvent):
                self.state = InitState()
            elif isinstance(event, LongEvent):
                self.state = LongState(stime)
            elif isinstance(event, StartEvent):
                self.state = StartState(stime)

        elif isinstance(self.state, LongState):
            if isinstance(event, TickEvent):
                if self.lpause <= int(stime - self.state.get_time()):
                    self.state = InitState()
                    config.notify('Long Pause Stop')
                    self.pomidor = 0
            elif isinstance(event, StopEvent):
                self.state = InitState()
            elif isinstance(event, ShortEvent):
                self.state = ShortState(stime)
            elif isinstance(event, StartEvent):
                 self.state = StartState(stime)
