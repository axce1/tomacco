from .config import notify


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
    pass


class SelectState(State):
    pass


class TomatoState(State):

    def __init__(self, stime):
        """
        stime - state start time
        """
        self.stime = stime

    def get_time(self):
        return self.stime


class ShortState(State):

    def __init__(self, stime):
        self.stime = stime

    def get_time(self):
        return self.stime


class LongState(State):

    def __init__(self, stime):
        self.stime = stime

    def get_time(self):
        return self.stime


class LogicFMS():
    def __init__(self):
        self.state = InitState()
        self.tomacco = 0

    def remining_time(self, event, stime):
        if isinstance(event, TickEvent):
            count = stime - self.state.get_time()
            return count

    def set_state(self, state):
        self.state = state

    def next_state(self, event, stime):
        if isinstance(self.state, InitState):
            if event == StartEvent:
                self.state = TomatoState(stime)
            elif isinstance(event, ShortEvent):
                self.state = ShortState(stime)
            elif isinstance(event, LongEvent):
                self.state = LongState(stime)

        elif isinstance(self.state, TomatoState):
            if isinstance(event, TickEvent):
                if self.tomat <= int(stime - self.state.get_time()):
                    self.state = SelectState()
                    self.tomacco += 1
                    notify('Count Tomacco Stop')
            elif isinstance(event, StopEvent):
                self.state = InitState()
            elif isinstance(event, LongEvent):
                self.state = LongState(stime)
            elif isinstance(event, ShortEvent):
                self.state = ShortState(stime)

        elif isinstance(self.state, SelectState):
            if event == StartEvent:
                self.state = TomatoState(stime)
            elif isinstance(event, ShortEvent)
                self.state = ShortState(stime)
            elif isinstance(event, LongEvent):
                self.state = LongState(stime)

        elif isinstance(self.state, ShortState):
            if isinstance(event, TickEvent):
                if self.spause <= int(stime - self.state.get_time()):
                    self.state = InitState()
                    notify('Short Pause Stop')
            elif isinstance(event, StopEvent):
                self.state = InitState()
            elif isinstance(event, LongEvent):
                self.state = LongState(stime)
            elif isinstance(event, StartEvent):
                self.state = TomatoState(stime)

        elif isinstance(self.state, LongState):
            if isinstance(event, TickEvent):
                if self.lpause <= int(stime - self.state.get_time()):
                    self.state = InitState()
                    notify('Long Pause Stop')
                    self.tomacco = 0
            elif isinstance(event, StopEvent):
                self.state = InitState()
                self.tomacco = 0
            elif isinstance(event, ShortEvent):
                self.state = ShortState(stime)
            elif isinstance(event, StartEvent):
                self.state = TomatoState(stime)
