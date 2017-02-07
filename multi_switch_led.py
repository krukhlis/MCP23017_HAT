#!/usr/bin/python

import wiringpi as wiringpi
from time import sleep

# set the base number of ic1, this can be any number above (not including) 64
ic1_pin_base = 65
# pin number to code number:
# 1 = 65, 2 = 66, 3 = 67, 4 = 68, 5 = 69, 6 = 70, 7 = 71, 8 = 72, 9 = 73, 10 = 74, 11 = 75, 12 = 76, 13 = 77, 14 = 78, 15 = 79, 16 = 80
# define the i2c address of ic1, this is set by the jumpers on the HAT
ic1_i2c_addr = 0x20

# set the base number of ic2, this can be any number above (not including) 80. Pins 65 - 80 have been allocated to IC1 as defined above.
ic2_pin_base = 81
# pin number to code number:
# 1 = 81, 2 = 82, 3 = 83, 4 = 84, 5 = 85, 6 = 86, 7 = 87, 8 = 88, 9 = 89, 10 = 90, 11 = 91, 12 = 92, 13 = 93, 14 = 94, 15 = 95, 16 = 96
# define the i2c address of ic2, this is set by the jumpers on the HAT
ic2_i2c_addr = 0x24

# initiate the wiringpi library
wiringpi.wiringPiSetup()
# enable ic1 on the mcp23017 hat
wiringpi.mcp23017Setup(ic1_pin_base,ic1_i2c_addr)
# enable ic2 on the mcp23017 hat
wiringpi.mcp23017Setup(ic2_pin_base,ic2_i2c_addr)

# setup led pins
blue_led = 65
yellow_led = 66
red_led = 67
green_led = 68

# setup switch pins
blue_switch = 81
yellow_switch = 82
red_switch = 83
green_switch = 84

# set the pin mode to an output, 1, for all our leds
wiringpi.pinMode(blue_led,1)
wiringpi.pinMode(yellow_led,1)
wiringpi.pinMode(red_led,1)
wiringpi.pinMode(green_led,1)
# set all the leds off to start with, 0
wiringpi.digitalWrite(blue_led,0)
wiringpi.digitalWrite(yellow_led,0)
wiringpi.digitalWrite(red_led,0)
wiringpi.digitalWrite(green_led,0)

# set the pin mode to an input, 0, for all our switches
wiringpi.pinMode(blue_switch,0)
wiringpi.pinMode(yellow_switch,0)
wiringpi.pinMode(red_switch,0)
wiringpi.pinMode(green_switch,0)
# the mcp23017 ic has an internal pull up resistor. enabling this will keep the output pulled high. this stops any floating states which could cause odd things to happen in our script, 2
wiringpi.pullUpDnControl(blue_switch,2)
wiringpi.pullUpDnControl(yellow_switch,2)
wiringpi.pullUpDnControl(red_switch,2)
wiringpi.pullUpDnControl(green_switch,2)

# create an infinite loop
while True:
	# because we set the pull up resistor on our output, when we press the button the pin state will actually go low. so we need to check when the pin is low, hense the not in the if statement
	if not wiringpi.digitalRead(blue_switch):
		wiringpi.digitalWrite(blue_led,1)
	else:
		wiringpi.digitalWrite(blue_led,0)
	if not wiringpi.digitalRead(yellow_switch):
		wiringpi.digitalWrite(yellow_led,1)
	else:
		wiringpi.digitalWrite(yellow_led,0)
	if not wiringpi.digitalRead(red_switch):
		wiringpi.digitalWrite(red_led,1)
	else:
		wiringpi.digitalWrite(red_led,0)
	if not wiringpi.digitalRead(green_switch):
		wiringpi.digitalWrite(green_led,1)
	else:
		wiringpi.digitalWrite(green_led,0)
	# when we release the button the pin state changes back to high

# add a little pause for 1/10 of a second, to allow other process on the Pi to happen, we dont want to hog all the cpu :)
sleep(0.1)