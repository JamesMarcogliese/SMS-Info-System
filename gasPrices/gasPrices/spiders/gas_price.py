import scrapy
import json
import os

class GasPriceSpider(scrapy.Spider):
    name = "gassp"

    def start_requests(self):
        if (self.location.lower() == "mississauga"):
            yield scrapy.Request('http://www.torontogasprices.com/mississauga/index.aspx')
        elif (self.location.lower()  == "toronto"):
            yield scrapy.Request('http://www.torontogasprices.com/')
        elif (self.location.lower()  == "hamilton"):
            yield scrapy.Request('http://www.hamiltongasprices.com/')

    def parse(self, response):
            price = response.css("table.p_v2")
            count = 0

            for p_low in price:
                count = count + 1
                print(count)
                if count == 3:
                    break
                yield {   
                        'price': p_low.css('div.price_num::text').extract(),
                        'address': p_low.css('dd::text').extract()
           	} 
    #need to create json file by command "scrapy crawl gassp -o gas_prices.json"    
    #edit path to json location     
    def read_gasPrice(self):
        output = ""
        path = "/home/ubuntu/Capstone-SIS/gasPrices/gas_prices.json"   
        if os.path.exists(path):
            with open(path) as data_file:    
                data = json.load(data_file)  
    
            price = data[0]["price"]
            address = data[0]["address"]
    
            #"array" has empty data after every address since xml has empty <dd> tags
            #deletes the empty data
            address = filter(lambda name: name.strip(), address)    
            
            for i in range(0,5):
                #concatenate results to output
                output = output + "\n" + "Rate: " + price[i] + "\n" + "Address: " + address[i]
            os.remove("/home/ubuntu/Capstone-SIS/gasPrices/gas_prices.json")    
            return output
        
        else:
            #print "JSON file missing or not readable"
            output = "JSON file missing or not readable"
            return output
