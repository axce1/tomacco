State = type("State", (), {})


class TickEvent(current_time):
    pass


class StartEvent:
    pass


class StopEvent:
    pass


class ShortEvent:
    pass


class LongEvent:
    pass


class InitState(State):
    pass


class SelectState(State):
    pass


class TomatoState(State, init_time):
    pass


class ShortState(State, init_time):
    pass


class LongState(State, init_time):
    pass


class LogicFMS():
    def __init__(self):
        self.state = InitState()

    def set_state(self, name):
        self.state = name

    def get_state(self):
        return self.state

    def next_state(self, handler):
        if isinstance(self.state, InitState()):
            self.set_state(TomatoState())
