
import cv2
import numpy as np

image = cv2.imread("/Users/gimsumin/Desktop/opencv/img.png") #파일 불러오기

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

def draw_box_and_text(result, color_name, color):
    contours, _ = cv2.findContours(result, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
        cv2.putText(image, color_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

#빨강
lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])
red_mask = cv2.inRange(hsv_image, lower_red, upper_red)
draw_box_and_text(red_mask, "Red", (0, 0, 255)) 

#파랑
lower_blue = np.array([110, 50, 50])
upper_blue = np.array([130, 255, 255])
blue_mask = cv2.inRange(hsv_image, lower_blue, upper_blue)
draw_box_and_text(blue_mask, "Blue", (255, 0, 0))

#초록
lower_green = np.array([40, 40, 40])
upper_green = np.array([80, 255, 255])
green_mask = cv2.inRange(hsv_image, lower_green, upper_green)
draw_box_and_text(green_mask, "Green", (0, 255, 0))


cv2.imshow("Result", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
