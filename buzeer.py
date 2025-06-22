#Program to beep the buzzer continuosly

import time, machine

buz=machine.Pin(21,machine.Pin.OUT)

while:
    buz.on()
    time.sleep(0.3)
    buz.off()
    time.sleep(0.3)