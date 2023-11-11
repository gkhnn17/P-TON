import numpy as np
import cv2


img = cv2.imread("CAS/cas3/shapes.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray,50,0.01,2 )#source,corners,minquality of corner,min_distance
corners = np.int0(corners)

for corner in corners:
    x,y =corner.ravel()#flatten [[x,y]] ->[x,y]
    cv2.circle(img,(x,y),5,(255,0,0),5)#source,center,radius,color,thichness

for i in range(len(corners)):
    for j in range(i+1,len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])
        color = tuple(map(lambda x : int(x),np.random.randint(0,255,size=3)))#making random color but randint making64bit what we making it 8bit
                                                                            #map making them array againg
        cv2.line(img,corner1,corner2,color,1)
        
cv2.imshow("Frame",img)
cv2.waitKey(0)
cv2.destroyAllWindows()