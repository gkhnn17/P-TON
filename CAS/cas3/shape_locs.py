import cv2
import numpy as np

class Shapeandloc():
    def __init__(self,image):
        self.image = image
        
    def reimg(self):
        img = cv2.imread(self.image)
        img = cv2.resize(img,(0,0),fx=0.5,fy=0.5)

        img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    
        _ , thresh = cv2.threshold(img_gray, 245, 255, cv2.THRESH_BINARY_INV)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        print(len(contours))
        center_x,center_y = int(img.shape[1]//2),img.shape[0]//2

        
        
        self.locations(img,contours,center_x,center_y)
    def locations(self,img,contours,center_x,center_y):

        liste  = {"konum: ": "","şekil:": ""}


        for i,contour in enumerate(contours):
            if i == 0:
                continue
                
            epsilon = 0.01*cv2.arcLength(contour,True)
            approx = cv2.approxPolyDP(contour,epsilon,True)

            x_pos,ypos = approx[0][0]
            area = cv2.contourArea(contour)
            if area < 100:  # Exclude small shapes
                continue
            cv2.drawContours(img, [approx], 0, (0), 3)
                # Position for writing text
            x, y, w, h = cv2.boundingRect(approx)
            if len(approx) == 3:
                    cv2.putText(img, "Triangle", (x,y), cv2.FONT_HERSHEY_COMPLEX, 1, 0,2)                                  
                    if x < center_x and y <center_y:
                        print("Triangel,North-West")
                        dir["konum: ":"North-West","şekil:":"Triangel"]
                    elif x < center_x and y > center_y:
                        print("Triangel,South-West")
                        dir["konum: ":"South-West","şekil:":"Triangel"]
                    elif x > center_x and y < center_y:
                        print("Triangel,North-East")
                        dir["konum: ":"North-East","şekil:":"Triangel"]
                    elif x > center_x and y > center_y:
                        print("Triangel,South-East")
                        dir["konum: ":"South-East","şekil:":"Triangel"]
            elif len(approx) == 4:
                    x, y, w, h = cv2.boundingRect(approx)
                    aspect_ratio = float(w) / h
                        
                    if 0.95 <= aspect_ratio <= 1.05:#SQUARE
                        cv2.putText(img, "Square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, 0, 2)
                        if x < center_x and y <center_y:
                            print("Square,North-West")
                            dir["konum: ":"North-West","şekil:":"Square"]
                        elif x < center_x and y > center_y:
                            print("Square,South-West")
                            dir["konum: ":"South-West","şekil:":"Square"]
                        elif x > center_x and y < center_y:
                            print("Square,North-East")
                            dir["konum: ":"North-East","şekil:":"Square"]
                        elif x > center_x and y > center_y:
                            print("Square,South-East")
                            dir["konum: ":"South-East","şekil:":"Square"]
                    else:
                        cv2.putText(img, "Rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1,0, 2)
                        if x < center_x and y <center_y:
                            print("Rectangle,North-West")
                            dir["konum: ":"North-West","şekil:":"Rectangle"]
                        elif x < center_x and y > center_y:
                            print("Rectangle,South-West")
                            dir["konum: ":"South-West","şekil:":"Rectangle"]
                        elif x > center_x and y < center_y:
                            print("Rectangle,North-East")
                            dir["konum: ":"North-East","şekil:":"Rectangle"]
                        elif x > center_x and y > center_y:
                            print("Rectangle,South-East")
                            dir["konum: ":"South-East","şekil:":"Rectangle"]
            else :#CİRCLE
                        area = cv2.contourArea(contour)
                        perimeter = cv2.arcLength(contour, True)#kontur kenarlarının uzunluğu
                        circularity = 4 * 3.14159 * (area / (perimeter * perimeter))                
                        if circularity >= 0.85:#circle
                            cv2.putText(img, "Circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, 0,2)
                            if x < center_x and y <center_y:
                                print("Circle,North-West")
                                dir["konum: ":"North-West","şekil:":"Circle"]
                            elif x < center_x and y > center_y:
                                print("Circle,South-West")
                                dir["konum: ":"South-West","şekil:":"Circle"]
                            elif x > center_x and y < center_y:
                                print("Circle,North-East")
                                dir["konum: ":"North-East","şekil:":"Circle"]
                            elif x > center_x and y > center_y:
                                print("Circle,South-East")
                                dir["konum: ":"South-East", "şekil:":"Circle"]
        cv2.imshow("img",img)
        self.around(liste)
    def around(self,liste):
         for loc,shape in liste["konum"]["şekil"]:
            print(shape)
            
              
             

        
"""

    def locations(self,img):

        for i,contour in enumerate(self.contours):
            if i == 0:
                continue
                
            epsilon = 0.01*cv2.arcLength(contour,True)
            approx = cv2.approxPolyDP(contour,epsilon,True)

            x_pos,ypos = approx[0][0]
            area = cv2.contourArea(contour)
            if area < 100:  # Exclude small shapes
                continue
            cv2.drawContours(img, [approx], 0, (0), 3)
                # Position for writing text
            x, y, w, h = cv2.boundingRect(approx)
            if len(approx) == 3:
                    cv2.putText(img, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, 0,2)                                  
                    if x < self.center_x and y <self.center_y:
                        print("Triangel,North-West")
                    elif x < self.center_x and y > self.center_y:
                        print("Triangel,South-West")
                    elif x > self.center_x and y < self.center_y:
                        print("Triangel,North-East")
                    elif x > self.center_x and y > self.center_y:
                        print("Triangel,South-East")
            elif len(approx) == 4:
                    x, y, w, h = cv2.boundingRect(approx)
                    aspect_ratio = float(w) / h
                        
                    if 0.95 <= aspect_ratio <= 1.05:#SQUARE
                        cv2.putText(img, "Square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, 0, 2)
                        if x < self.center_x and y <self.center_y:
                            print("Square,North-West")
                        elif x < self.center_x and y > self.center_y:
                            print("Square,South-West")
                        elif x > self.center_x and y < self.center_y:
                            print("Square,North-East")
                        elif x > self.center_x and y > self.center_y:
                            print("Square,South-East")
                    else:
                        cv2.putText(img, "Rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1,0, 2)
                        if x < self.center_x and y <self.center_y:
                            print("Rectangle,North-West")
                        elif x < self.center_x and y > self.center_y:
                            print("Rectangle,South-West")
                        elif x > self.center_x and y < self.center_y:
                            print("Rectangle,North-East")
                        elif x > self.center_x and y > self.center_y:
                            print("Rectangle,South-East")
            else :#CİRCLE
                        area = cv2.contourArea(contour)
                        perimeter = cv2.arcLength(contour, True)#kontur kenarlarının uzunluğu
                        circularity = 4 * 3.14159 * (area / (perimeter * perimeter))                
                        if circularity >= 0.85:#circle
                            cv2.putText(img, "Circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, 0,2)
                            if x < self.center_x and y <self.center_y:
                                print("Circle,North-West")
                            elif x < self.center_x and y > self.center_y:
                                print("Circle,South-West")
                            elif x > self.center_x and y < self.center_y:
                                print("Circle,North-East")
                            elif x > self.center_x and y > self.center_y:
                                print("Circle,South-East")
            cv2.imshow("img",img)

"""
image = Shapeandloc("CAS/cas3/shapes_locations.png")
image.reimg()
cv2.waitKey(0)
cv2.destroyAllWindows()
        
"""import cv2
import numpy as np

class Shapeandloc():
    def __init__(self,img):
        self.img = img

    def reimg(self):
        img = cv2.imread(self.img)
        img = cv2.resize(img,(0,0),fx=0.5,fy=0.5)
        img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


        _ , self.thresh = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY)
        self.contours, hierarchy = cv2.findContours(img_gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


        self.center_x,self.center_y = int(img.shape[1]//2),img.shape[0]//2
        
        self.locations(img)


    def locations(self,img):

        for i,contour in enumerate(self.contours):
            if i == 0:
                continue
                
            epsilon = 0.01*cv2.arcLength(contour,True)
            approx = cv2.approxPolyDP(contour,epsilon,True)
            cv2.drawContours(img, [approx], 0, (0,0,255), 3)

            x,y,h,w = cv2.boundingRect(contour)
            x_pos,ypos = approx[0][0]
            area = cv2.contourArea(contour)
            if area < 100:  # Exclude small shapes
                continue
            if len(approx)==3:
                cv2.putText(img, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, 0,2)
                if x < self.center_x and y <self.center_y:
                    print("Triangel,North-West")
                elif x < self.center_x and y > self.center_y:
                    print("Triangel,South-West")
                elif x > self.center_x and y < self.center_y:
                    print("Triangel,North-East")
                elif x > self.center_x and y > self.center_y:
                    print("Triangel,South-East")

            elif len(approx) == 4:
                area = cv2.contourArea(contour)
                perimeter = cv2.arcLength(contour, True)#kontur kenarlarının uzunluğu
                circularity = 4 * 3.14159 * (area / (perimeter * perimeter))
                aspect_ratio = float (w)/h
                
                if circularity >= 0.85:#circle
                    if x < self.center_x and y <self.center_y:
                        print("circle,North-West")
                    elif x < self.center_x and y > self.center_y:
                        print("circle,South-West")
                    elif x > self.center_x and y < self.center_y:
                        print("circle,North-East")
                    elif x > self.center_x and y > self.center_y:
                        print("circle,South-East")
                    
                elif  0.95 <= aspect_ratio <=1.05:#square
                    if x < self.center_x and y <self.center_y:
                        print("Square,North-West")
                    elif x < self.center_x and y > self.center_y:
                        print("Square,South-West")
                    elif x > self.center_x and y < self.center_y:
                        print("Square,North-East")
                    elif x > self.center_x and y > self.center_y:
                        print("Square,South-East")
            
                else:#Rectangle
                    if x < self.center_x and y <self.center_y:
                        print("Rectangle,North-West")
                    elif x < self.center_x and y > self.center_y:
                        print("Rectangle,South-West")
                    elif x > self.center_x and y < self.center_y:
                        print("Rectangle,North-East")
                    elif x > self.center_x and y > self.center_y:
                        print("Rectangle,South-East")
                   
        cv2.imshow("img",img)

"""