#cv2.circle(img ct r color thic, linetype, shift)
import numpy as np
import cv2

orange, blue, cyan = (0,165,255), (255,0,0),(255,255,0)
white, black = (255, 255, 255), (0,0,0)

image = np.full((300,500,3),white,np.uint8)

center = (image.shape[1]//2, image.shape[0]//2)
pt1,pt2 = (300,50), (100,220)
shade = (pt2[0] + 2, pt2[1]+2)

cv2.circle(image,center,100,blue)
cv2.circle(image,pt1,5,orange,2)
cv2.circle(image,pt2,70,cyan,-1)

cv2.imshow("Draw circle", image)
cv2.waitKey(0)

