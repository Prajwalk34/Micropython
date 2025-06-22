import network
import time

# Replace with your Wi-Fi credentials
ssid = 'Your_SSID'
password = 'Your_PASSWORD'

# Set up station interface
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# Connect to Wi-Fi
if not wlan.isconnected():
    print('Connecting to network...')
    wlan.connect(ssid, password)

    # Wait until connected
    timeout = 10  # seconds
    start = time.time()
    while not wlan.isconnected():
        if time.time() - start > timeout:
            print("Failed to connect to Wi-Fi")
            break
        time.sleep(1)

# Display connection info
if wlan.isconnected():
    print('Connected! Network config:', wlan.ifconfig())