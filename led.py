"""Program to turn on LED when swtich is pressed and turn off led when swtich is released"""

#led: 2, swtich: 0

import machine

led=machine.Pin(2, machine.Pin.OUT)
sw=machine.Pin(0, machine.Pin.IN)

while(1):
    stat=sw.value()
    if(stat==0):       #switch is pressed
        led.on()
    else:          #switch is released
        led.off()
            

