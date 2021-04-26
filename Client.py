import re
import socket
import json
import struct


class Client():
    def __init__(self, name="", ip="", port=-1):
        if isinstance(name, str) and isinstance(ip, str) and isinstance(port, int):
            self.name = name
            self.ip_server = ip
            self.port_server = port
            self.isConnect = False
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.setblocking(False)
        else:
            raise Exception("Invalid input!")

    def set_Ip(self, ip, port=-1):
        if isinstance(ip, str) and isinstance(port, int):
            if re.match('^([0-9]|[0-9][0-9]|[01][0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[0-9][0-9]|[01][0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[0-9][0-9]|[01][0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[0-9][0-9]|[01][0-9][0-9]|2[0-4][0-9]|25[0-5])$',
                        ip, flags=0) != None:
                self.ip_server = ip
                self.port_server = port
                if self.isConnect == True:
                    self.socket.close()
                    self.isConnect = False
            else:
                raise Exception("Ip format error!")
        else:
            raise Exception("Invalid input!")

    def set_Port(self, port):
        if isinstance(port, int):
            self.port_server = port
            if self.isConnect == True:
                self.socket.close()
                self.isConnect = False
        else:
            raise Exception("Invalid input!")

    def set_Name(self, name):
        if isinstance(name, str):
            self.name = name
        else:
            raise Exception("Invalid input!")

    def is_Connect(self):
        return self.isConnect

    def connect(self):
        if self.isConnect == True:
            raise Exception("Currently connected!")
        elif self.ip_server == "" or self.port_server == -1:
            raise Exception("Have not initialized!")
        else:
            try:
                self.socket.connect((self.ip_server, self.port_server))
                self.isConnect = True
            except:
                raise Exception("Connect Error!")

    ############################################
    # 发送包头
    ############################################
    def send_Head(self, header):
        if self.isConnect == False:
            raise Exception("Have not connected yet!")
        if not isinstance(header, dict):
            raise Exception("Invalid input!")
        try:
            head_byte = json.dumps(header).encode('utf-8')
            head_len = len(head_byte)
            head_struct = struct.pack('i', head_len)
            self.socket.send(head_struct+head_byte)
        except:
            raise Exception("Send head failure!")

    def send_Data(self, data):
        if self.isConnect == False:
            raise Exception("Have not connected yet!")
        if not isinstance(data, bytes):
            raise Exception("Invalid input!")
        try:
            self.socket.send(data)
        except:
            raise Exception("Send data failure!")

    def receive_Head(self):
        if self.isConnect == False:
            raise Exception("Have not connected yet!")
        try:
            len_struct = self.socket.recv(4)
            if not len(len_struct):
                raise Exception("Message miss!")
            head_len = struct.unpack('i', len_struct)
            head_byte = b''
            recv_size = 0
            while head_len-recv_size >= 1024:
                curByte = self.socket.recv(1024)
                head_byte += curByte
                recv_size = len(curByte)
            head_byte += self.socket.recv(head_len-recv_size)
            header = json.loads(head_byte.decode('utf-8'))
            if not isinstance(header, dict):
                raise Exception("Received object is not header!")
            return header
        except:
            raise Exception("Receive header failure!")

    def receive_Data(self, len_Data):
        if self.isConnect == False:
            raise Exception("Have not connected yet!")
        try:
            recv_size = 0
            data_byte = b''
            while len_Data-recv_size >= 1024:
                curByte = self.socket.recv(1024)
                data_byte += curByte
                recv_size += len(curByte)
            data_byte += self.socket.recv(len_Data-recv_size)
            return data_byte
        except:
            raise Exception("Receive data failure!")
