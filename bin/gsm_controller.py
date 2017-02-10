#!/usr/bin/python

"""gsm_controller module.

This module controls the GSM module (SIM900) interfaces via 
physical serial and GPIO ports on the single-board computer. 

"""

import serial
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

def power_on():
	"""Turns the SIM900 GSM module ON.
	
	Powers ON the SIM900 GSM shield via GPIO pins.
	
	Args: None.
	
	Returns: None.
	
	Raises: None.
	"""
	
	return
	
def send_sms(message):
	"""Sends an SMS message.
	
	Pushes an SMS message onto the cellular 
	network using physical serial interface.
	
	Args: 
		message: String.
	
	Returns: None.
	
	Raises: None.
	"""
	
   return

def check_message():
	"""Checks for new unread message.
	
	Queries the cellular network for new
	unread SMS messages and downloads them
	using the serial interface.
	
	Args: None.
	
	Returns: 
		Message: String.
	
	Raises: None.
	"""
	
   return message