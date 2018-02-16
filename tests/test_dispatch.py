from cmdbus import cmdbus, Command


class AddCommand(Command):
    def __init__(self, v1: int, v2: int):
        self.v1 = v1
        self.v2 = v2

    def handle(self):
        return self.v1 + self.v2


def test_dispatch():
    cmd = AddCommand(3, 5)
    result = cmdbus.dispatch(cmd)
    assert result is 8
