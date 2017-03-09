#!/usr/bin/python

"""gsm_controller module.

This module controls the GSM module (SIM900) interfaces via 
physical serial and GPIO ports on the single-board computer. 

"""

import serial
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)

def power_toggle():
	"""Toggles the SIM900 GSM module ON or OFF.
	
	Powers ON or OFF the SIM900 GSM shield via GPIO pin
	on the RPi.
	
	Args: None.
	
	Returns: None.
	
	Raises: None.
	"""
	
	GPIO.setup(11, GPIO.OUT)
	GPIO.output(11, GPIO.HIGH)
	time.sleep(2);
	GPIO.output(11, GPIO.LOW)
	
	return
	
def send_sms(message, address):
	"""Sends an SMS message.
	
	Pushes an SMS message onto the cellular 
	network using physical serial interface on the RPi.
	
	Args: 
	message: String.
	address: String.
		
	Returns: None.
	
	Raises: None.
	"""
	if(ser.isOpen() == False):
		ser.open()
	
	ser.write('AT+CMGS="+%s"\r' % address)	# Destination address
	time.sleep(1)
	ser.write("%s\r" % message) # Message
	time.sleep(1)
	ser.write(chr(26))	# End of text requires (^Z). 
	ser.close()
	
	return

def check_message():
	"""Checks for new unread message.
	
	Queries the cellular network for new
	unread SMS messages and downloads them
	using the serial interface on the RPi.
	
	Args: None.
	
	Returns: 
	Message: String.
	Address: String.
	
	Raises: None.
	"""
	
	
	return message, address

def power_reset():
	"""Resets the SIM900 module.
	
	Resets the SIM900 GSM shield via RPi GPIO pin.
	
	Args: None.
	
	Returns: None.
	
	Raises: None.
	"""
	
	GPIO.setup(12, GPIO.OUT)
	GPIO.output(12, GPIO.HIGH)
	time.sleep(2);
	GPIO.output(12, GPIO.LOW)
	
	return
	
def clean_up():
	"""Resets the GPIO pin states
	
	Resets the RPi GPIO pin states by
	calling the cleanup function in the GPIO lib.
	
	Args: None.
	
	Returns: None.
	
	Raises: None.
	"""
	
	GPIO.cleanup()
	
	return
	
