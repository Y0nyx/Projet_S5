import line_follower
import Ultrasonic_Avoidance
from picar import front_wheels
from picar import back_wheels
import picar
import time

picar.setup()

ua = Ultrasonic_Avoidance.Ultrasonic_Avoidance(20)
lf = line_follower.Line_Follower()
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

def picar_setup():
    bw.speed = forward_speed

def opposite_angle():
	global last_angle
	if last_angle < 90:
		angle = last_angle + 2* fw.turning_max
	else:
		angle = last_angle - 2* fw.turning_max
	last_angle = angle
	return angle

def start_avoidance():
    while True:
        distance = ua.get_distance()
        print("distance: %scm" % distance)

        if distance > 0:
            count = 0
            if distance < back_distance:  # backward
                print("backward")
                fw.turn(opposite_angle())
                bw.backward()
                bw.speed = backward_speed
                time.sleep(1)
                fw.turn(opposite_angle())
                bw.forward()
                time.sleep(1)
            elif distance < turn_distance:  # turn
                print("turn")
                # fw.turn(rand_dir())
                bw.forward()
                bw.speed = forward_speed
                time.sleep(1)
            else:
                fw.turn_straight()
                bw.forward()
                bw.speed = forward_speed

        else:  # forward
            fw.turn_straight()
            if count > timeout:  # timeout, stop;
                bw.stop()
            else:
                bw.backward()
                bw.speed = forward_speed
                count += 1

def stop():
	bw.stop()
	fw.turn_straight()

if __name__ == '__main__':
    picar_setup()
	start_avoidance()
    bw.forward()
    print(lf.read_analog())
    print(lf.read_digital())
    print('')
    time.sleep(0.5)