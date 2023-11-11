import cv2
import numpy as np
import random
import time

img = np.zeros([900,900,3],dtype=np.uint8)
#arka planı beyaz yapmak
img.fill(255)

xCord=random.randint(150,750)
yCord=random.randint(150,750)

while True:
    xCord = random.randint(100, 800)
    yCord = random.randint(100, 800)
    img = cv2.circle(img, (xCord,yCord),50, (255,0,0), 100)
    cv2.imwrite("circle.png",img)
    time.sleep(1)
    img.fill(255)#ekran tekrar beyaz olur


