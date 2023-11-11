import landingClient
import landingServer
import threading
import cv2
import numpy as np
import time

class findLand():
    def __init__(self):
        self.client = landingClient.CL("127.0.0.1",9099,8080)
        self.status = landingServer.SV("127.0.0.1",9990)

        dataThread =threading.Thread(target=self.client.send)
        dataThread.start()

        statusThread1 = threading.Thread(target=self.status.receive)
        statusThread2 = threading.Thread(target=self.status.broadcast)
        wrtThread = threading.Thread(target=self.writer,args=(self.client.message,))
        wrtThread.start()
        statusThread1.start()
        statusThread2.start()

    def find(self): 
        video_path = "CAS\cas4\odev4\landing.avi"
        cap = cv2.VideoCapture(video_path)    
        while True:
            if self.status.msg =="on": 
                ret,frame = cap.read()
                frame = cv2.resize(frame,(0,0),fx=2,fy=2)
                width = frame.shape[1]
                height = frame.shape[0]

                origin = (width/2),(height/2)
                hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
                #define RED
                #red to yellow
                lower_red1 = np.array([0, 90, 20])
                upper_red1 = np.array([20, 255, 255])
                #red to purple
                lower_red2 = np.array([150, 90, 20])
                upper_red2 = np.array([179, 255, 255])

                redmask1 = cv2.inRange(hsv,lower_red1,upper_red1)
                redmask2 = cv2.inRange(hsv,lower_red2,upper_red2)

                combinedred = cv2.bitwise_or(redmask1,redmask2)
                contours ,_  = cv2.findContours(combinedred,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

                #part of without red
                if len(contours) > 0:
                    x,y,w,h = cv2.boundingRect(contours[0])

                    target = (int((x+x+w)/2),int((y+y+h)/2))

                    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
                    cv2.circle(frame, target, 3, (0, 0, 255), 3)
                    loc = self.getLoc(origin,target)
                    self.client.message=loc
                   
                    frame = cv2.putText(frame,"{}".format(loc),target,cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),2,cv2.LINE_AA)

                    cv2.waitKey(30)
                cv2.imshow("frame",frame)
            else:
                cv2.destroyAllWindows()



    def getLoc(self,origin,target):
        xDif = target[0] - origin[0]
        yDif = target[1] - origin[1]


        if abs(xDif) < 25:
            xDif = 0

        if abs(yDif) < 25:
            yDif = 0

   
        if xDif > 0 and yDif > 0:
            return "Guney Dogu"
        elif xDif > 0 and yDif < 0:
            return "Kuzey Dogu"
        elif xDif < 0 and yDif > 0:
            return "Guney Bati"
        elif xDif > 0 and yDif == 0:
            return "Dogu"
        elif xDif < 0 and yDif == 0:
            return "Bati"
        elif xDif == 0 and yDif > 0:
            return "Guney"
        elif xDif == 0 and yDif < 0:
            return "Kuzey"
        else:
            return "Kuzey Bati"

    
    def writer(self,loc):
        file = open("locs.txt","a")
        file.write(f"{loc}\n")
        time.sleep(5)

if __name__ == '__main__':
    find=findLand()
    find.find()


