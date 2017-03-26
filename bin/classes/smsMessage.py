#!/usr/bin/python

class SMSMessage:

	"""SMS Message class.

	This class contains data types to hold SMS message details.
	"""
	
	storage_index = None
	message_status = None
	address_field = None
	arrival_timestamp = None
	message_body = None
	
	def __init__(self, 	storage_index, message_status, address_field, arrival_timestamp, message_body):
	
		"""SMSMessage Constructor.

		Populates attributes of object.
		"""
		self.storage_index = storage_index
		self.message_status = message_status
		self.address_field = address_field
		self.arrival_timestamp = arrival_timestamp
		self.message_body = message_body