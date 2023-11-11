import numpy as np
import cv2
cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    witdh = int(cap.get(3))#3 is witdh
    height = int(cap.get(4))#4 is witdh
    """
    image = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv2.resize(frame,(0,0),fx=0.5,fy=0.5)
    image[:height//2, :witdh//2] = cv2.rotate(smaller_frame,cv2.ROTATE_180)
    image[height//2:, :witdh//2] = cv2.rotate(smaller_frame,cv2.ROTATE_180)
    image[:height//2, witdh//2:] = smaller_frame
    image[height//2:, witdh//2:] = smaller_frame
    """
    image = np.zeros(frame.shape, np.uint8)
    image = cv2.rotate(frame,cv2.ROTATE_180)
    cv2.imshow("frame",image)
    
    if cv2.waitKey(1) == ord("q"):
        break
 
cap.release()
cv2.destroyAllWindows()