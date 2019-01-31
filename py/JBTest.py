#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import SimpleMFRC522

reader = SimpleMFRC522.SimpleMFRC522()

Pwr=2
Pwr_status = 0

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
		print(id)
		print(text)
		relay()
		time.sleep(2)
except KeyboardInterrupt:
	GPIO.cleanup()
