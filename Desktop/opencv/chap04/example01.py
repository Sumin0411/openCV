import cv2

capture  = cv2.VideoCapture(0)
if capture.isOpened() == False: raise Exception("카메라 연결 안됨")

fps = 30
delay = round(1000/fps)
size = (640, 480)
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

while True:
    ret, frame = capture.read()
    if not ret: break
    x, y, w, h = (200,100, 100, 200)
    cv2.rectangle(frame, (x,y,w,h), (0,0,255), 3)

    blue, green, red = cv2.split(frame)
    tmp = green[y:y+h, x:x+w]
    cv2.add(tmp, 50, tmp)
    frame = cv2.merge([blue, green, red])

    if cv2.waitKey(delay) >= 0:break
    cv2.imshow("ex16", frame)

capture.release()
