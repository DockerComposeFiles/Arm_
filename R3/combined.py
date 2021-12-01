#!/usr/bin/python
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# HTU
import time
import board
# BMP
import bme280
from adafruit_htu21d import HTU21D

# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C()  # uses board.SCL and board.SDA
sensor = HTU21D(i2c)
print("\nTemperature: %0.1f C" % sensor.temperature)
print("Humidity: %0.1f %%" % sensor.relative_humidity)

# Messdaten Holen BMP
temperatur, druck, x = bme280.readBME280All()
print("Temperatur : ", temperatur, "C")
print("Druck: ", druck, "hPa")
time.sleep(2)

