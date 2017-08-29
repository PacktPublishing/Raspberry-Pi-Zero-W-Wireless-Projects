#!/usr/bin/python
import sys
import Adafruit_DHT
import time

while True:
	humidity, temperature = Adafruit_DHT.read_retry(11, 4)
	print "Humidity: " + str(humidity)
	print "Temperature: " + str(temperature) + "\n"
	time.sleep(1)

