import network
import time
import machine
import urequests

while True:
    if ldr_sensor_pin.value() == 0:
        print("There is ligth")
    else:
        print("There is no light")
        
    time.sleep(2)
    
# Replace with your WiFi credentials
WIFI_SSID= "Prajwal"    #wifi name: SSID: Service Set IDentifier
WIFI_PASSWORD= "prajwal129"