import threading
import landingServer
import landingClient
import tkinter as tk
import sys


class landingContral():
    def __init__(self):
        self.sv = landingServer.SV("127.0.0.1",9099)# "9099" ve "9990", sunucu ve istemcinin iletişim kurmak için seçilen bağlantı noktalarıdır.
        self.status = landingClient.CL("127.0.0.1",9990,8090)

        dataThread1 = threading.Thread(target=self.sv.receive)
        dataThread2 = threading.Thread(target=self.sv.broadcast)
        dataThread1.start()
        dataThread2.start()

        statusThread = threading.Thread(target=self.status.send)
        statusThread.start()

        self.flag = 0
        self.main = tk.Tk()
        self.main.title("Landing Kontral İstasyonu")

        canvas = tk.Canvas(self.main,height=140,width=300)
        canvas.pack()

        """self.main.protocol("WM_DELETE_WINDOW", self.on_closing)"""

        self.start()



    def start(self):
        self.status.message = "off"
        
        self.flag= 0
        frame = tk.Frame(self.main)
        frame.place(relwidth=1,relheight=1)
        lb = tk.Label(text="Landing Kontrol İstasyonu")
        lb.place(relx=0.1,rely=0.10,relwidth=0.8)
        buttonStartLoc = tk.Button(frame,text="Başlat",command=self.getLoc)
        buttonStartLoc.place(relx=0.1,rely=0.45,relwidth=0.8)
        self.main.mainloop()

    def getLoc(self):
        self.status.message = "on"
        frame = tk.Frame(self.main)
        frame.place(relheight=1,relwidth=1)
        buttonStopLoc = tk.Button(frame,text="Bitir",command=self.stopGetLoc)
        buttonStopLoc.place(relx=0.1,rely=0.45,relwidth=0.8)
        lb = tk.Label(text=f"Cismin yönü {self.sv.msg}")
        lb.place(relx=0.1,rely=0.10,relwidth=0.8)
        if(self.flag==0):
            self.main.after(200,self.getLoc)#loop
        else:
            self.start()  
            


    def stopGetLoc(self):
        self.flag =1
"""
    def stop_server(self): 
        self.sv.close()

    def stop_client(self):
        self.status.close()

    def on_closing(self):
        self.stop_server()  # Sunucu işlemini sonlandır
        self.stop_client()  # İstemci işlemini sonlandır
        self.main.destroy()  # Pencereyi kapat
        sys.exit()"""
        

if __name__ == "__main__":
    print("[STARTING]...")
    cntStation= landingContral()