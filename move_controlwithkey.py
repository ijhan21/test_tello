from djitellopy import Tello, tello
import cv2

tello = Tello()

tello.connect()

# tello.takeoff()
# tello.move_up(200)
# tello.move_forward(100)
# tello.move_left(100)
# tello.move_back(100)
# tello.move_right(100)
# tello.flip_back()
# tello.land()

pannel = cv2.imread('images.jpeg')
cv2.imshow('TelloPannel', pannel)
while True:
    key = cv2.waitKey(1)
    if key == 27 or key ==ord('q'):break
    elif key == ord('t'):
        tello.takeoff()
    elif key == ord('l'):
        tello.land()
    elif key == ord('b'):
        tello.move('back', 50)
    elif key == ord('f'):
        tello.move('forward', 50)

cv2.destroyAllWindows()
pass