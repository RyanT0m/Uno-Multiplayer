#!/usr/bin/env python3
import socket

class Client(socket.socket):

    DEFAULT_PACKET_SIZE = 1024

    def __init__(self, *args, **kwargs):
        super.__init__(socket.AF_INET, socket.SOCK_STREAM)

        self.port = kwargs.get("port")
        self.host = kwargs.get("host")
        self.data = None

    def start(self):
        if not host or not port:
            print("[Error] - Host or port variable is empty")

        self.connect((self.host, self.port))

    def send(self, data):
        '''
        Transmits data across the current socket
        inputs:
            data - data in byteform
        outputs:
            None
        '''
        self.sendall(data)

    def recieve(self):
        '''
        Recieve data from current socket
        inputs:
            None
        outputs:
            return -- data in byteform from server
        '''
        return s.recv(Client.DEFAULT_PACKET_SIZE)
