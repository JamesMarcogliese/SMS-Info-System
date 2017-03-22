#!/usr/bin/python

"""Main script to chain together functions of the SIS.

"""

import sys
import time
from classes.sim900 import SIM900
from classes.smsMessage import SMSMessage
import message_validator

def main():
	"""Main entry point for the script."""

	while True: # Loop Main
		print "In Main"
		message_list = sim900.get_unread_messages() # Get messages if available
		print "Got messages"
		if (message_list):	# If messages are available
			print "Messages returned"
			for message in message_list: # Validate each message
				print "Iterating through messages..."
				print "body: " + message.message_body
				print "address: " + message.address_field
				message = message_validator.validate_command(message)
				print "Message validated"
				if (message.message_status == 'menu'): # If returning menu, send back to user.
					print "Menu getting returned..."
					sim900.send_message(message)
					print "Sent."
			# Format
			# API call
			# Format results
			# Send back to use
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
