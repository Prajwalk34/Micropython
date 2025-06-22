import machine
import time

ldr_sensor_pin = machine.Pin(15, machine.Pin.IN)

#main loop
while True:
    if ldr_sensor_pin.value() == 0:
        print("There is ligth")
    else:
        print("There is no light")
        
    time.sleep(2)
    