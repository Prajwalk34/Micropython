#write a program to run the servo motor rotate at the angle 10deg

from machine import Pin, PWM
import time

servo_pin = Pin(23, Pin.OUT)
pwm_pin = PWM(servo_pin)

pwm_pin.freq(50)
pwm_pin.duty(0)

def map(x, inmin, inmax, outmin, outmax):
    #map(0, 0, 180, 20, 120)
    return int((x-inmin)*(outmax-outmin)/(inmax-inmin)+outmin)
    #return int((0-0) * (120-20)/ (180-0) + 20)
                           
def servo(pwm_pin, angle):
    pwm_pin.duty(map(angle, 0, 180, 20, 120))
    #pwm pin duty(20)

servo(pwm_pin, 0) #position for 0 deg
time.sleep(3)

servo(pwm_pin, 90) #position for 90 deg
time.sleep(3)

servo(pwm_pin, 170) #position for 170 deg
time.sleep(3)

servo(pwm_pin, 0) #position for 0 deg
time.sleep(3)
    

