import cv2
winname = "apple"
winname2 = "dog"
winname3 = "cat"

cv2.namedWindow(winname, cv2.WINDOW_AUTOSIZE)#cat이라는 창이름을 가진 빈 윈도우
cv2.namedWindow(winname2, cv2.WINDOW_AUTOSIZE)
cv2.namedWindow(winname3, cv2.WINDOW_AUTOSIZE)

img = cv2.imread("apple.jpeg")# 이미지 불러오기
img2 = cv2.imread("dog.jpeg")
img3 = cv2.imread("cat.jpeg")
cv2.imshow(winname,img)
cv2.imshow(winname2,img2)
cv2.imshow(winname3,img3)
cv2.resizeWindow(winname,300,150)
cv2.resizeWindow(winname2,300,150)
cv2.resizeWindow(winname3,300,150)

cv2.waitKey(0)
cv2.destroyWindow()
