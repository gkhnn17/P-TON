import cv2
import numpy as np

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
#BLUR

# Find contours in the binary mask
contours, hierarchy = cv2.findContours(blue_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
center_x, center_y = int(img.shape[1]//2), img.shape[0] // 2
print(len(contours))
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
    cv2.putText(img, direction,(center_x,center_y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
   

# Visualize the result (draw blue contours on the original image)


cv2.imshow("Detected Rectangles", img)
cv2.waitKey(0)
cv2.destroyAllWindows()