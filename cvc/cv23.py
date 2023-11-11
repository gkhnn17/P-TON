import numpy as np
import cv2


cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    witdh = int(cap.get(3))#3 is witdh
    height = int(cap.get(4))#4 is witdh

    img = cv2.line(frame,(0,0),(witdh,height),(255,0,0),(10))#(sourceimage,(starting position),(ending position),(color),(line thickness))
    img = cv2.line(img,(0,height),(witdh,0),(100,100,0),(10))#(sourceimage,(starting position),(ending position),(color),(line thickness))
    img = cv2.rectangle(img,(100,100),(200,200),(0,128,128),-1)#(sourceimage,(center position),(radius),(color),(line thickness*-1 to fill))
    img = cv2.circle(img,(325,240),(60),(255,0,255),5)
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img,"Gökhan",(10,height-10),font,1,(0,0,0),5)#(sourceimage,(position),(font),(fontscale),(color),(thickness))

    cv2.imshow("frame",frame)
    
    if cv2.waitKey(1) == ord("q"):
        break
 
cap.release()
cv2.destroyAllWindows()