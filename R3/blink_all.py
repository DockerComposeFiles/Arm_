#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
# Temperatur
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

GPIO.setup(22, GPIO.OUT)

GPIO.setup(23, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

GPIO.setup(8, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)

# Feuchtigkeit
GPIO.setup(16, GPIO.OUT)

GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

fields = [17, 27, 22, 23, 25, 8, 7, 16, 20, 21]
for x in fields:
    GPIO.output(x, 1)
    time.sleep(0.2)
    GPIO.output(x, 0)


