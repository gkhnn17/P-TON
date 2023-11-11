import clientClass
import serverClass
import threading
import cv2


class findCircle():

    def __init__(self):
        self.client = clientClass.CL("127.0.0.1",9099,8080)
        self.status = serverClass.SV("127.0.0.1", 9990)


        dataThread = threading.Thread(target=self.client.send)
        dataThread.start()

        statusThread1 = threading.Thread(target=self.status.recieve)#ağdan veri almakla 
        statusThread2 = threading.Thread(target=self.status.broadcast)#ağdan ver vermek

        statusThread1.start()
        statusThread2.start()


    def getLoc(self,origin, target):
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

    def find(self):
        while True:
            if self.status.msg == "on":

                img = cv2.imread("circle.png")

                origin = (int(img.shape[0] / 2), int(img.shape[1] / 2))#orijin
                can = cv2.Canny(img, threshold1=120, threshold2=60)
                cnt, _ = cv2.findContours(can, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                x, y, w, h = cv2.boundingRect(cnt[0])

                center=(int((x + x + w) / 2),int((y + y + h) / 2))
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)#nesnenin yerini belirlemek
                img = cv2.circle(img, center, 3, (0, 0, 255), 3)
                loc=self.getLoc(origin,center)
                self.client.massage=loc
                img = cv2.putText(img, " {}".format(loc), center, cv2.FONT_HERSHEY_SIMPLEX,0.8, (0, 0, 255), 2, cv2.LINE_AA)
                cv2.imshow("Camera", img)
                cv2.waitKey(990)
            else:
                cv2.destroyAllWindows()



if __name__ == '__main__':
    find=findCircle()
    find.find()

#cd CAS/cas4/odev4/Referans
#python .\camera.py
#python .\controlStation.py
#python .\generate.py