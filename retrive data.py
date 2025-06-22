import network
import time
import urequests

# Replace with your WiFi credentials
WIFI_SSID= "Prajwal"    #wifi name: SSID: Service Set IDentifier
WIFI_PASSWORD= "prajwal129"

def wifi_setup():
    wifi= network.WLAN(network.STA_IF)
    
    if not wifi.isconnected():
        print("Connecting to WiFi...")
        wifi.active(True)
        wifi.connect(WIFI_SSID, WIFI_PASSWORD)
        
    if wifi.isconnected():
        print("Connected to WiFi:", wifi.ifconfig())       
        
        #Read data from cloud- Thingspeak
        thing_read()
        
    else:
        print("Failed to connect to Wi-Fi!!!")
        wifi.active(False)   #deactivate the interface

def thing_read():
    url='https://api.thingspeak.com/channels/ID/fields/NUMBER/last.json?api_key=AN3DY3R54TVBAV7B'
    
    print("Reading data from the Cloud..")
    response= urequests.get(url)
    data= response.json()
    
    print('Data is:\n', data)
    
    f1= data.get('field1')
    f2= data.get('field2')
    f3= data.get('field3')
    
    print("Field1 data=", f1)
    print("Field2 data=", f2)
    print("Field3 data=", f3)
    
    response.close()

#setup wifi connection
print("Setting up the Wifi to ESP32..")
wifi_setup()
print('End')
