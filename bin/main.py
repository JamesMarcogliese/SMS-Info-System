#!/usr/bin/python

"""Main script to chain together functions of the SIS.

"""

import sys
import time
from classes.sim900 import SIM900
from classes.smsMessage import SMSMessage
import message_validator
import api_caller
import logging

def main():
	"""Main loop for the program."""
	logger.info('Arrived in main loop')
	while True: # Loop Main
		message_list = sim900.get_unread_messages()
		if (message_list):	
			for message in message_list: # Validate each message
				message = message_validator.validate_message(message)
				if (message.message_status == 'query_2' or message.message_status == 'query_3'): # If multi-parameter, split string
					message,p1,p2 = message_validator.extract_parameters(message)
				logger.debug('Message status: ' % message.message_status)
				if (message.message_status == 'query_1'):
					message.message_body = api_caller.weather_call(message.message_body)
				elif (message.message_status == 'query_2'):
					message.message_body = api_caller.directions_call(p1,p2)
				elif (message.message_status == 'query_3'):
					message.message_body = api_caller.places_call(p1,p2)
				elif (message.message_status == 'query_4'):
					message.message_body = api_caller.news_call(message.message_body)
				elif (message.message_status == 'query_5'):
					message.message_body = api_caller.gas_call(message.message_body)

				if (message.message_status == 'drop'): # If returning drop, drop object.
					del	message
				else:
					sim900.send_message(message)
	pass

if __name__ == '__main__':
	logging.basicConfig(level=logging.DEBUG)
	logger = logging.getLogger(__name__)
	logger.info('Started program')
	try:
		sim900 = SIM900()
		main()
	except KeyboardInterrupt:
		logger.exception('Killed by user')
		sys.exit(0)
	except:
		e = sys.exc_info()[0]
		logger.exception('Other exception occured: %s' % e)
		sys.exit(1)
