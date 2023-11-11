import cv2
import numpy as np

file_path = "CAS/cas4/odev4/16.jpg"
image = cv2.imread(file_path,-1)

#conver image to frayscale
image_gray =cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#conver image to black and white
thresh , image_edges = cv2.threshold(image_gray,240,255,cv2.THRESH_BINARY)

#define canvas
canvas = np.zeros(image.shape,np.uint8)
canvas.fill(255)
#create bacground mask
mask = np.zeros(image.shape,np.uint8)
mask.fill(255)


#get all contours
contours_draw,heirarchy =cv2.findContours(image_edges,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)

#get most significant contours
contours_mask,heirarchy =cv2.findContours(image_edges,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

#draw allcontours
#cv2.drawContours(canvas,contours_draw,-1,(0,255,0),3)               


#contours traversal
for contour in range(len(contours_draw)):
    #draw current contour
    cv2.drawContours(canvas,contours_draw,contour,(0,0,0),2)

    #debug
    cv2.waitKey(0)
    cv2.imshow("origin",canvas)

#draw contours the image in 
#open source
cv2.imshow("original", canvas)
#escape condition
cv2.waitKey(0)

#cleanup windows
cv2.destroyAllWindows()