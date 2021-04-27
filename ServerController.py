
from Controller import Controller
from Tool import Tool
from Log import Log


class ServerController(Controller):
    def __init__(self, window=None):
        Controller.__init__(self)
        self.tool = Tool()
        self.log = Log()

    def run(self):
        pass
