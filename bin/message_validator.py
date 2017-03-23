﻿#!/usr/bin/python

"""message_validator module

This module validates commands and arguments of an incoming message.

"""
import re
from classes.smsMessage import SMSMessage

menu = ("--Welcome to SIS--\n"
		"Reply with one of the numbers below.\n"
		"1 Weather\n"
		"2 Directions\n"
		"3 Places of Interest\n"
		"4 News\n"
		"5 Gas Prices")

menu_option1_detail = ("Follow the format below for a weather request:\n"
					   "Eg. 1 Oakville, Ontario")

menu_option2_detail = ("Follow the format below for a direction request:\n"
					   "Enter the start and end location separated by a slash.\n"
					   "Eg. 2 123 Regal Ct,Oakville/56 Muns,Mississuaga")

menu_option3_detail = ("Follow the format below for a places request:\n"
					   "Enter the category and location separated by a slash.\n"
					   "Eg. 3 Food/Brampton,Ontario\n"
					   "Eg. 3 Bank/Hamilton,Ontario")

menu_option4_detail = ("Follow the format below for a news request:\n"
					   "Enter the news outlet name.\n"
					   "Eg. 4 cnn-news\n"
					   "Eg. 4 ars-technica\n")

menu_option5_detail = ("Follow the format below for a gas prices request:\n"
					   "5 Mississauga")


def validate_command(message):
	print "validating..."
	
	# Drop messages from non-canadian addresses or short codes
	if (not message.address_field.startswith('+1') or len(message.address_field) < 12):
		message.message_status = 'drop'
		return message
	else:
		message.address_field = message.address_field[2:]

	# Validate command if present
	command = message.message_body.lower()
	if (command.startswith('1')):
		command = command.lstrip('1 ').replace('weather','').strip()
		print "Stripped"
		if (command):	# If message contains a query
			message.message_status = 'query'
			message.message_body = command
		else:
			message.message_status = 'menu'
			message.message_body = menu_option1_detail # If message does not contain a query
		return message
 	elif (command.startswith('2')):
		command = command.lstrip('2 ').replace('directions','').strip()
		if (command):	# If message contains a query
			message.message_status = 'query'
			message.message_body = command
		else:
			message.message_status = 'menu'
			message.message_body = menu_option2_detail # If message does not contain a query
		return message
	elif (command.startswith('3')):
		command = command.lstrip('3 ').replace('places','').strip()
		if (command):	# If message contains a query
			message.message_status = 'query'
			message.message_body = command
		else:
			message.message_status = 'menu'
			message.message_body = menu_option3_detail # If message does not contain a query
		return message
	elif (command.startswith('4')):
		command = command.lstrip('4 ').replace('news','').strip()
		if (command):	# If message contains a query
			message.message_status = 'query'
			message.message_body = command
		else:
			message.message_status = 'menu'
			message.message_body = menu_option4_detail # If message does not contain a query
		return message
	elif (command.startswith('5')):
		command = command.lstrip('5 ').replace('gas prices','').strip()
		if (command):	# If message contains a query
			message.message_status = 'query'
			message.message_body = command
		else:
			message.message_status = 'menu'
			message.message_body = menu_option5_detail # If message does not contain a query
		return message
	else: # If message contains anything else
		message.message_status = 'menu'
		message.message_body = menu # If message does not contain a query or option selected
		return message
