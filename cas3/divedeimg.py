import cv2
image = cv2.imread("cas3/shapes_locations.png")

h,w =image.shape[:2]#[:2]for without channel

centerx,centery = w//2 , h//2

topLeft = image[0:centery,0:centerx]#y,x
topRight = image[0:centery,centerx:w]

cv2.imshow("topLeft",topLeft)
cv2.imshow("topLeft",topLeft)
cv2.imshow("topLeft",topLeft)
cv2.imshow("topLeft",topLeft)

cv2.waitKey()