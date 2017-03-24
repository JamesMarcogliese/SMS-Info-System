#!/usr/bin/python

import json
import requests
import re

"""api_caller module

This module formats information for API calls and then
makes the call to the respective API.

"""
#storing API Key's in variables
weather_api_key = '6c0b081fbb4411e1fc3d6836fe090fed'
place_api_key = 'AIzaSyBJ-HaEFhUJC_hz1kC3UsKpyNDz8l5n2FQ'
news_api_key = 'c743d7069e6a4f4b95e800e6915f2612'
directions_api_key = 'AIzaSyChHK_pRbyKc3BrrpqIp4MvCzcHPimfrDQ'

#Making API call to weather API.
def weather_call(query):
    payload = {'appid':weather_api_key,'q':query,'units':'metric'}
    data = requests.get('http://api.openweathermap.org/data/2.5/weather', params=payload).json()

    if (str(data['cod']) == "200"):
        _cityName = "City Name: " + (data["name"])
        _clouds = ("Clouds: " + data["weather"][0]["description"])
        _temp = "Temperature: " + str(data["main"]["temp"])
        _humidity = "Humidity: " + str(data["main"]["humidity"])
        output = _cityName + "\n" + _clouds + "\n" + _temp + "\n" + _humidity
    else:  #if no results found
        output = "NO RESULTS FOUND"
    return output

#Making API Call to news api
def news_call(source):
    print "source is:" + source

    payload = {'source':source,'apiKey':news_api_key}
    data = requests.get('https://newsapi.org/v1/articles', params=payload).json()

    #if results are found
    if (str(data['status']) == "ok"):
        count = len(data['articles'])
        for i in range (3):
            _title = "Title: " + data['articles'][i]['title']
            _desc =  "Description: " + data['articles'][i]['description']
            output = "\n" + _title + "\n" + _desc
    else:
        output = "NO RESULTS FOUND"
    return output

def places_call(place_type, address):

    place_types_dict = {'hospital', 'food', 'restaurant','hindu_temple', 'university', 'veterinary_care',
        'travel_agency', 'transit_station', 'train_station', 'taxi_stand', 'subway_station', 'store',
        'storage', 'stadium', 'spa', 'shopping_mall', 'shoe_store', 'school' ,'rv_park', 'roofing_contractor',
        'real_estate_agency', 'post_office', 'police', 'plumber', 'physiotherapist', 'pharmacy','car_rental',
        'car_repair', 'car_wash', 'casino', 'cemetry', 'pet_store', 'parking', 'park', 'painter', 'night_club',
        'museum', 'moving_company', 'movie_theatre', 'mosque', 'meal_takeaway', 'meal_delivery', 'lodging',
        'locksmith', 'local_government_office', 'liquor_store', 'library', 'lawyer', 'laundry', 'jewelry_store',
        'insuarance_agency','accounting', 'amusement_park', 'art_gallery', 'bakery', 'bank', 'bar', 'beauty_salon',
        'book_store', 'bowling_alley', 'bus_station', 'cafe', 'campground', 'car_dealer','clothing_store',
        'convenience_store', 'courthouse', 'dentist', 'department_store', 'doctor', 'electrician',
        'electronics_store', 'embassy', 'florist', 'funeral_home' ,'furniture_store', 'gas_station',
        'gym','hair_care', 'hardware_store'}

    payload = {'query':place_type+address,'key':place_api_key}
    r = requests.get('https://maps.googleapis.com/maps/api/place/textsearch/json', params=payload).json()

    #if results are found
    if (str(r['status']) == "OK"):
        count=len(r['results'])
        #for place types in the dictionary
        if place_type in place_types_dict:
            if (count > 3):
                count = 3
            for i in range(count):

                #store name and address into variables
                _name = "Name: " + r['results'][i]['name']
                _address = "Address: " + r['results'][i]['formatted_address']

                #query to get phone number
                place_id = r['results'][i]['place_id']
                payload = {'placeid':place_id,'key':place_api_key}
                r2 = requests.get('https://maps.googleapis.com/maps/api/place/details/json', params=payload).json()
                #store phone number into variable
                _phone = "Phone No: " +  r2['result']['formatted_phone_number']

                #concatenate all outputs into one variable
                output = "\n" + _name + "\n" + _address + "\n" + _phone

            return output

        #for names not in dictionary
        else:
            for i in range(count):

                #store name,address,rating,open-status into variables
                _name = "Name: " + r['results'][i]['name']
                _address = "Address: " + r['results'][i]['formatted_address']
                _rating = "Rating: " + str(r['results'][i]['rating'])
                _openStatus =  "Open: " + str(r['results'][i]['opening_hours']['open_now'])

                #query to get phone number
                place_id = r['results'][i]['place_id']
                payload = {'placeid':place_id,'key':place_api_key}
                r2 = requests.get('https://maps.googleapis.com/maps/api/place/details/json', params=payload).json()
                #store phone number into variable
                _phone = "Phone No: " +  r2['result']['formatted_phone_number']

                #concatenate all outputs into one variable
                output = "\n" + _name + "\n" + _address + "\n" + _rating + "\n" + _openStatus + "\n" + _phone

            return output
    #if no results found
    else:
        output = "NO RESULTS FOUND"
        return output

#Making API call to directions API.
def directions_call(start, end):

    start = start.replace(" ", "+");
    end = end.replace(" ", "+");
    payload = {'origin':start,'destination':end,'key':directions_api_key}
    r = requests.get('https://maps.googleapis.com/maps/api/directions/json', params=payload).json()

    #if results are found
    if (str(r['status']) == "OK"):
        #store start, end, total distance, and total time into variables
        _start = "Start location: " + r['routes'][0]['legs'][0]['start_address']
        _end = "End location: " + r['routes'][0]['legs'][0]['end_address']
        _totalDist = "Total distance: " + r['routes'][0]['legs'][0]['distance']['text']
        _totalTime = "Total time: " + r['routes'][0]['legs'][0]['duration']['text']

        #Counts the number of steps towards destination
        stepCount = len(r['routes'][0]['legs'][0]['steps'])
        #display step by step directions
        for i in range(stepCount):
            instruction = str(r['routes'][0]['legs'][0]['steps'][i]['html_instructions'])
            #adds spacing to XML tags to avoid format errors
            instruction = instruction.replace("><", "> <")
            instruction = instruction.replace(")<", ") <")
            #deletes everything between <> in relation to XML tags
            instruction = re.sub(r'<.*?>', '', instruction)
            #store time and distance into variables
            time = str(r['routes'][0]['legs'][0]['steps'][i]['duration']['text'])
            distance = str(r['routes'][0]['legs'][0]['steps'][i]['distance']['text'])
            #concatenate the steps to output
            stepString = "Step " + str(i+1) + ": "+ instruction + "  [" + time + " (" + distance + ")]\n"
            output = output + stepString
        #concatenate start,end,total distance, and total time to final output
        output = "\n" + _start + "\n" + _end + "\n" + _totalDist + "\n" + _totalTime + "\n" + output
        return output
    #if no results found
    else:
        output = "NO RESULTS FOUND"
        return output
