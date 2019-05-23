#!/usr/bin/env python3
import socket

class Server(socket.socket):
    '''
    Server represents the server side communication for Uno
    '''
    def __init__(self, *args, **kwargs):
        super.__init__(socket.AF_INET, socket.SOCK_STREAM)

        self.port = kwargs.get("port")
        self.host = kwargs.get("host")
        self.data = None

        if not host:
            self.host = self._getHost()
        if not port:
            self.port = self._getPort()

    def _getHost(self):
        '''
        Get host will attempt to return the host Ipv4 address using socket library
        inputs
            None
        outputs
            return -- string of Ipv4 address
        '''
        try:
            return socket.gethostbyname(socket.gethostname())
        except:
            print("[Error] - Unable to obtain host IP address")

    def _getPort(self):
        '''
        Will get a random port to initiate the connection
        inputs
            None
        outputs
            return -- integer value for port
        '''
        return random.randint(4000,5000)

    def start(self):
        '''
        Starts listening on host and port, then connects to first host and stores recieved
        data until no more data is sent
        inputs
            None
        outputs
            None
        '''
        self.bind((self.host,self.port))
        s.listen()
        connection, address = s.accept()

        with connection:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                self.data += data
