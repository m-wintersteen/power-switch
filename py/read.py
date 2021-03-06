#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522

reader = SimpleMFRC522.SimpleMFRC522()

GPIO.setmode(GPIO.BCM)

try:
	id, text = reader.read()
	print(id)
	print(text)
finally:
	GPIO.cleanup()
