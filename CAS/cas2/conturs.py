import cv2
img = cv2.imread("CAS/cas2/rectangles.png",1)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edged = cv2.Canny(gray,50,200)#img,min,max#resmin kenarlarını bulur

contours,hierarchy = cv2.findContours(edged,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)#img,hiyerarşi değer,yaklaşım modeli
print("number of counters: ",len(contours))

#finding biggest one
biggest_shape = max(contours,key=cv2.contourArea)
smallest_shape = min(contours,key=cv2.contourArea)

for contour in contours:
    if (contour is not biggest_shape) or (contour is not smallest_shape):
        cv2.drawContours(img,[contour],-1,(0,0,255),5)

cv2.drawContours(img,[biggest_shape],-1,(0,255,0),5)
cv2.drawContours(img,[smallest_shape],-1,(255,0,0),5)
cv2.imshow("Originalcounters",img)

cv2.imwrite("CAS/cas2/img6.png",img)
cv2.waitKey(0)
cv2.destroyAllWindows()