
import numpy as np
import cv2

def onMouse(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)

image = np.full((200,300), 255, np.int32)

title = "Mouse Event1"

cv2.imshow(title, image)

cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
cv2.destroywindows("Mouse Event1")