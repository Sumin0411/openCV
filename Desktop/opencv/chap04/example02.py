import numpy as np, cv2

def onMouse(event, x, y, flags, param):
    global title, image
    pt = (x,y)

    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(image, pt, 20, 100, 2)
        cv2.imshow(title, image)
    elif event == cv2.EVENT_LBUTTONDOWN:
        pt2 = (pt[0]+30, pt[1]+30)
        cv2.rectangle(image, pt, pt2, 100, 2)
        cv2.imshow(title, image)

image = np.ones((600,600), np.uint8) * 255
title = "example 02"
cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)