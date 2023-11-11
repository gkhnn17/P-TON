import threading
import serverClass
import clientClass
import tkinter as tk


class controlStation():
    def __init__(self):
        self.sv = serverClass.SV("127.0.0.1",9099)# "9099" ve "9990", sunucu ve istemcinin iletişim kurmak için seçilen bağlantı noktalarıdır.
        self.status=clientClass.CL("127.0.0.1", 9990,8090)# 8090 Bu, istemci tarafından kullanılan başka bir bağlantı noktas

        dataThread1 = threading.Thread(target=self.sv.recieve)
        dataThread2 = threading.Thread(target=self.sv.broadcast)
        dataThread1.start()
        dataThread2.start()

        statusThread = threading.Thread(target=self.status.send)
        statusThread.start()



        self.flag = 0
        self.main=tk.Tk()
        self.main.title("CasMarine Kontrol İstasyonu Simülasyonu")

        canvas = tk.Canvas(self.main, height=140, width=300)
        canvas.pack()

        self.start()

    def start(self):
        self.status.massage = "off"
        self.flag = 0
        frame = tk.Frame(self.main)
        frame.place(relwidth=1, relheight=1)
        lb=tk.Label(text="CasMarine Kontrol İstasyonu Simülasyonu")
        lb.place(relx=0.1, rely=0.10, relwidth=0.8)
        buttonStartLoc = tk.Button(frame, text='Başlat', command=self.getLoc)
        buttonStartLoc.place(relx=0.1, rely=0.45, relwidth=0.8)
        self.main.mainloop()


    def getLoc(self):
        self.status.massage = "on"
        frame = tk.Frame(self.main)
        frame.place(relwidth=1, relheight=1)
        buttonStopLoc = tk.Button(frame, text='Bitir', command=self.stopGetLoc)
        buttonStopLoc.place(relx=0.1, rely=0.45, relwidth=0.8)
        lb = tk.Label(text="Cismin Yönü {}".format(self.sv.msg))
        lb.place(relx=0.1, rely=0.10, relwidth=0.8)
        if(self.flag==0):
            self.main.after(200,self.getLoc)
        else:
            self.start()


    def stopGetLoc(self):
        self.flag=1

if __name__ == '__main__':
    cntStation=controlStation()
