import cv2 
import numpy as np

class Shapeandloc():
    def __init__(self,img):
        self.img= img

    def locations(self):
        img = cv2.imread(self.img)
        img = cv2.resize(img,(0,0),fx=0.5,fy=0.5)
        
        hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

        lower_green = np.array([50,50,10])
        upper_green = np.array([70,255,250])


        green_mask = cv2.inRange(hsv,lower_green,upper_green)
        cv2.imshow("img",img)
        contours, hierarchy = cv2.findContours(green_mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        center_x,center_y = int(img.shape[1]//2),img.shape[0]//2
        directions = []
        for contour in contours:
            x,y,h,w = cv2.boundingRect(contour)

            if x < center_x and y <center_y:
                directions.append("North-West")
            elif x < center_x and y > center_y:
                directions.append("South-West")
            elif x > center_x and y < center_y:
                directions.append("North-East")
            elif x > center_x and y > center_y:
                directions.append("South-East")

            cv2.drawContours(img, [contour], -1, (255, 0, 0), 5)
    
        for directs in directions:
            print(directs)

        self.shape(green_mask,img)
        
    
    def shape(self,img,show):
        
        _, thresh = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        print(len(contours))
        cv2.drawContours(img, contours, -1, (255, 0, 0), 5)

        
        h,w = img.shape[:2]

        centerx,centery = w//2 , h//2 
        topLeft = img[0:centery,0:centerx]
        topRight = img[0:centery,0:centerx]
        bottomLeft = img[0:centery,0:centerx]
        bottomLeft = img[0:centery,0:centerx]
        for i,contour in enumerate(contours):
            if i == 0:
                continue

            epsilon = 0.1*cv2.arcLength(contour,True)
            approx = cv2.approxPolyDP(contour,epsilon,True)

            x,y,h,w = cv2.boundingRect(approx)
            x_mid = int(x+w/3)
            y_mid = int(y+h/2)

            coords = x_mid,y_mid
            colour = (255,50,0)
            font = cv2.FONT_HERSHEY_DUPLEX


            if len(approx)==3:
                cv2.putText(show,"Triangel",coords,font,1,colour,1)
                print("1")
            elif len(approx) == 4:
                area = cv2.contourArea(contour)
                perimeter = cv2.arcLength(contour, True)#kontur kenarlarının uzunluğu
                circularity = 4 * 3.14159 * (area / (perimeter * perimeter))
                aspect_ratio = float (w)/h
                
                if circularity >= 0.85:
                    shape_label = "Circle"
                    cv2.putText(show, "Circle", coords, font, 1, colour, 1)
                    print("3")
                elif  0.95 <= aspect_ratio <=1.05:
                    shape_label = "Square"
                    cv2.putText(show,"Square",coords,font,1,colour,1)
                    print("4")
                else:
                    shape_label = "Rectangle"
                    cv2.putText(show,"Rectangel",coords,font,1,colour,1)
                    print("5")
            elif len(approx) ==5:
                shape_label = "Pentagon"
                cv2.putText(show,"Pentagon",coords,font,1,colour,1)#fontscale,thickness
        
            else:
                cv2.putText(show,"Circle",coords,font,1,colour,1)#fontscale,thickness

            cv2.imshow("img",show)
        


    """
    def shape(self,img):
        img = self.img
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        _ , thresh = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)
        contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        h,w = img.shape[:2]

        centerx,centery = w//2 , h//2 
        topLeft = img[0:centery,0:centerx]
        topRight = img[0:centery,0:centerx]
        bottomLeft = img[0:centery,0:centerx]
        bottomLeft = img[0:centery,0:centerx]
        print(len(contours))
        
        for i,contour in enumerate(contours):
            if i == 0 :#it is whole  image
                continue

            #approximate the shape for some images not perfect like square
            epsilon = 0.1*cv2.arcLength(contour,True)
            approx = cv2.approxPolyDP(contour,epsilon,True)

            x,y,h,w = cv2.boundingRect(approx)
            x_mid = int(x+w/3)
            y_mid = int(y+h/2)

            coords = x_mid,y_mid
            colour = (255,255,0)
            font =cv2.FONT_HERSHEY_DUPLEX

            if len(approx) ==3:
                cv2.putText(img,"Triangel",coords,font,1,colour,1)#fontscale,thickness
            
            elif len(approx) == 4:
                area = cv2.contourArea(contour)
                perimeter = cv2.arcLength(contour, True)#kontur kenarlarının uzunluğu
                circularity = 4 * 3.14159 * (area / (perimeter * perimeter))
                aspect_ratio = float (w)/h

                if circularity >= 0.85:
                    cv2.putText(img, "Circle", coords, font, 1, colour, 1)
                elif  0.95 <= aspect_ratio <=1.05:
                    cv2.putText(img,"Square",coords,font,1,colour,1)
                else:
                    cv2.putText(img,"Rectangel",coords,font,1,colour,1)
                    
            elif len(approx) ==5:
                cv2.putText(img,"Pentagon",coords,font,1,colour,1)#fontscale,thickness
            
            else:
                cv2.putText(img,"Circle",coords,font,1,colour,1)#fontscale,thickness
            
    
        cv2.imshow("window",img)
"""

show = Shapeandloc("CAS/cas3/shapes_locations.png")
show.locations()
cv2.waitKey(0)
cv2.destroyAllWindows()

