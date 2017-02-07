#!/usr/bin/python

import wiringpi as wiringpi
from time import sleep

ic1_pin_base = 65
ic1_i2c_addr = 0x20

wiringpi.wiringPiSetup()
wiringpi.mcp23017Setup(ic1_pin_base,ic1_i2c_addr)

led = 65

wiringpi.pinMode(led,1)
wiringpi.digitalWrite(led,0)

while True:
	wiringpi.digitalWrite(led,1)
	sleep(0.5)
	wiringpi.digitalWrite(led,0)
	sleep(0.5)