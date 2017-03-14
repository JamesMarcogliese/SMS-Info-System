#!/usr/bin/python

import serial
import time
import RPi.GPIO as GPIO
import re
import smsMessage

class SIM900:

	"""SIM900 GSM Module class.

	This class controls the GSM module (SIM900) interfaces via 
	physical serial and GPIO ports on the single-board computer. 
	"""
	
	ser = None
	
	def __init__(self):
	
		"""SIM900 Constructor.
		
		Sets up GPIO, serial connection, turns on board and performs
		initial SIM900 config.
		"""
		# Set GPIO to BOARD reference
		GPIO.setmode(GPIO.BOARD)
		# Set power and reset key pin and as OUTPUT
		GPIO.setup(11, GPIO.OUT)
		
		# Create serial object and open on port '/dev/ttyAMA0' with baud 115200 and timeout=0
		self.ser = serial.Serial('/dev/ttyAMA0', 115200, timeout=0) 
		
		# Toggle power on board. If startup sequence is not returned, cycle again.
		self.power_toggle()
		time.sleep(10)
		if ("IIII" not in self.ser.read(size = self.ser.in_waiting)):
			self.power_toggle()
			
		# Forbid incoming calls
		self.ser.write('AT+GSMBUSY=1\r')
		# Set command echo mode off
		self.ser.write('ATE0\r')
		# Set result code off
		self.ser.write('ATQ1\r')
		
		return
		
	def __del__(self):
		"""SIM900 Destructor.
		
		Closes the serial connection, turns off SIM900 board, and cleans up GPIO. 
		"""
		self.power_toggle()
		self.ser.close()
		GPIO.cleanup()
		
		return

	def power_toggle(self):
		"""Toggles the SIM900 GSM module ON or OFF.
		
		Powers ON or OFF the SIM900 GSM shield via GPIO pin
		on the RPi. 
		
		Args: None.
		
		Returns: None.
		
		Raises: None.
		"""

		GPIO.output(11, GPIO.HIGH)
		time.sleep(2)
		GPIO.output(11, GPIO.LOW)
		
		return
		
	def send_message(message, address):
		"""Sends an SMS message.
		
		Pushes an SMS message onto the cellular 
		network using physical serial interface on the RPi.
		
		Args: 
		message: String.
		address: String.

		Returns: None.
		
		Raises: None.
		"""
		
		self.ser.reset_input_buffer()
		
		self.ser.write('AT+CMGS="+%s"\r' % address)	# Destination address
		self.ser.write('%s\r' % message) # Message
		self.ser.write(chr(26))	# End of text requires (^Z). 
		
		return

	def get_unread_messages():
		"""Retrieves unread messages.
		
		Queries the storage on the SIM card for 
		unread SMS messages received via the cellular network
		using physical serial interface on the RPi. 
		
		Args: None.
		
		Returns: 
		List of smsMessage objects
		
		Raises: None.
		"""
		
		self.ser.reset_input_buffer()	
		
		self.ser.write('AT+CMGL="REC UNREAD"\r')	# Request all unread messages
		response = self.ser.read(size = self.ser.in_waiting) # Read all unread messages
		
		if (response):	
			message_list = []
			match = re.finditer("\+CMGL: (\d+),""(.+)"",""(.+)"",\"\",""(.+)""\n(.+)\n", response)
			for each in match:
				storage_index = each.group(1)
				message_status = each.group(2)
				address_field = each.group(3).strip('"').replace('+1','')
				arrival_timestamp = each.group(4)
				message_body = each.group(5)
				message = smsMessage(storage_index, message_status, address_field, arrival_timestamp, message_body)
				message_list.append(message)
			self.delete_messages()
			return message_list
		return
		

	def delete_messages(self):
		"""Deletes read and sent messages.
		
		Deletes all stored SMS messages from the SIM
		card whose status is "received read" as well as 
		"sent" mobile originated numbers.
		
		Args: None.
		
		Returns: None.
		
		Raises: None.
		"""
		
		self.ser.write('AT+CMGDA="DEL READ"\r')
		self.ser.write('AT+CMGDA="DEL SENT"\r')
		
		return