#Implement Street ligth System:

import machine, time

led_pin=machine.Pin(2, machine.Pin.OUT)
ldr_pin=machine.Pin(15, machine.Pin.IN)

while(1):
    v=ldr_pin.value()
    if(v==0):
        print("It is Morning!, Street light is off!")
        led_pin.off()
    else:
        print("It's Dark!, Street light is on")
        led_pin.on()
    time.sleep(2)
    