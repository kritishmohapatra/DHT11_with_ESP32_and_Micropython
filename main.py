# Import necessary libraries
import time  # To add delays between sensor readings
import dht   # To interact with DHT11 sensor
from machine import Pin  # To set up GPIO pins on ESP32

# Initialize the DHT11 sensor connected to GPIO pin 4
sensor = dht.DHT11(Pin(4))

# Infinite loop to keep taking readings from the sensor
while True:
    try:
        # Measure temperature and humidity from the sensor
        sensor.measure()
        
        # Get temperature (in Celsius) and humidity (in percentage)
        temp = sensor.temperature()
        hum = sensor.humidity()

        # Print the temperature and humidity to the Serial Monitor
        print('Temperature:', temp, '°C')
        print('Humidity:', hum, '%')
        print('------------------------')

    except OSError as e:
        # If there is an error reading from the sensor, print an error message
        print('Failed to read sensor.')

    # Wait for 2 seconds before taking the next reading
    time.sleep(2)
