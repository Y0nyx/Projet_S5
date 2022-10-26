from SunFounder_Line_Follower import Line_Follower
from SunFounder_Ultrasonic_Avoidance import Ultrasonic_Avoidance
from picar import front_wheels
from picar import back_wheels
import picar
import time

picar.setup()

_DEBUG = True
_DEBUG_INFO = 'DEBUG INFO : '

ua = Ultrasonic_Avoidance.Ultrasonic_Avoidance(20)
lf = Line_Follower.Line_Follower()
fw = front_wheels.Front_Wheels(db='config')
bw = back_wheels.Back_Wheels(db='config')
fw.turning_max = 45

min_backward_speed = 30
max_backward_speed = 50

def debug_(message):
    if _DEBUG:
        print(_DEBUG_INFO, message)
def acceleration(final_speed, acceleration):
    needed_time = (final_speed-min_backward_speed)/acceleration
    bw.backward()
    for i in range(0, final_speed):
        bw.speed = i
        print(i)
        time.sleep(needed_time/final_speed)

def line_follower():
    while True:
        analog_data = lf.read_analog()

        case = -1
        lower_value = 100
        moy_analog_data = sum(analog_data)/len(analog_data)

        for i in range(len(analog_data) - 1):
            if analog_data[i] < lower_value and analog_data[i] < moy_analog_data*0.55:
                lower_value = analog_data[i]
                case = i

        if case == 0:
            debug_("case 0")
            last_angle = 15
            fw.turn(last_angle)
        elif case == 1:
            debug_("case 1")
            last_angle = 65
            fw.turn(last_angle)
        elif case == 2:
            debug_("case 2")
            last_angle = 90
            fw.turn(last_angle)
        elif case == 3:
            debug_("case 3")
            last_angle = 115
            fw.turn(last_angle)
        elif case == 4:
            debug_("case 4")
            last_angle = 145
            fw.turn(last_angle)
        elif case == -1:
            debug_("LINE LOST")
            last_angle = 90
            fw.turn(last_angle)
            bw.foward()
            time(1)
            bw.backward()
            time(1)
        time.sleep(0.1)
def stop():
	bw.stop()
	fw.turn_straight()

if __name__ == '__main__':
    try:
        acceleration(max_backward_speed, 3)
        line_follower()
    except KeyboardInterrupt:
        stop()