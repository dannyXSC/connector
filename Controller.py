from Tool import Tool
from Log import Log


class Controller():
    def __init__(self, logPath="", repoPath=""):
        self.log_Path = logPath
        self.repertory_Path = repoPath
        self.tool = Tool()
        self.log = Log()

    def setRepertoryPath(self, path):
        self.repertory_Path = path

    def setLogPath(self, path):
        self.log_Path = path

