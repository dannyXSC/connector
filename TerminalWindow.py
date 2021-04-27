import re
from prettytable import PrettyTable

from Window import Window


class TerminalWindow(Window):
    def __init__(self):
        Window.__init__(self)
        self.header = "(NotSet): "

    def getUserName(self):
        print("Please input your name...")
        print(self.header, end='')
        name = input()
        print()
        return name

    def getAddress(self):
        while True:
            print("Please input server ip...")
            print(self.header, end='')
            ip = input()
            print()
            if re.match('^([0-9]|[0-9][0-9]|[01][0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[0-9][0-9]|[01][0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[0-9][0-9]|[01][0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[0-9][0-9]|[01][0-9][0-9]|2[0-4][0-9]|25[0-5])$',
                        ip, flags=0) != None:
                print("Please input server port...")
                print(self.header, end='')
                port = input()
                print()
                if port.isdigit() == True:
                    return ip, int(port)
                else:
                    self.promptError(
                        f"Port({port}) is invalid! Please retype!\n")
            else:
                self.promptError(f"Ip({ip}) is invalid! Please retype!\n")

    def setHeader(self, header):
        self.header = header

    def welcome(self):
        title = "Terminal Window [Client]"
        title_len = 40
        print("="*title_len)
        print(' '*((title_len-len(title))//2)+title)
        print("="*title_len)

    def waitForCommand(self):
        print("Please input your command:")
        print(self.header, end='')
        return input()

    def showOtherUsers(self, info):
        if not isinstance(info, list):
            raise Exception("Invalid input!")
        try:
            cnt = 0
            output = PrettyTable()
            output.field_names = ["Id", "Name", "Ip", "Port"]
            for user in info:
                output.add_row([cnt, user["Name"], user["Ip"], user["Port"]])
                cnt += 1

            title = "User List"
            title_len = 40
            print("-"*title_len)
            print(' '*((title_len-len(title))//2), title)
            print("-"*title_len)
            print(output)

        except:
            raise Exception("Show other users failure!")

    def getRepertoryPath(self):
        print("Please set your repertory path...")
        print(self.header, end='')
        path = input()
        print()
        return path

    def promptError(self, error):
        print(f"\033[0;31;40mERROR:\033[0m {error}\n")

    def prompt(self, pmt):
        print(pmt)
    
    def promptHint(self,hint):
        print(f"\033[0;33;40mHint:\033[0m {hint}\n")

    def promptSuccess(self,success):
        print(f"\033[0;32;40mSuccess:\033[0m {success}\n")

    def showConfig(self, config):
        if config==None:
            self.promptError("You do not have config!")
            return None
        if not isinstance(config, list):
            raise Exception("Invalid input!")
        try:
            number_config = len(config)
            if number_config<=0:
                self.promptError("Have no config!")
                return None
            cnt = 0
            output = PrettyTable()
            output.field_names = ["Id","Name", "Ip", "Port","Repetroy path"]
            for cfg in config:
                output.add_row([cnt, cfg["Name"], cfg["Ip"], cfg["Port"],cfg["Path"]])
                cnt += 1

            title = "Config List"
            title_len = 80
            print("-"*title_len)
            print(' '*((title_len-len(title))//2), title)
            print("-"*title_len)
            print(output)

            while True:
                print(f'[0-{number_config-1}](q/Q to quit): ',end='')
                command=input()
                if command!='' and command.isdigit()==True and( int(command)>=0 and int(command)<number_config):
                    print()
                    return config[int(command)]
                elif command=='q' or command=='Q':
                    return None
                self.promptError("Invalid input!")
        except:
            raise Exception("Show config failure!")

    def askForConfig(self):
        while True:
            print('Do you want to use config?')
            command=input('[y/n]: ')
            if command=='y' or command=='Y' :
                return True
            elif command=='n' or command=='N':
                return False
            self.promptError("Invalid input!")


if __name__ == '__main__':
    # test
    windowHandle = TerminalWindow_Client()
    windowHandle.welcome()
    windowHandle.setHeader(">> ")
    info = list()
    '''
    for i in range(5):
        name = windowHandle.getUserName()
        ip, port = windowHandle.getAddress()
        info.append({"Name": name, "Ip": ip, "Port": port})
    windowHandle.showOtherUsers(info)
    windowHandle.waitForCommand()
    '''
    info=[{"Name":"1","Ip":1,"Port":1,"Path":1}]
    config=windowHandle.showConfig(info)
    print(config)
