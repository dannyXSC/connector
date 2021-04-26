import socket


class Server():
    def __init__(self):
        self.port = 5050
        self.ip = socket.gethostbyname(socket.gethostname())
        self.addr = (self.ip, self.port)
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.addr)
