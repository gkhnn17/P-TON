import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread("CAS/cas3/location.png")
#IMREAD_COLOR -> 1(COLOR),0(GREY),-1(UNCHANGED)
img = cv2.resize(img,(0,0),fx=0.5,fy=0.5)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret1,thresholded = cv2.threshold(gray,250,255,cv2.THRESH_BINARY)


edged = cv2.Canny(thresholded,50,200)
contours,hierarchy = cv2.findContours(edged,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)#Syntax: cv2.findContours(src, contour_retrieval, contours_approximation)
"""
src: input image n-dimensional (but for in our example we are going to use 2 dimensional image which is 
mostly preferred.)
contour_retrieval:
cv.RETR_EXTERNAL:retrieves only the extreme outer contours
cv.RETR_LIST:retrieves all of the contours without establishing any hierarchical relationships.
cv.RETR_TREE:retrieves all of the contours and reconstructs a full hierarchy of nested contours.
contours_approximation:
cv.CHAIN_APPROX_NONE: It will store all the boundary points.
cv.CHAIN_APPROX_SIMPLE: It will store number of end points(eg.In case of rectangle it will store 4)
Return value: list of contour points
"""
print("number of counters" ,len(contours))


i = 0
# list for storing names of shapes
for contour in contours:
    
    # here we are ignoring first counter because 
    # findcontour function detects whole image as shape
    if i == 0:
        i = 1
        continue

      # cv2.approxPloyDP() function to approximate the shape
    approx = cv2.approxPolyDP(
        contour, 0.01 * cv2.arcLength(contour, True), True)
    
    cv2.drawContours(img,[contour],-1,(0,0,255),5)#-1 all of them

  # finding center point of shape
    M = cv2.moments(contour)#momentum
    if M['m00'] != 0.0:#m00 ağırlığı temsil eder 
        x = int(M['m10']/M['m00'])#x koordinatlarının momenti/alan = x koordianatlarının ağırlığı
        y = int(M['m01']/M['m00'])

    if len(approx) == 4:
        cv2.putText(img, 'Quadrilateral', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
  
"""
Syntax: cv.DrawContours(src, contour, contourIndex, colour, thickness)

Parameters:

src: n dimensional image
contour: contour points it can be list.
contourIndex:
-1:draw all the contours
To draw individual contour we can pass here index value
color:color values
thickness: size of outline
"""

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()