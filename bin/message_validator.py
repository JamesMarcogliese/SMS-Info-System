#!/usr/bin/python

"""message_validator module

This module validates commands and arguments of an incoming message.

"""
import re
menu = ("--Welcome to SIS--\n"
		"Reply with one of the numbers below.\n"
		"1 Weather\n"
		"2 Directions\n"
		"3 Places\n"
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
	
def validate_command(command):
	command = command.lower()
    if (('' in command) or ('1 weather' in command)): 
        return menu_option1_detail
    elif (() or ('2 directions' in command)): 
        return menu_option2_detail
    elif (() or ('3 places' in command)): 
        return menu_option3_detail
    elif (() or ('4 news' in command)): 
        return menu_option4_detail
    elif (() or ('5 gas prices' in command)):
        return menu_option5_detail
    else: # If message contains anything else
        return menu
  
