import numpy as np
import cv2

switch_case = {
    ord('a'): "a키 입력",
    ord('b'): "b키 입력",
    0x41: "A키 입력",
    int('0x42', 16): "B키 입력",
    2424832:"왼쪽화살키 입력",
    2490368:"위쪽화살키 입력",
    2555904:"오른쪽화살키 입력",
    2621440: "아래쪽 화키 입력"
}

image = np.ones((200,300), np.float32)
cv2.namedWindow("Keyboard Event")
cv2.imshow("Keyboard Event", image)

while True:
    key = cv2.waitKeyEx(100)#이것만 기억하자
    if key == 27:
        break

    try:
        result= switch_case[key]
        print(result)
    except KeyError:
        reuslt = -1

cv2.destroyAllWindows()
