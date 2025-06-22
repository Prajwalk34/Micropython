from machine import Pin
import network
import time
from umqtt.robust import MQTTClient
import sys

led=Pin(2,Pin.OUT)    #Onboard LED on Pin 2 of ESP32

WIFI_SSID= "Prajwal"
WIFI_PASSWORD= "prajwal129"

#Creates a unique client ID for MQTT
#and converts it into bytes format: client_12345
mqtt_client_id= bytes('client_'+'12345', 'utf-8')

ADAFRUIT_IO_URL  = 'io.adafruit.com' 
ADAFRUIT_USERNAME= 'anish6469'   #your account username
ADAFRUIT_IO_KEY  = 'aio_LNNK42OpTT3ndIgsbXL7iCZp18Oe'   #Key

#Defining the MQTT feed (topic) that will control the LED
TOGGLE_FEED_ID= 'new-feed-led'    #Key for feed name created

# Connect to WiFi
def connect_wifi():
    wifi= network.WLAN(network.STA_IF)
    if not wifi.isconnected():
        print("Connecting to WiFi...")
        wifi.active(True)
        wifi.connect(WIFI_SSID, WIFI_PASSWORD)
        while not wifi.isconnected():
                pass
    if wifi.isconnected():
        print("Connected to WiFi:", wifi.ifconfig())
    else:
        print("Failed to connect to Wi-Fi!!!")
        wifi.active(False)
        sys.exit()        

connect_wifi()  #Connecting to WiFi Router

#creating a client to communicate with the Adafruit server
client= MQTTClient(client_id=mqtt_client_id, 
                    server=ADAFRUIT_IO_URL, 
                    user=ADAFRUIT_USERNAME, 
                    password=ADAFRUIT_IO_KEY,
                    ssl=False)    #no encryption
try:            
    client.connect()
except Exception as e:
    print('Couldnot connect to MQTT server!:',e)
    sys.exit()

def cb(topic, msg):    # Callback function
    print('Received Data:Topic=',topic,'Msg=',msg)
    received_data = str(msg,'utf-8')     # Receiving Data
    if received_data=="0":
        led.value(0)   #LED off
    if received_data=="1":
        led.value(1)   #LED on

# format- Name/feeds/nameofthefeed
toggle_feed= bytes('{:s}/feeds/{:s}'.format(ADAFRUIT_USERNAME, TOGGLE_FEED_ID),'utf-8')   

client.set_callback(cb)      #Callback function               
client.subscribe(toggle_feed)   #Subscribing to a particular topic

while True:
    try:
        client.check_msg()   #non blocking function
    except :
        client.disconnect()
        sys.exit()
