#!/usr/bin/python

import serial
import time
import RPi.GPIO as GPIO
import re
from smsMessage import SMSMessage
import logging

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
		logging.getLogger(__name__)
		logging.info('Init SIM900')
		logging.info('Setup GPIO and serial...')
		# Set GPIO to BOARD reference
		GPIO.setmode(GPIO.BOARD)
		# Set power and reset key pin and as OUTPUT
		GPIO.setup(11, GPIO.OUT)

		# Create serial object and open on port '/dev/ttyAMA0' with baud 115200 and timeout=0
		self.ser = serial.Serial('/dev/ttyAMA0', 115200, timeout=0)
		logging.info('GPIO and serial set up')
		# Toggle power on board. If startup sequence is not returned, cycle again.
		self.power_toggle()
		time.sleep(10)
		if ("IIII" not in self.ser.read(size = self.ser.in_waiting)):
			self.power_toggle()

		logging.info('Module is ON')
		logging.info('Setting initial SIM900 config...')
		# Forbid incoming calls
		self.ser.write('AT+GSMBUSY=1\r')
		# Set command echo mode off
		time.sleep(1)
		self.ser.write('ATE0\r')
		# Set result code off
		time.sleep(1)
		self.ser.write('ATQ1\r')
		# Set SMS Message Format to Text
		time.sleep(1)
		self.ser.write('AT+CMGF=1\r')
		logging.info('Initial SIM900 config set')
		pass

	def __del__(self):
		"""SIM900 Destructor.

		Closes the serial connection, turns off SIM900 board, and cleans up GPIO.
		"""
		logging.info('Terminating SIM900 object...')
		self.ser.close()
		self.power_toggle()
		GPIO.cleanup()
		logging.info('SIM900 object terminated')
		pass

	def power_toggle(self):
		"""Toggles the SIM900 GSM module ON or OFF.

		Powers ON or OFF the SIM900 GSM shield via GPIO pin
		on the RPi.

		Args: None.

		Returns: None.

		Raises: None.
		"""
		logging.info('Cycling power...')
		GPIO.output(11, GPIO.HIGH)
		time.sleep(2)
		GPIO.output(11, GPIO.LOW)

		return

	def send_message(self, message):
		"""Sends an SMS message.

		Pushes an SMS message onto the cellular
		network using physical serial interface on the RPi.

		Args:
		message: SMSMessage Object.

		Returns: None.

		Raises: None.
		"""

		logging.info('Sending message...')
		while (message.message_body):
			message_part = message.message_body[:160]
			logging.debug('Message part: %s' % message_part)
			message.message_body = message.message_body[160:]
			logging.debug('Remaining part: %s' % message.message_body)
			self.ser.write('AT+CMGS=\"+%s\"\r' % message.address_field)	# Destination address
			time.sleep(1)
			self.ser.write("%s" % str(message_part)) # Message
			time.sleep(1)
			self.ser.write(chr(26))	# End of text requires (^Z)
			logging.info('Message sent')
			time.sleep(5)
		return

	def get_unread_messages(self):
		"""Retrieves unread messages.

		Queries the storage on the SIM card for
		unread SMS messages received via the cellular network
		using physical serial interface on the RPi.

		Args: None.

		Returns:
		List of SMSMessage objects.

		Raises: None.
		"""
		logging.info('Checking for unread messages...')
		self.ser.reset_input_buffer()

		self.ser.write('AT+CMGL="REC UNREAD"\r')	# Request all unread messages
		time.sleep(1)
		response = self.ser.read(size = self.ser.in_waiting) # Read all unread messages

		if (response):
			logging.info('New messages found')
			logging.debug('-%s-' % response)
			message_list = []
			match = re.finditer("\+CMGL: (\d+),""(.+)"",""(.+)"",\"\",""(.+)""\n(.+)\n", response)
			for each in match:
				storage_index = each.group(1)
				message_status = each.group(2)
				address_field = each.group(3).strip('"')
				arrival_timestamp = each.group(4)
				message_body = each.group(5)
				message = SMSMessage(storage_index, message_status, address_field, arrival_timestamp, message_body)
				message_list.append(message)
			self.delete_messages()
			return message_list
		logging.info('No messages found')
		return None


	def delete_messages(self):
		"""Deletes read and sent messages.

		Deletes all stored SMS messages from the SIM
		card whose status is "received read" as well as
		"sent" mobile originated numbers.

		Args: None.

		Returns: None.

		Raises: None.
		"""
		logging.info('Deleting read messages')
		self.ser.write('AT+CMGDA="DEL READ"\r')
		time.sleep(1)
		logging.info('Deleting sent messages')
		self.ser.write('AT+CMGDA="DEL SENT"\r')
		time.sleep(1)

		return
