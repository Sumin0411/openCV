import numpy as np
import cv2

image = np.zeros((200, 300), np.uint8)
image.fill(255)                                 # 모든 원소에 255(흰색) 지정

title1, title2 = 'AUTOSIZE', 'NORMAL'           # 윈도우 이름
cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE)
cv2.namedWindow(title2, cv2.WINDOW_NORMAL)

cv2.imshow(title1, image)
cv2.imshow(title2, image)
cv2.resizeWindow(title1, 400, 300)
cv2.resizeWindow(title2, 400, 300)
cv2.waitKey(0)
cv2.destroyAllWindows()                         # 열린 모든 윈도우 제거