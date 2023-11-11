import sys
import typing
from PyQt5.uic import loadUi
from PyQt5 import QtCore,QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication,QWidget,QStackedWidget,QVBoxLayout
from PyQt5.QtGui import QImage,QPixmap


import cv2
import numpy as np


#İMPORT
from ekran1 import Ekran1
from ekran2 import Ekran2
from mission1 import Mission1Ui
from mission2 import Mission2Ui
from mission3 import Mission3Ui

# Define the WelcomeScreen class
class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen,self).__init__()
        self.ui =Ekran1()
        self.ui.setupUi(self)

        # Connect the signup button to the loginfunction
        self.ui.signup_button.clicked.connect(self.loginfunction)
        # Set the password field to display dots
        self.ui.password_field.setEchoMode(QtWidgets.QLineEdit.Password)
        # Create a QStackedWidget to manage UI transitions
        self.widget = QtWidgets.QStackedWidget()  # Create a QStackedWidget
        self.widget.addWidget(self.ui)  # Add the initial UI (Ekran1) to the widget

    #DATA
    def persons(self):
            persons = [
            {"ID": "23000040", "Şifre": "1122", "İsim": "Ahmet Yildirim"},
            {"ID": "22000025", "Şifre": "3344", "İsim": "Elif Öztürk"},
            {"ID": "23000027", "Şifre": "5566", "İsim": "Murat Doğan"},
            {"ID": "21000042", "Şifre": "7788", "İsim": "Yasemin Erdem"},
            {"ID": "1", "Şifre": "1", "İsim": "Gökhan"}
            ]
            return persons
    # Define the loginfunction
    def loginfunction(self):#PASSWORD
        user = self.ui.id_field.text()
        password = self.ui.password_field.text()

        if len(user) == 0 or len(password) == 0 :
            self.ui.error_label.setText("Please input all fields")
        
        else:
             for person in self.persons():
                if person["ID"] == user and person["Şifre"] == password:
                    print("Succesfully logged in.")
                    self.ui.error_label.setText("")

                    # Create and switch to MissionPage
                    
                    missionpage = MissionPage(person["İsim"])
                    widget.addWidget(missionpage)#ı cant use it with self.widget
                    widget.setCurrentIndex(widget.currentIndex() + 1)
                    
                    return

                else:
                    self.ui.error_label.setText("Invalid username or password")
                
# Define the MissionPage class
class MissionPage(QDialog):
    def __init__(self,name):
        super(MissionPage,self).__init__()
        self.ui2 = Ekran2()
        self.ui2.setupUi(self)
        self.name = name

        self.ui2.who_label.setText(f"Hoşgeldiniz {name}")
        
        # Connect buttons to mission functions
        self.ui2.mission_button.clicked.connect(self.mission1)
        self.ui2.mission2_button.clicked.connect(self.mission2)
        self.ui2.mission3_button.clicked.connect(self.mission3)

        # Create a QStackedWidget to manage UI transitions
        self.widget = QtWidgets.QStackedWidget()  # Create a QStackedWidget
        self.widget.addWidget(self.ui2)

    # MİSSİONS
    def mission1(self):
        print("mission ")
        mission1 = Mission1()
        widget.addWidget(mission1)
        widget.setCurrentWidget(mission1)

    
    def mission2(self):
        print("mission2")
        mission2 = Mission2()
        widget.addWidget(mission2)
        widget.setCurrentWidget(mission2)

    def mission3(self):
        print("mission3")
        mission3 = Mission3()
        widget.addWidget(mission3)
        widget.setCurrentWidget(mission3)


class Mission1(QDialog):
    def __init__(self):
        super(Mission1,self).__init__()
        self.ui = Mission1Ui()
        self.ui.setupUi(self)
        
        self.ui.answer_button.clicked.connect(self.complete)
        
        #LOCATİON İMAGE
        mission1png = "CAS/cas3/location.png"
        qpixmap = QPixmap(mission1png)
        
        
        # Get the dimensions of the image
        image_width = qpixmap.width()
        image_height = qpixmap.height()
        print(f"Image Width: {image_width}, Image Height: {image_height}")
        # Calculate the new page size (half of the image size)
        new_width = image_width // 2
        new_height = image_height // 2
        print(f"New Width: {new_width}, New Height: {new_height}")
        # Set the new size for the dialog
   
        widget.setFixedHeight(new_height)#!!!!!!!!!!self.widget olmadıı
        widget.setFixedWidth(new_width)
        scaled_pixmap = qpixmap.scaled(new_width, new_height, QtCore.Qt.KeepAspectRatio)
        self.ui.image_label.setPixmap(scaled_pixmap)

    def complete(self,mission1png ="CAS/cas3/location.png"):
                
        # Load and preprocess the image
        img = cv2.imread("CAS/cas3/location.png")
        img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

        # Convert image to HSV color space
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # Define the lower and upper bounds of blue in HSV
        lower_blue = np.array([50, 200, 100])  # Example lower bound
        upper_blue = np.array([130, 255, 255])  # Example upper bound

        # Threshold the image to create a binary mask of blue pixels
        blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)

        # Find contours in the binary mask
        contours, hierarchy = cv2.findContours(blue_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        center_x, center_y = int(img.shape[1]//2), img.shape[0] // 2
        # Extract and print coordinates of each rectangle
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
        
            if x < center_x and y < center_y:
                direction = "North-West"
            elif x < center_x and y > center_y:
                direction = "South-West"
            elif x > center_x and y < center_y:
                direction = "North-East"
            elif x > center_x and y > center_y:
                direction = "South-East"

            cv2.drawContours(img, [contour], -1, (255, 0, 0), 5)
        
        answer1png = "CAS/cas3/answer1.png"
        cv2.imwrite(answer1png ,img)
        self.ui.image_label.setPixmap(QPixmap(answer1png ))
        self.ui.answer_label.setText(f"Cevap : {direction} ")

class Mission2(QDialog):
    def __init__(self):
        super(Mission2,self).__init__()
        self.ui = Mission2Ui()
        self.ui.setupUi(self)

        self.ui.answer_button.clicked.connect(self.complete)

        #PNG LOC
        mission2png = "CAS/cas3/shapes.png"
        qpixmap = QPixmap(mission2png)
        image_height = qpixmap.height()
        image_width = qpixmap.width()
        print(f"İmage width {image_width} height: {image_height}")

        widget.setFixedSize(image_width,image_height)
        scaled_pixmap = qpixmap.scaled(image_width, image_height, QtCore.Qt.KeepAspectRatio)
        self.ui.image_label.setPixmap(scaled_pixmap)

    def complete(self, mission2png = "CAS/cas3/shapes.png" ):
        
        image = cv2.imread("CAS/cas3/shapes.png" )
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

        _ , thresh = cv2.threshold(gray , 200, 255 , cv2.THRESH_BINARY)
        contours,hierarchy =  cv2.findContours(thresh,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for i,contour in enumerate(contours):
            if i == 0:#it is whole image
                continue

            #approximate the shape for some images not perfect like square
            epsilon = 0.01*cv2.arcLength(contour,True)
            approx = cv2.approxPolyDP(contour,epsilon,True)

            x,y,h,w =cv2.boundingRect(approx)
            x_mid =int(x+w/20)
            _ ,y_mid = approx[0][0]//2

            coords = x_mid,y_mid
            colour = (0,0,0)
            font = cv2.FONT_HERSHEY_DUPLEX

            if len(approx) == 3:
                cv2.putText(image,"Triangel",coords,font,1,colour,2)

            elif len(approx) ==4:
                aspect_ratio = float (w)/h

                if 0.95 <= aspect_ratio <=1.05:
                    cv2.putText(image,"Square",coords,font,1,colour,2)
                else:
                    cv2.putText(image,"Rectangel",coords,font,1,colour,2)

            else:
                cv2.putText(image,"Circle",coords,font,1,colour,2)
        
        #answer2png
        answer2png = "CAS/cas3/answer2.png"
        cv2.imwrite(answer2png,image)
        self.ui.image_label.setPixmap(QPixmap(answer2png))


class Shape:
    def __init__(self,shape_type,location):
        self.shape_type = shape_type
        self.location = location

class Mission3(QDialog):
    def __init__(self):
        super(Mission3,self).__init__()
        self.ui= Mission3Ui()
        self.ui.setupUi(self)

        self.ui.answer_button.clicked.connect(self.complete)
        #mission3png
        mission3png = "CAS/cas3/shapes_locations.png"
        qpixmap = QPixmap(mission3png)
        image_height = qpixmap.height()//2
        image_width = qpixmap.width()//2
        print(f"Image width {image_width} height {image_height}")

        widget.setFixedSize(image_width,image_height)
        scaled_pixmap = qpixmap.scaled(image_width,image_height,QtCore.Qt.KeepAspectRatio)
        self.ui.image_label.setPixmap(scaled_pixmap)


        #list of shapes
        self.detected_shapes = []

    def complete(self):
      self.reimg()

    def reimg(self,mission3png = "CAS/cas3/shapes_locations.png"):
        # Load the image
        img = cv2.imread(mission3png)
        img = cv2.resize(img,(0,0),fx = 0.5,fy = 0.5)
        # Convert to greyscale
        img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        # Convert to binary image by thresholding
        _ , threshold = cv2.threshold(img_gray, 245,255,cv2.THRESH_BINARY_INV)
            # Find the contours
        self.contours , _ = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        print(len(self.contours))
        self.center_x,self.center_y = int(img.shape[1]//2),img.shape[0]//2
            # For each contour approximate the curve and
            # detect the shapes.
           
        self.locations(img)
            
    def locations(self,img):
        for i,contour in enumerate(self.contours):
            if i == 0 :
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
                shape = "Triangel"
                if x < self.center_x and y <self.center_y:
                    self.ui.northwest_label.setText(f"{shape},North-West")
                    shape = Shape("Triangel","North-West")
                elif x < self.center_x and y > self.center_y:
                    self.ui.southwest_label.setText(f"{shape},South-West")
                    shape = Shape("Triangel","South-West")
                elif x > self.center_x and y < self.center_y:
                    self.ui.northeast_label.setText(f"{shape},North-East")
                    shape = Shape("Triangel","North-East")
                elif x > self.center_x and y > self.center_y:
                   self.ui.southeast_label.setText(f"{shape},South-East")
                   shape = Shape("Triangel","South-East")
                self.detected_shapes.append(shape)

            elif len(approx) == 4:
                x, y, w, h = cv2.boundingRect(approx)
                aspect_ratio = float(w) / h
                                
                if 0.95 <= aspect_ratio <= 1.05:#SQUARE
                    shape = "Square"                                
                    if x < self.center_x and y <self.center_y:
                        self.ui.northwest_label.setText(f"{shape},North-West")
                        shape = Shape("Square","North-West")
                    elif x < self.center_x and y > self.center_y:
                         self.ui.southwest_label.setText(f"{shape},South-West")
                         shape = Shape("Square","South-West")
                    elif x > self.center_x and y < self.center_y:
                        self.ui.northeast_label.setText(f"{shape},North-East")
                        shape = Shape("Square","North-East")
                    elif x > self.center_x and y > self.center_y:
                        self.ui.southeast_label.setText(f"{shape},South-East")
                        shape = Shape("Square","South-East")
                    self.detected_shapes.append(shape)
                else:
                    shape = "Rectangle"
                    if x < self.center_x and y <self.center_y:
                        self.ui.northwest_label.setText(f"{shape},North-West")
                        shape = Shape("Rectangle","North-West")
                    elif x < self.center_x and y > self.center_y:
                         self.ui.southwest_label.setText(f"{shape},South-West")
                         shape = Shape("Rectangle","South-West")
                    elif x > self.center_x and y < self.center_y:
                        self.ui.northeast_label.setText(f"{shape},North-East")
                        shape = Shape("Rectangle","North-East")
                    elif x > self.center_x and y > self.center_y:
                         self.ui.southeast_label.setText(f"{shape},South-East")
                         shape = Shape("Rectangle","South-East")
                    self.detected_shapes.append(shape)
            else :#CİRCLE
                perimeter = cv2.arcLength(contour, True) #kontur kenarlarının uzunluğu
                circularity = 4 * 3.14159 * (area / (perimeter * perimeter))                
                if circularity >= 0.85:#circle
                    shape = "Circle"
                    if x < self.center_x and y <self.center_y:
                        self.ui.northwest_label.setText(f"{shape},North-West")
                        shape = Shape("Circle","North-West")
                    elif x < self.center_x and y > self.center_y:
                        self.ui.southwest_label.setText(f"{shape},South-West")
                        shape = Shape("Circle","South-West")
                    elif x > self.center_x and y < self.center_y:
                        self.ui.northeast_label.setText(f"{shape},North-East")
                        shape = Shape("Circle","North-East")
                    elif x > self.center_x and y > self.center_y:
                        self.ui.southeast_label.setText(f"{shape},South-East")
                        shape = Shape("Circle","South-East")
                    self.detected_shapes.append(shape)

        mission3answerpng = "CAS/cas3/answer3.png"
        cv2.imwrite(mission3answerpng,img)
        self.ui.image_label.setPixmap(QPixmap(mission3answerpng)) 
        self.comparison()

    def comparison(self):
        for shape in self.detected_shapes:
            if shape.location == "North-East":
                print(shape.shape_type)
                self.ui.northwest_east_label.setText(f"{shape.shape_type}- East")
                self.ui.southeast_north_label.setText(f"{shape.shape_type}- North")
                self.ui.southwest_northeast_label.setText(f"{shape.shape_type}-North East ")
            elif shape.location == "North-West":
                print(shape.shape_type)
                self.ui.northeast_west_label.setText(f"{shape.shape_type}- West")
                self.ui.southwest_north_label.setText(f"{shape.shape_type}- North")
                self.ui.southeast_northwest_label.setText(f"{shape.shape_type}-North West ")
            elif shape.location == "South-East":
                print(shape.shape_type)
                self.ui.southwest_east_label.setText(f"{shape.shape_type}- East")
                self.ui.northeast_south_label.setText(f"{shape.shape_type}- South")
                self.ui.northwest_southeast_label.setText(f"{shape.shape_type}-SouthEast ")
            elif shape.location == "South-West":
                print(shape.shape_type)
                self.ui.southeast_west_label.setText(f"{shape.shape_type}- West")
                self.ui.northwest_south_label.setText(f"{shape.shape_type}- South")
                self.ui.northeast_southwest_label.setText(f"{shape.shape_type}-SouthWest ")
            



app =QApplication(sys.argv)
welcome =WelcomeScreen()
widget = QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(620)
widget.setFixedWidth(440)
widget.show()

try:
    sys.exit(app.exec())
except:
    print("Exiting")
