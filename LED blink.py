#Program to blink led continously: GPIO2

#import the libraries
import machine, time
led=2

#direction of LED pin
led_pin=machine.Pin(led, machine.Pin.OUT)

while(1):
    #turn on LED
    led_pin.on()
    
    #delay: 1 sec
    time.sleep(1)
    
    #turn off LED
    led_pin.off()
    
    time.sleep(1)
    