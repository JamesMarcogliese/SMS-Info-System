import scrapy
import json
import os


class GasPriceSpider(scrapy.Spider):
    name = "gasp"
    command =   "Hamilton"

    if(command == "Mississauga"):
        start_urls = ['http://www.torontogasprices.com/mississauga/index.aspx']
    elif (command == "Toronto"):
        start_urls = ['http://www.torontogasprices.com/']
    elif (command == "Hamilton"):
        start_urls = ['http://www.hamiltongasprices.com/']

    def parse(self, response):
            price = response.css("table.p_v2")
            count = 0

            #price_address = response.css("dl.address")
            for p_low in price:
                count = count + 1
                print(count)
                if count == 3:
                    break
                yield {
                        'price': p_low.css('div.price_num::text').extract(),
                        'address': p_low.css('dd::text').extract()
            }

    #-----WARNING: If following command is executed TWICE with same file name, it messes up JSON file output and data cant be read------        
    #need to create json file by command "scrapy crawl gas_prices -o gas_prices.json"
    #edit path to json location
    path = "/home/ubuntu/Capstone-SIS/gasPrices/" + name + ".json"
    if os.path.exists(path):
        with open(path) as data_file:
            data = json.load(data_file)

        price = data[0]["price"]
        address = data[0]["address"]

        #"array" has empty data after every address since xml has empty <dd> tags
        #deletes the empty data
        address = filter(lambda name: name.strip(), address)

	for i in range(0,5):
            print price[i]
            print address[i]
        os.remove("/home/ubuntu/Capstone-SIS/gasPrices/gasp.json")
        print("File Removed!")
    else:
        print "JSON file missing or not readable"
