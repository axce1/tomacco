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


class FMS():
    def __init__(self):
        self.state = InitState()

    def next_state(self):
        pass
