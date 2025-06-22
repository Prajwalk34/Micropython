from machine import Pin
from time import sleep

IR_PIN=15

ir_sense = Pin(IR_PIN , Pin.IN)

while True:
    val=ir_sense.value()
    if (val==0):
        print("Object detected!!")
    else:
        print("Object not detected..")
    sleep(2)
    
