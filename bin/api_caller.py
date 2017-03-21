﻿#!/usr/bin/python
import urllib2
import json
import requests


"""api_caller module

This module formats information for API calls and then 
makes the call to the respective API.

"""
#storing API Key's in variables
weather_api_key = '6c0b081fbb4411e1fc3d6836fe090fed'
place_api_key = 'AIzaSyBJ-HaEFhUJC_hz1kC3UsKpyNDz8l5n2FQ'
news_api_key = 'ed19d95d5d41476b8096018c2ce18828'
directions_api_key = 'AIzaSyChHK_pRbyKc3BrrpqIp4MvCzcHPimfrDQ'


#Making API call to weather API.
def weather_search(query):
    api_key = weather_api_key
    url = 'http://api.openweathermap.org/data/2.5/weather?APPID=' + api_key
    city = query
    final_url = url + "&q=" + city
    
    json_obj = urllib2.urlopen(final_url)
    data = json.load(json_obj)
    return data
    
    #parsing---
    print 'City Name:',
    print (data["name"])
    print("clouds: " + data["weather"][0]["description"])
    print 'Temperature:' ,
    temp = (data["main"]["temp"])
    temp = temp - 273.15
    print(temp)
    print 'Humidity:',
    print(data["main"]["humidity"])

#Making API Call to news api
def news_info(input1, input2):
    api_key = news_api_key
    source = input1
    sort= input2

    url = 'https://newsapi.org/v1/articles?source=' + source + '&sortBy=' + sort + '&apiKey=' + api_key
    json_obj = urllib2.urlopen(url)
    data = json.load(json_obj)

    #parsing---
    for i in range (0,5):
         print "Title: ", data['articles'][i]['title']
         print "Description: ", data['articles'][i]['description'] 
         print "Published Date: ", data['articles'][i]['publishedAt'] 
         print("\n")

def places_info(type, address):
    
    output=""
    loop = 0
    
    place_types_dict = {'hospital', 'food', 'restaurant','hindu_temple', 'university', 'veterinary_care', 'travel_agency', 'transit_station', 'train_station', 'taxi_stand', 'subway_station', 'store', 'storage', 'stadium', 'spa', 'shopping_mall', 'shoe_store', 'school' ,'rv_park', 'roofing_contractor', 'real_estate_agency', 'post_office', 'police', 'plumber', 'physiotherapist', 'pharmacy',
        'car_rental', 'car_repair', 'car_wash', 'casino', 'cemetry', 'pet_store', 'parking', 'park', 'painter', 'night_club', 'museum', 'moving_company', 'movie_theatre', 'mosque', 'meal_takeaway', 'meal_delivery', 'lodging', 'locksmith', 'local_government_office', 'liquor_store', 'library', 'lawyer', 'laundry', 'jewelry_store', 'insuarance_agency', 'accounting', 'amusement_park', 'art_gallery', 'bakery', 'bank', 'bar', 'beauty_salon', 'book_store', 'bowling_alley', 'bus_station', 'cafe', 'campground', 'car_dealer',
        'clothing_store', 'convenience_store', 'courthouse', 'dentist', 'department_store', 'doctor', 'electrician', 'electronics_store', 'embassy', 'florist', 'funeral_home' ,'furniture_store', 'gas_station', 'gym','hair_care', 'hardware_store'}
        
    api_key = place_api_key
    place_type = type
    place_address = address
    url_search = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query=' + place_type + place_address + '&key=' + api_key
        
    r = requests.get(url_search).json()
    
    #parsing---
    Count=len(r['results'])
    
    #if results are found
    if (str(r['status']) == "OK"):   
        #for place types in the dictionary
        if place_type in place_types_dict:
            for i in range(Count):
                
                #only print 3 results at most
                if (loop == 3):
                    break
                
                #store name and address into variables
                _name = "Name: " + r['results'][i]['name']
                _address = "Address: " + r['results'][i]['formatted_address']

                #query to get phone number
                place_id = r['results'][i]['place_id']
                url_details = 'https://maps.googleapis.com/maps/api/place/details/json?placeid=' + place_id +'&key=' + api_key
                r2 = requests.get(url_details).json()     
                #store phone number into variable
                _phone = "Phone No:" +  r2['result']['formatted_phone_number']

                #concatenate all outputs into one variable
                merge = "\n" + _name + "\n" + _address + "\n" + _phone  
                #concatenate the merged result to output
                output = output + merge 
                
                #increment loop counter
                loop = loop + 1                      
            return output
            
        #for names not in dictionary
        else:
            for i in range(Count):
                
                #only print 3 results at most
                if (loop == 3):
                    break
                
                #store name,address,rating,open-status into variables
                _name = "Name: " + r['results'][i]['name']
                _address = "Address: " + r['results'][i]['formatted_address']
                _rating = "Rating: " + str(r['results'][i]['rating'])
                _openStatus =  "Open: " + str(r['results'][i]['opening_hours']['open_now'])

                #query to get phone number
                place_id = r['results'][i]['place_id']
                url_details = 'https://maps.googleapis.com/maps/api/place/details/json?placeid=' + place_id +'&key=' + api_key
                r2 = requests.get(url_details).json()
                #store phone number into variable
                _phone = "Phone No:" +  r2['result']['formatted_phone_number']
                
                #concatenate all outputs into one variable
                merge = "\n" + _name + "\n" + _address + "\n" + _rating + "\n" + _openStatus + "\n" + _phone
                #concatenate the merged result to output
                output = output + merge 
                
                #increment loop counter
                loop = loop + 1 
            return output
            
    #if no results found
    else:
        output = "NO RESULTS FOUND"
        return output




#Making API call to directions API.
def directions_api(start, end):
    api_key = directions_api_key
    #start = "square one, mississauga"
    start = start.replace(" ", "+");
    #end = 'mcmaster university'
    end = end.replace(" ", "+");
    
    #mode {driving(default), walking, transit, bicycling}
    #avoid {tolls, highways, ferries, indoor}    
    #mode = "driving"
    #avoid = "highways"

    url = "https://maps.googleapis.com/maps/api/directions/json?origin=" + start + "&destination=" + end + "&key=" + api_key
    r = requests.get(url).json()

    #Parsing---
    #display start, end, total distance, and total time
    if (str(r['status']) == "OK"):
    
        #display start, end, total distance, and total time
        print "Start location: ", r['routes'][0]['legs'][0]['start_address']
        print "End location: ", r['routes'][0]['legs'][0]['end_address']
        print "Total distance: ", r['routes'][0]['legs'][0]['distance']['text']
        print "Total time: ", r['routes'][0]['legs'][0]['duration']['text'], "\n"
    
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
            time = str(r['routes'][0]['legs'][0]['steps'][i]['duration']['text'])
            distance = str(r['routes'][0]['legs'][0]['steps'][i]['distance']['text'])

            print "Step " + str(i+1) + ": "+ instruction + "  [" + time + " (" + distance + ")]"
    
    #if (str(r['status']) == "ZERO_RESULTS") or (str(r['status']) == "UNKNOWN_ERROR"):
    else:
        print "NO DIRECTIONS FOUND"


