import socket
import time

class CL():
    def __init__(self,localhost,portSend,port):
        self.client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)##server =IPV4,UDP
        self.localHost = localhost
        self.portSend = portSend
        self.port = port
        self.client.bind((self.localHost,self.port))
        self.message = 0

    def send(self):
        while True:
            self.client.sendto(f"{self.message}".encode(),(self.localHost,self.portSend))#data,address
            time.sleep(0.5)