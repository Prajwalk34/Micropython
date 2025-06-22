#write a alert the user if some one enters the home

from machine import Pin
import time

# Set up IR sensor input (e.g., GPIO 14)
ir_sensor = Pin(14, Pin.IN)

# Set up buzzer output (e.g., GPIO 12)
buzzer = Pin(12, Pin.OUT)

print("System ready. Monitoring for motion...")

while True:
    if ir_sensor.value() == 1:
        print("Motion detected! Triggering buzzer.")
        buzzer.value(1)  # Turn on buzzer
        time.sleep(0.5)  # Buzz for 0.5 seconds
        buzzer.value(0)  # Turn off buzzer
        time.sleep(2)    # Wait before checking again to avoid continuous alerts
    else:
        buzzer.value(0)  # Ensure buzzer is off
    time.sleep(0.1)
