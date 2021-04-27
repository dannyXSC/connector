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
            # TODO:
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

    def showUsers(self, info):
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


if __name__ == '__main__':
    # test
    windowHandle = TerminalWindow()
    windowHandle.welcome()
    windowHandle.setHeader(">> ")
    info = list()
    for i in range(5):
        name = windowHandle.getUserName()
        ip, port = windowHandle.getAddress()
        info.append({"Name": name, "Ip": ip, "Port": port})
    windowHandle.showUsers(info)
    windowHandle.waitForCommand()
