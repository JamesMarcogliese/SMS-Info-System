#!/usr/bin/python
import urllib2
import json

"""api_caller module

This module formats information for API calls and then 
makes the call to the respective API.

"""
#storing API Key's in variables
news_api = 'ed19d95d5d41476b8096018c2ce18828'
weather_api = '6c0b081fbb4411e1fc3d6836fe090fed'


#Making API call to weather API.
def weather_search(query):
    api_key = weather_api
    url = 'http://api.openweathermap.org/data/2.5/weather?APPID=' + api_key
    city = query
    final_url = url + "&q=" + city
    
    json_obj = urllib2.urlopen(final_url)
    data = json.load(json_obj)
    return data
    
    #parsing
    #print 'City Name:',
    #print (data["name"])
    #print("clouds: " + data["weather"][0]["description"])
    #print 'Temperature:' ,
    #temp = (data["main"]["temp"])
    #temp = temp - 273.15
    #print(temp)
    #print 'Humidity:',
    #print(data["main"]["humidity"])

#Making API Call to news api
def news_info(query):
    api_key = news_api
    source = query
    url = 'https://newsapi.org/v1/articles?source=' + source + '&sortBy=latest&apiKey=' + api_key
    json_obj = urllib2.urlopen(url)
    data = json.load(json_obj)
    return(data)

def places_api(list);
	"""Formats, calls, and returns results from weather API.
	
	Command and arguments passed in are formatted to API specification
	and called. Results are returned.
	
	Args: 
		split_message: Array of strings.
	
	Returns: 
		response: JSON object
	
	Raises: None.
	"""
	
	return

def directions_api(list);
	"""Formats, calls, and returns results from weather API.
	
	Command and arguments passed in are formatted to API specification
	and called. Results are returned.
	
	Args: 
		split_message: Array of strings.
	
	Returns: 
		response: JSON object
	
	Raises: None.
	"""
	
	return
	
def contacts_api(list);
	"""Formats, calls, and returns results from weather API.
	
	Command and arguments passed in are formatted to API specification
	and called. Results are returned.
	
	Args: 
		split_message: Array of strings.
	
	Returns: 
		response: JSON object
	
	Raises: None.
	"""
	
	return