import socket
import queue
import time

class SV():
    def __init__(self, localhost, port):
        self.messages  = queue.Queue()  # total messages
        self.clients = []
        self.localHost = localhost
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server.bind((self.localHost, self.port))  # connect
        self.msg = "-----------"  # to messages

    def receive(self):
        print(f"[LİSTENİNG] server {self.localHost}")
        while True:
            try:
                message, addr = self.server.recvfrom(1024)
                self.messages.put((message, addr))
            except:
                pass

    def broadcast(self):
        print(F"[NEW CONNECTION] connected")
        while True:
            while not self.messages.empty():
                message, addr = self.messages.get()
                self.msg = message.decode()
            time.sleep(0.55)
