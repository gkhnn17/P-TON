import cv2
image = cv2.imread("CAS/cas2/threshold.jpg",0)

image = cv2.resize(image,(0,0),fx=2,fy=2)
#simple
ret1,thresh1 = cv2.threshold(image,0,255,cv2.THRESH_BINARY)#

#ret2,thresh2 = cv2.threshold(image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow("original",image)
cv2.imshow("thresh1",thresh1)
#cv2.imshow("thresh2",thresh2)
cv2.imwrite("CAS/cas2/img3.jpg",thresh1)
cv2.waitKey(0)
cv2.destroyAllWindows()