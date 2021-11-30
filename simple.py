from djitellopy import Tello

CONTROL_UDP_PORT = 8889
STATE_UDP_PORT = 8890

tello = Tello()

tello.connect()
tello.takeoff()
tello.move_up(200)
# tello.move_forward(100)
# tello.move_left(100)
# tello.move_back(100)
# tello.move_right(100)
tello.flip_back()


tello.land()
pass