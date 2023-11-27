import cv2
import random

img = cv2.imread("CAS/lena.jpg",1)
#line

img = cv2.line(img,(0,216),(512,216),(255,0,0),10)
#circle
img = cv2.circle(img,(310,315),(25),(0,0,255),-1)

#triangle
img = cv2.line(img,(310,220),(370,270),(255,255,255),10)#yeşil
img = cv2.line(img,(370,270),(310,300),(255,255,255),10)#mqvi
img = cv2.line(img,(310,300),(310,220),(255,255,255),10)#mor

cv2.imwrite("CAS/lenaProcess.jpg",img)
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(img.shape)