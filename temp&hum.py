import dht
import machine
import time



# Define the DHT11 sensor pin
dht_pin= 14  # Replace with the GPIO pin to which your DHT11 is connected

# Create a DHT object

dht_sensor = dht.DHT11(machine.Pin(dht_pin))

while True:
    try:
        # Trigger a measurement
        dht_sensor.measure()

        # Read temperature and humidity
        temperature_celsius = dht_sensor.temperature()
        humidity_percent = dht_sensor.humidity()

        # Print the results
        print("Temperature: %3.1f °C" %temperature_celsius)
        print("Humidity   : %3.1f %%" %humidity_percent)
        
    except Exception as e:
        print("Error reading DHT11 sensor:", e)

    # Wait before the next measurement
    time.sleep(2)
