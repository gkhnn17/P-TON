import cv2


img_path = "CAS/cas2/lena2.png"
img =cv2.imread(img_path,1)
output = cv2.blur(img,(5,5))#img,(x,y)sliding
output = cv2.GaussianBlur(output,(7,7),100)#,img,(kernel size),disturbuting along

cv2.imshow("image",output)
cv2.imshow("original",img)
cv2.imwrite("CAS/cas2/img5.jpg",output)
cv2.waitKey(0)
cv2.destroyAllWindows()