#!/usr/bin/python

"""message_validator module

This module validates commands and arguments of an incoming message.

"""
import re
from collections import defaultdict
from classes.smsMessage import SMSMessage
import api_caller

main_menu = ("--Welcome to SIS--\n"
		"Reply with one of the numbers below.\n"
		"1 for Weather\n"
		"2 for Directions\n"
		"3 for Places of Interest\n"
		"4 for News\n"
		"5 for Gas Prices")

menu_option1_detail = ("Reply in the format below for a weather request:\n"
					   "Eg. 1 Oakville, Ontario")

menu_option2_detail = ("Reply in the format below for a directions request:\n"
					   "Start and end location must be separated by a slash.\n"
					   "Eg. 2 123 Regal Ct,Oakville/56 Muns,Mississuaga")

menu_option3_detail = ("Reply in the format below for a places request:\n"
					   "Category and location must be separated by a slash.\n"
					   "Eg. 3 Food/Brampton,Ontario\n"
					   "Eg. 3 Bank/Hamilton,Ontario")

menu_option4_detail = ("Reply in the format below for a news request:\n"
					   "Enter the news outlet name.\n"
					   "Eg. 4 cnn\n"
					   "Eg. 4 espn")

menu_option5_detail = ("Reply in the format below for a gas prices request:\n"
					   "Enter the location.\n"
					   "Eg. 5 Mississauga")

area_codes = [403,780,250,604,204,506,709,867,902,416,519,613,705,807,905,418,
450,514,819,306,587,778,431,782,647,226,343,249,289,581,579,438,873,639,825,236,437,365,600]

options = defaultdict(lambda:[None,'main_menu'], {'1': ['1 ','query_1','menu_option1_detail'],
	'2': ['2 ','query_2','menu_option2_detail'],
	'3': ['3 ','query_3','menu_option3_detail'],
	'4': ['4 ','query_4','menu_option4_detail'],
	'5': ['5 ','query_5','menu_option5_detail']})

def validate_command(message):
	print "validating..."

	# Drop messages from non-canadian addresses or short codes
	if (not message.address_field.startswith('+1') or
		len(message.address_field) < 12 or
		int(message.address_field[2:5]) not in area_codes):
		message.message_status = 'drop'
		return message
	else:
		message.address_field = message.address_field[2:]

	# Validate command if present
	message.message_body = message.message_body.lower()
	option = options[message.message_body[:1]]
	message.message_body = message.message_body.lstrip(option[0]).strip()
	if (message.message_body):
		message.message_status = option[1]
	else:
		message.message_status = 'menu'
		message.message_body = eval(option[2])
	return message

#validator for API calls where there are 2 parameters
def extract_parameters(message):
    if (message.message_body.count('/') == 1):
        p1,p2 = message.message_body.split('/')
        p1 = p1.strip()
        p1 = p2.strip()

        if (p1 and p2):
            return message, p1, p2
    else:
        message.message_status = 'invalid'
		message.message_body = ("Invalid query! Please specify command number" 
								"at start of query and separate locations or categories" 
								"with a single slash (/).")
    return message, None, None
