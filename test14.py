import numpy as np
import cv2

blue, green, red = (255, 0, 0), (0, 255, 0), (0, 0, 255)
image = np.zeros((400, 600, 3), np.uint8)
image[:] = (255, 255, 255)

title = 'Line & rectangle'
cv2.imshow(title, image)
cv2.rectangle(image,(50,50),(250,150),blue,3,cv2.LINE_4)
cv2.line(image,(50,50),(250,150),red,1,cv2.LINE_4)

cv2.putText(image,'SIMPLEX',(250,150),cv2.FONT_HERSHEY_SIMPLEX,1,(42,42,165))
cv2.imshow(title,image)
cv2.waitKey(0)
cv2.destroyAllWindows()