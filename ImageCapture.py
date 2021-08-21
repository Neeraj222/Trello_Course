from djitellopy import tello
import cv2


me = tello.Tello()
me.connect()
me.streamon()
print(me.get_battery())

while True:
    img = me.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    cv2.imshow("Image", img)
    cv2.waitKey(1)