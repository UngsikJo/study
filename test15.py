import random

import numpy as np
import cv2


def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        x2 = random.randrange(x + 10, x + 50)
        y2 = random.randrange(y -50, y - 10)
        cv2.rectangle(image, (x, y), (x2, y2), blue, 3, cv2.LINE_4)
        # 사각형이 그려진 이미지를 갱신해 주기 위해 새로 imshow
        cv2.imshow("Mouse Event", image)
    if event == cv2.EVENT_RBUTTONDOWN:
        x2 = random.randrange(x + 10, x + 50)
        y2 = random.randrange(y + 10, y + 50)
        cv2.circle(image,(x2, y2),10,blue)
        cv2.putText(image,f"{x2 , y2}",(0,400),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0))
        cv2.imshow("Mouse Event", image)




# opencv에서 기본 색은 BGR을 상요한다.
blue, green, red = (255, 0, 0), (0, 255, 0), (0, 0, 255)
image = np.zeros((400, 600, 3), np.uint8)
image[:] = (255, 255, 255)#색상을 휜색으로

cv2.namedWindow("Mouse Event")
cv2.imshow("Mouse Event", image)
cv2.setMouseCallback("Mouse Event", onMouse)
cv2.waitKey(0)#창이 떠 있다가 뭐든 키를 누르면 꺼짐.
cv2.destroyAllWindows()