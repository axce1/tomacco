State = type("State", (), {})


class InitState(State):
    pass


class SelectState(State):
    pass


class TomatoState(State):
    pass


class ShortState(State):
    pass


class LongState(State):
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
