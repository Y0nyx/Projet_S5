from SunFounder_Line_Follower import Line_Follower
from SunFounder_Ultrasonic_Avoidance import Ultrasonic_Avoidance
from picar import front_wheels
from picar import back_wheels
import picar
import time

picar.setup()

ua = Ultrasonic_Avoidance.Ultrasonic_Avoidance(20)
lf = Line_Follower.Line_Follower()
fw = front_wheels.Front_Wheels(db='config')
bw = back_wheels.Back_Wheels(db='config')
fw.turning_max = 45

forward_speed = 30
backward_speed = 70

back_distance = 10
turn_distance = 20

timeout = 10
last_angle = 90
last_dir = 0


def acceleration(final_speed, acceleration):
    needed_time = final_speed/acceleration
    bw.forward()
    for i in range(0, final_speed):
        bw.speed = i
        print(bw.speed)
        time.sleep(needed_time/final_speed)


def stop():
	bw.stop()
	fw.turn_straight()

if __name__ == '__main__':
    try:
        acceleration(70, 3)
    except KeyboardInterrupt:
        stop()