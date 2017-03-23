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
				elif (message.message_status == 'query'):
					print "Results getting returned..."
					if(message.message_body.startswith('1')):
						message.message_body =  message.message_body.replace('1','')
						print('removed query number from the query...')
						result = api_caller.weather_search(message.message_body)
						message.message_body = result
                                       		print (message.message_body)
						sim900.send_message(message)
                                        	print "Sent."

                                        elif(message.message_body.startswith('2')):
                                                message.message_body =  message.message_body.replace('2','')
                                                print('removed query number from the query...')
                                                p1, p2 = message.message_body.split("/")
                                                print (p1 + " " + p2)
                                                results = api_caller.directions_api(p1,p2)
                                                print (results)
                                                sim900.send_message(results)
                                                print "Sent."

				        elif(message.message_body.startswith('3')):
						message.message_body = message.message_body.replace('3','')
                                                print('removed query number from the query...')
						p1, p2 = message.message_body.split("/")
						print (p1 + " " + p2)
                                                results = api_caller.places_info(p1,p2)
                                                print (results)
                                                sim900.send_message(results)
                                                print "Sent."

				        elif (message.message_body.startswith('4')):
                                                message.message_body = message.message_body.replace('4','')
                                                print('removed query number from the query...')
                                                p1, p2 = message.message_body.split("/")
                                                print (p1 + " " + p2)
                                                results = api_caller.news_info(p1,p2)
                                                print (results)
                                                sim900.send_message(results)
                                                print "Sent."

				        elif (message.message_body.startswith('5')):
                                                message.message_body = message.message_body.replace('5','')
                                                print('removed query number from the query...')
                                                results = api_caller.places_info(message.message_body)
                                                print (results)
                                                sim900.send_message(results)
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
		sys.exit(1)
	except:
		print "Other exception occured!"
		e = sys.exc_info()[0]
		print e
		sys.exit(1)
