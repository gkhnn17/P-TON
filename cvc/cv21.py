import cv2
import random
"""
img = cv2.imread("CAS/lena.jpg",1)
img = cv2.resize(img,(0,0),fx=1,fy=1)
img = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite("CAS/new_img.jpg",img)

cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

img = cv2.imread("CAS/lena.jpg",1)
#[0,0,0] blue,green,red

tag = img[210:310,210:310]
img[100:200,100:200] = tag #copying tag
"""#coloring top of image pixels random 
for i in range(100):
    for j in range(img.shape[1]):
        #(rows,columns,channels)
        img[i][j] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
"""
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(img.shape)