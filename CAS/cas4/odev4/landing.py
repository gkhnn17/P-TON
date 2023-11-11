import landingServer
import threading

class Writer():
    def __init__(self):
        self.status = landingServer.SV("127.0.0.1",9099)

        dataThread1 = threading.Thread(target=self.status.broadcast)
        dataThread1.start()

    def write(self):
        while True:
                if self.status.msg =="on":
                    file = open("locs.txt","w")
                    file.write(self.status.msg)
                    print("selam")
if __name__ =="__main__":
     writer = Writer()