from djitellopy import Tello
from time import sleep

# Note: The drone will already start facing East

tello = Tello()

tello.takeoff()

tello.connect()
sleep(1)

tello.move_up(77)
sleep(1)

tello.move_forward(153)
sleep(1)

tello.rotate_counter_clockwise(90)
sleep(1)

tello.move_forward(153)
sleep(1)

tello.rotate_clockwise(90)
sleep(1)

tello.move_down(106)
sleep(1)

tello.move_forward(91)
sleep(1)

tello.rotate_clockwise(90)
sleep(1)

tello.move_up(45)
sleep(1)

tello.move_forward(91)
sleep(1)

tello.rotate_counter_clockwise(90)

tello.move_forward(183)

tello.land()
