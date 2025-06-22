import network
import time
import urequests

# Replace with your WiFi credentials
WIFI_SSID= "Prajwal"    #wifi name: SSID: Service Set IDentifier
WIFI_PASSWORD= "prajwal129"

def thing_write():
    #send data to the Cloud- Thingspeak
    #1. Replace with your ThingSpeak:Write API key:
    WRITE_API_KEY= "SSWRHK722V0P57PS"

    #2.Define url and data to upload:
    api_url= "http://api.thingspeak.com/update"
    data= {
        "api_key": WRITE_API_KEY,
        "field3": 75,
        }

    #3.Upload the data using post function:
    print("Uploading the data to the CLOUD..")
    response_cloud= urequests.post(api_url, json=data)
    print(response_cloud)
    print("ThingSpeak response:", response_cloud.text)

    #4.Close the connection
    response_cloud.close()
    print("Data is successfully uploaded")
    
def wifi_setup():
    wifi= network.WLAN(network.STA_IF)
    
    if not wifi.isconnected():    #setup wifi with details
        print("Connecting to WiFi...")
        wifi.active(True)     #activate interface
        wifi.connect(WIFI_SSID, WIFI_PASSWORD)
        
    if wifi.isconnected():
        print("Connected to WiFi:", wifi.ifconfig())    #details of connection        
        
        #upload data to cloud- Thingspeak
        thing_write()
        
    else:
        print("Failed to connect to Wi-Fi!!!")
        wifi.active(False)   #deactivate the interface

#setup wifi connection
print("Setting up the Wifi to ESP32..")
wifi_setup()
print('End')