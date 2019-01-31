#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522

reader = SimpleMFRC522.SimpleMFRC522()

GPIO.setmode(GPIO.BCM)

try:
	text = raw_input('Input training (tXXX,tXXX,tXXX): ')
	print("Now place your tag to write")
	reader.write(text)
	print("Written")
finally:
	GPIO.cleanup()
