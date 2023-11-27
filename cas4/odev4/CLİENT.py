import socket


HEADER =64
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MSG ="DISCONNECT"
SERVER ="192.168.1.33"
ADDR = (SERVER,PORT)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_lenght = str(msg_length).encode(FORMAT)
    send_lenght += b" "* (HEADER - len(send_lenght))
    client.send(send_lenght)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))#msg from server

send("Hello world")
input()
send("Hello0000")
send("Hello world")
send(DISCONNECT_MSG)


"""
# An example script to connect to Google using socket
# programming in Python
import socket # for socket
import sys
 
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ("Socket successfully created")
except socket.error as err:
    print ("socket creation failed with error %s" %(err))
 
# default port for socket
port = 80
 
try:
    host_ip = socket.gethostbyname('www.google.com')
except socket.gaierror:
 
    # this means could not resolve the host
    print ("there was an error resolving the host")
    sys.exit()
 
# connecting to the server
s.connect((host_ip, port))
 
print ("the socket has successfully connected to google")
"""