#!/usr/bin/python

"""Main script to chain together functions of the SIS.

"""

import sys
import time
from classes.sim900 import SIM900
from classes.smsMessage import SMSMessage
import message_validator
import api_caller


def main():
	"""Main entry point for the script."""

	while True: # Loop Main
		print "In Main"
		message_list = sim900.get_unread_messages() # Get messages if available
		print "Getting messages..."
		if (message_list):	# If messages are available
			print "Messages returned!"
			for message in message_list: # Validate each message
				message = message_validator.validate_message(message)
				if (message.message_status == 'query_2' or message.message_status == 'query_3'):
					message,p1,p2 = message_validator.extract_parameters(message)
					print p1 + p2
				print "Message validated."
				print message.message_status
				if (message.message_status == 'query_1'):
					message.message_body = api_caller.weather_call(message.message_body)
				elif (message.message_status == 'query_2'):
					message.message_body = api_caller.directions_call(p1,p2)
				elif (message.message_status == 'query_3'):
					message.message_body = api_caller.places_call(p1,p2)
				elif (message.message_status == 'query_4'):
					message.message_body = api_caller.news_call(message.message_body)
				elif (message.message_status == 'query_5'):
					#message.message_body = api_caller.places_call(message.message_body)
					print "In 5"

				if (message.message_status == 'drop'): # If returning drop, drop object.
					print "Message dropped."
					del	message
				else:
					print "Results getting returned..."
					sim900.send_message(message)
					print "Sent."

		time.sleep(5)
	pass

if __name__ == '__main__':
	try:
		sim900 = SIM900()
		main()
	except KeyboardInterrupt:
		print "Killed by user"
		sys.exit(0)
	except:
		print "Other exception occured!"
		e = sys.exc_info()[0]
		print e
		sys.exit(1)
