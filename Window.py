import abc


class Window():
    def __init__(self):
        pass

    @abc.abstractmethod
    def getRepertoryPath(self):
        ##########################
        # 获得仓库位置
        ##########################
        pass

    @abc.abstractmethod
    def setHeader(self, header):
        ##########################
        # 显示当前用户名称
        # 我的想法是对于命令行的窗口有一个前置显示的内容 所以要set一下
        ##########################
        pass

    @abc.abstractmethod
    def waitForCommand(self):
        ##########################
        # 等待输入命令
        ##########################
        pass

    @abc.abstractmethod
    def showUsers(self, info):
        ##########################
        # 窗口显示其他用户
        ##########################
        pass

    @abc.abstractmethod
    def getAddress(self):
        ##########################
        # 获得ip、port
        ##########################
        pass

    @abc.abstractmethod
    def welcome(self):
        ##########################
        # 欢迎界面
        ##########################
        pass

    @abc.abstractmethod
    def promptError(self, error):
        ##########################
        # 提示错误
        ##########################
        pass

    @abc.abstractmethod
    def prompt(self, error):
        ##########################
        # 提示
        ##########################
        pass

    @abc.abstractmethod
    def showConfig(self, config):
        ##########################
        # 展示预置配置
        ##########################
        pass

    @abc.abstractmethod
    def askForConfig(self):
        ##########################
        # 询问是否需要config
        ##########################
        pass


