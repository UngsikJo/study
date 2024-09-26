
import numpy as np
import cv2

def onChange(value):
    global image, title
    print("추가 화소값:", value)
    image[:] = (255, 255, 255) #여기서 초기화 해줘야 함.
    cv2.rectangle(image, (0,0), (value, value), blue, 3, cv2.LINE_4)
    cv2.imshow(title,image)




blue, green, red = (255, 0, 0), (0, 255, 0), (0, 0, 255)
image = np.zeros((400, 600, 3), np.uint8)
image[:] = (255, 255, 255)


title = 'Trackbar Event'
cv2.imshow(title, image)

cv2.createTrackbar('rectangle size',title,0,255, onChange)
cv2.waitKey(0)
cv2.destroyAllWindows()
