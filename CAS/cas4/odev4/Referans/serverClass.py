#ağ üzerinden veri gönderme veya alma işlemi için kullanılan ağ soketlerini oluşturur
import socket
import queue
import time

class SV():

    def __init__(self,localhost,port):
        self.massages = queue.Queue()#lınan mesajları ve kaynak adreslerini saklamak için kullanılır.
        self.clients = []
        self.localHost = localhost
        self.port = port
        self.server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.server.bind((self.localHost,self.port))
        self.msg= "-------"

    def recieve(self):
        while True:
            try:
                #recv işlevi sadece veriyi alırken, recvfrom işlevi ayrıca bu verinin geldiği kaynağı da döndürür.
                #message: Bu değişken, soketten alınan veriyi içerir. recvfrom işlevi, maksimum 1024 byte uzunluğundaki bir veriyi message değişkenine atar
                #addr: Bu değişken, gelen verinin kaynağını temsil eder. İki öğeli bir tuple (demet) olarak döner. İlk öğe, kaynak IP adresini içerir ve ikinci öğe, kaynak port numarasını içerir. Bu bilgiler, gelen verinin nereden geldiğini belirlemenize yardımcı olur.
                massage,addr = self.server.recvfrom(1024)
                #self message kuyruğu temsil ederken put ise veri ekler
                self.massages.put((massage,addr))
            except:
                pass

    def broadcast(self):
        while True:
            while not self.massages.empty():
                massage, addr= self.massages.get()
                self.msg=massage.decode()# yöntemi, baytları karakterlere çevirmek için kullanılır
            time.sleep(0.25)