#!/usr/bin/python
from sense_hat import SenseHat
import time
import sys
from ISStreamer.Streamer import Streamer  

sense = SenseHat()
logger = Streamer(bucket_name="Sense Hat Sensor Data", access_key="YOUR_KEY_HERE")  
sense.clear()

try:
      while True:
           temp = sense.get_temperature()
           temp = round(temp, 1)
           logger.log("Temperature C",temp) 

            humidity = sense.get_humidity()  
            humidity = round(humidity, 1)  
            logger.log("Humidity :",humidity)  

            pressure = sense.get_pressure()
            pressure = round(pressure, 1)
            logger.log("Pressure:",pressure)

           time.sleep(1)
except KeyboardInterrupt:
      pass

