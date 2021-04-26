import os

from Controller import Controller
from Client import Client
from TerminalWindow_Client import TerminalWindow_Client
from Log import Log


class ClientController(Controller):
    def __init__(self, window=None):
        Controller.__init__(self)
        self.client_Handle = Client()
        if window != None:
            self.window_Handle = window
        else:
            self.window_Handle = TerminalWindow_Client()
        self.log = Log()

    def run(self):
        self.window_Handle.welcome()
        self.window_Handle.setHeader(">> ")

        # get path
        while True:
            repertory_Path = self.window_Handle.getRepertoryPath()
            if os.path.isabs(repertory_Path):
                self.repertory_Path = repertory_Path
                break
            self.window_Handle.promptError(
                "Invalid path! It must be a abs path!")

        # get name
        while True:
            name = self.window_Handle.getUserName()
            if len(name) <= 20 and len(name) > 0:
                self.name = name
                break
            self.window_Handle.promptError("Name[1-20] invalid!")
        self.log.write(self.repertory_Path, f"{self.name} log in")

        self.window_Handle.setHeader(f"({self.name}) >> ")
        self.server_Ip, self.server_Port = self.window_Handle.getAddress()
        self.log.write(self.repertory_Path,
                       f"{self.name} set ip({self.server_Ip}), port(self.server_Port)")

    def manageCommand(self):
        pass


if __name__ == '__main__':
    handle = ClientController()
    handle.run()
