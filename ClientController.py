import os
import re
import sys
import json

from Controller import Controller
from Client import Client
from TerminalWindow import TerminalWindow
from Log import Log
from Config import Config
from Tool import Tool

class ClientController(Controller):
    def __init__(self, window=None):
        Controller.__init__(self)
        self.client_Handle = Client()
        if window != None:
            self.window_Handle = window
        else:
            self.window_Handle = TerminalWindow()
        self.log = Log()
        self.cfg=Config()
        self.tool=Tool()

    def run(self):
        self.window_Handle.welcome()
        self.window_Handle.setHeader(">> ")
        # require wheather to use config

        isPrepared=False
        config_path=sys.path[0]+'/config'

        if self.window_Handle.askForConfig()==True:
            config=self.cfg.read(config_path)
            config=self.window_Handle.showConfig(config)
            if config!=None:
                isPrepared=True
                self.name=config["Name"]
                self.window_Handle.setHeader(f"({self.name}) >> ")
                self.server_Ip, self.server_Port=config["Ip"],config["Port"]
                self.repertory_Path=config["Path"]
                self.log.write(self.repertory_Path,f"use config {str(config)}")
        
        if isPrepared==False:
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

            self.cfg.write(config_path,{"Name":self.name,"Ip":self.server_Ip,"Port":self.server_Port,"Path":self.repertory_Path})
        
        self.manageCommand()

    def manageCommand(self):
        try:
            while True:
                command=self.window_Handle.waitForCommand()
                self.log.write(self.repertory_Path,f"{self.name} input command: {command}")
                if command=='quit' or command=='q' or command=='Q':
                    if self.client_Handle.is_Connect==True:
                        header={"Action":"quit"}
                        self.client_Handle.send_Head(header)
                        self.client_Handle.close()
                    self.window_Handle.prompt("\033[0;31;40mEND\033[0m\n")
                    self.log.write(self.repertory_Path,f"{self.name} quit")
                    break
                elif re.match('^ *[Ss][Ee][Nn][Dd] *',command,flags=0)!=None:
                    pos=re.match('^ *[Ss][Ee][Nn][Dd] *',command,flags=0).span()[1]
                    info=command[pos:].strip()

                    self.window_Handle.promptHint("connecting...")
                    if self.client_Handle.is_Connect==False:
                        self.client_Handle.set_Address(self.server_Ip,self.server_Port)
                        self.client_Handle.connect()

                    if os.path.exists(info):
                        try:
                            self.window_Handle.promptHint("loading...")
                            info=self.tool.getTreeInfo(info)

                            byte_Message=json.dumps(info).encode("utf-8")
                            header={"Action":"sendF","Size":len(byte_Message)}
                            self.client_Handle.send_Head(header)
                            self.client_Handle.send_Data(byte_Message)
                        except:
                            raise Exception("SendF failure!")
                    else:
                        try:
                            #TODO:
                            pass
                        except:
                            raise Exception("Send txt failure!")
                    self.window_Handle.promptSuccess("Send successfully!")

                    self.log.write(self.repertory_Path,f"{self.name} send")

                else:
                    self.window_Handle.promptError('Input error!')
        except:
            raise Exception("Manage command error!")


if __name__ == '__main__':
    handle = ClientController()
    handle.run()
