#!/usr/bin/env python

# Here are the connections between the Raspberry Pi Zero v1.1 and the RFID chip  and the PowerSwitch Tail
# 1 / +3V3 to 3.3V
# 22 / GPIO25 to RST
# 6 / GND to GND *AND* -in(pwrtail)
# 21 / SPI MISO / GPIO10 to MISO
# 19 / SPI MOSI / GPIO9 to MOSI
# 23 / SPI SCLK / GPIO11 to SCK
# 24 / SPI CSO / GPIO8 to SDA
# 3 / 12C1 SDA / GPIO2  to +in(pwrtail)

# Hello GitHub!

import RPi.GPIO as GPIO
import time
import SimpleMFRC522

reader = SimpleMFRC522.SimpleMFRC522() 

Pwr=2 
Pwr_status = 0

key = 't111' #Set this string to the current code for the appropriate training

GPIO.setmode(GPIO.BCM)
GPIO.setup(Pwr,GPIO.OUT)
GPIO.output(Pwr,Pwr_status)

def relay():
	global Pwr_status
	Pwr_status = not Pwr_status
	GPIO.output(Pwr,Pwr_status)

try:
	while True:
		id,text = reader.read()
		if  key in text:
			print(id)
			print(text)
			relay()
			time.sleep(2)
		
except KeyboardInterrupt:
	GPIO.cleanup()
