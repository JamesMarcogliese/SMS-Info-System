#!/usr/bin/python

"""message_validator module

This module validates commands and arguments of a message.

"""

def generate_menu():       ## Your menu design here
    print 15 * "-" , "Welcome to SIS" , 15 * "-"
    print "1. Weather"
    print "2. Directions"
    print "3. Places"
    print "4. News"
    print "5. Gas Prices"
    print 15 * "-" , "Thank you for using SIS" , 15 * "-"


def validate_command(command):
	
    if(command == 'Hello' or command == 'HELLO' or command == 'hello'):
        generate_menu()
    elif (command == "1 Weather" or command == "1 weather" or command =="1"):
        #send command to format input.
        menu_option1_detail()
    elif (command == "2 Directions" or command == "2 directions" or command == "2"):
        #send command to format input.
        menu_option2_detail()
    elif (command == "3 Places" or command ==  "3 places" or command ==  "3"):
        #send command to format input.
        menu_option3_detail()
    elif (command == "4 News" or command ==  "4 news" or command == "4"):
        #send command to format input.
        menu_option4_detail()
    elif (command == "5 Gas Prices" or command == "5 gas prices" or command == "5"):
        menu_option5_detail()
    else:
        print ("--- Please choose the right option from the menu ---")
        generate_menu()
  
        
def menu_option1_detail():
    print "Follow the formatting below for a weather request: " 
    print "Eg. 1 Oakville, Ontario"
   
    
def menu_option2_detail():
    print "Follow the formatting below for a direction request:" 
    print "Enter the start and end location separated by a slash."
    print "Eg. 2  123 Regal Ct,Oakville/56 Strathaven,Mississuaga"
 
def menu_option3_detail():   
  print "Follow the formatting below for a places request:" 
  print "Enter the category and location separated by a slash."
  print "Eg. 3 Food, Brampton, Ontario"
  print "Eg. 3 McDonalds, Hamilton, Ontario"

def menu_option4_detail():
  print "Follow the formatting below for a news request:" 
  print "Enter the news outlet name."
  print "Eg. 4 cnn-news"
  print "Eg. 4 ars-technica"


def menu_option5_detail():
    print "Follow the formatting below for a gas prices request:" 
    print "5 Mississauga"


    	

validate_command('5')
