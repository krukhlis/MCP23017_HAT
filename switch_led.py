#!/usr/bin/python

import wiringpi as wiringpi
from time import sleep

ic1_pin_base = 65
ic1_i2c_addr = 0x20

ic2_pin_base = 81
ic2_i2c_addr = 0x24

wiringpi.wiringPiSetup()
wiringpi.mcp23017Setup(ic1_pin_base,ic1_i2c_addr)
wiringpi.mcp23017Setup(ic2_pin_base,ic2_i2c_addr)

led = 65
switch = 81

wiringpi.pinMode(led,1)
wiringpi.digitalWrite(led,0)

wiringpi.pinMode(switch,0)
wiringpi.pullUpDnControl(switch,2)

while True:
	if not wiringpi.digitalRead(switch):
		wiringpi.digitalWrite(led,1)
	else:
		wiringpi.digitalWrite(led,0)
sleep(0.1)