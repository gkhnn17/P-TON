import cv2

image = cv2.imread("CAS/cas3/shapes.png")

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

_ , thresh = cv2.threshold(gray,200,255,cv2.THRESH_BINARY)
contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for i,contour in enumerate(contours):
    if i == 0 :#it is whole  image
        continue

    #approximate the shape for some images not perfect like square
    epsilon = 0.1*cv2.arcLength(contour,True)
    approx = cv2.approxPolyDP(contour,epsilon,True)

    cv2.drawContours(image,contour,0,(100,100,50),5)

    x,y,h,w = cv2.boundingRect(approx)
    x_mid = int(x+w/3)
    y_mid = int(y+h/2)

    coords = x_mid,y_mid
    colour = (255,255,0)
    font =cv2.FONT_HERSHEY_DUPLEX

    if len(approx) ==3:
        cv2.putText(image,"Triangel",coords,font,1,colour,1)#fontscale,thickness
    
    elif len(approx) == 4:
        area = cv2.contourArea(contour)
        perimeter = cv2.arcLength(contour, True)#kontur kenarlarının uzunluğu
        circularity = 4 * 3.14159 * (area / (perimeter * perimeter))
        if circularity >= 0.85:
            cv2.putText(image, "Circle", coords, font, 1, colour, 1)
        else:
            cv2.putText(image, "Quadrilateral", coords, font, 1, colour, 1)
            
    elif len(approx) ==5:
        cv2.putText(image,"Pentagon",coords,font,1,colour,1)#fontscale,thickness
    
    else:
        cv2.putText(image,"Circle",coords,font,1,colour,1)#fontscale,thickness
        
cv2.imshow("window",image)
cv2.waitKey(0)
cv2.destroyAllWindows()