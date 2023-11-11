import socket
import time

class CL():
    def __init__(self,localhost,portSend,port):
        self.client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)#server =IPV4,UDP
        self.localHost = localhost#Yerel ana bilgisayarın adını veya IP adresini depolar.
        self.portSend=portSend#İletilerin gönderileceği port numarasını saklar.
        self.port = port# İstemci soketinin bağlanacağı port numarasını saklar.
        self.client.bind((self.localHost, self.port))# İstemci soketini belirtilen yerel ana bilgisayara ve porta bağlar.
        self.massage=0#Bu yöntem, düzenli aralıklarla ileti göndermek için kullanılır.

    def send(self):
        while True:
            self.client.sendto(f"{self.massage}".encode(), (self.localHost, self.portSend))#Mevcut self.massage değerini, belirtilen ana makine ve porta bir UDP ileti olarak gönderir. İleti encode() kullanılarak baytlara dönüştürülür.
            time.sleep(0.2)