from djitellopy import Tello

tello = Tello()
tello.connect()
tello.streamon()
frame_read = tello.get_frame_read()

import cv2
cv2.imshow('tello stream', frame_read.frame)
cv2.waitKey()

tello.streamoff()
cv2.destroyAllWindows()
pass