import network
import time

# Replace with your WiFi credentials
WIFI_SSID= "Prajwal"    #wifi name: SSID: Service Set IDentifier
WIFI_PASSWORD= "prajwal129"

wifi= network.WLAN(network.STA_IF)     #station mode: existing WLAN;
#AP_IF: Accesspoint mode: creates own WLAN

if not wifi.isconnected():    #setup wifi with details
    print("Connecting to WiFi...")
    wifi.active(True)     #activate interface
    wifi.connect(WIFI_SSID, WIFI_PASSWORD)
    while not wifi.isconnected():
            pass
if wifi.isconnected():
    print("Connected to WiFi:", wifi.ifconfig())    #details of connection
else:
    print("Failed to connect to Wi-Fi!!!")
    wifi.active(False)   #deactivate the interface
