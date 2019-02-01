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
mode = False

tKey = 't111' #Set this string to the current code for the appropriate training
sKey = 't999'

GPIO.setmode(GPIO.BCM)
GPIO.setup(Pwr,GPIO.OUT)
GPIO.output(Pwr,Pwr_status)

def relay():
	print("relay")
	global Pwr_status
	Pwr_status = not Pwr_status
	GPIO.output(Pwr,Pwr_status)

try:
	while True:
		if mode:
			id,text = reader.read()
			if not sKey in text:
				text = text.strip()+","+tKey
				reader.write(text)
			relay()
			time.sleep(1)
			mode = False
		else:
			id,text = reader.read()
			if  tKey in text:
				if sKey in text:
					mode = True
				relay()
				time.sleep(2)
		print(id)
		print(text)
		print(mode)
		
except KeyboardInterrupt:
	GPIO.cleanup()
