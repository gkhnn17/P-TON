import cv2
import numpy as np
 
# Load the image
img = cv2.imread("CAS/cas3/shapes_locations.png")
img = cv2.resize(img,(0,0),fx=0.5,fy=0.5)
# Convert to greyscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Convert to binary image by thresholding
_, threshold = cv2.threshold(img_gray, 245, 255, cv2.THRESH_BINARY_INV)
# Find the contours
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))
# For each contour approximate the curve and
# detect the shapes.
for cnt in contours:

    epsilon = 0.01*cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)

    area = cv2.contourArea(cnt)
    if area < 200:  # Exclude small shapes
        continue
    cv2.drawContours(img, [approx], 0, (0), 3)
    # Position for writing text
    x,y = approx[0][0]
    if len(approx) == 3:
        cv2.putText(img, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, 0,2)
    elif len(approx) == 4:
        x, y, w, h = cv2.boundingRect(approx)
        aspect_ratio = float(w) / h
            
        if 0.95 <= aspect_ratio <= 1.05:
            cv2.putText(img, "Square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
        else:
            cv2.putText(img, "Rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
    else :
            """area = cv2.contourArea(cnt)
            perimeter = cv2.arcLength(cnt, True)#kontur kenarlarının uzunluğu
            circularity = 4 * 3.14159 * (area / (perimeter * perimeter))                
            if circularity >= 0.85:#circle"""
            cv2.putText(img, "Circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, 0,2)
                     
cv2.imshow("final", img)
cv2.waitKey(0)