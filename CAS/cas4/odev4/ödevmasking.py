import cv2
import numpy as np

class Mask():
    def __init__(self,image):
        #path
        self.img = cv2.imread(image)

    def masking_green(self):
        
        #HSV transformation
        
        self.hsv = cv2.cvtColor(self.img,cv2.COLOR_BGR2HSV)
        #mask
        lower_green = np.array([32,50,50])
        upper_green = np.array([80,255,255])
        #show
        self.green_mask = cv2.inRange(self.hsv,lower_green,upper_green)
        cv2.imshow("greenimg",self.green_mask)

    
    def masking_red(self):
        
        #HSV transformation
        
        self.hsv = cv2.cvtColor(self.img,cv2.COLOR_BGR2HSV)
        #red to yellow
        lower_red1 = np.array([0, 100, 20])
        upper_red1 = np.array([10, 255, 255])
        #red to purple
        lower_red2 = np.array([160, 100, 20])
        upper_red2 = np.array([179, 255, 255])

        
        #mask
        red_mask1 = cv2.inRange(self.hsv, lower_red1, upper_red1)
        red_mask2 = cv2.inRange(self.hsv, lower_red2, upper_red2)
        # Combine the red and purple masks
        self.combined_mask = cv2.bitwise_or(red_mask1, red_mask2)
        cv2.imshow("redimg",self.combined_mask)



green = Mask("CAS/cas4/odev4/16.jpg")
red = Mask("CAS/cas4/odev4/26.jpg")
red.masking_red()
green.masking_green()
cv2.waitKey(0)
cv2.destroyAllWindows()
