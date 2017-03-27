import os
import sys
sys.path.insert(0, '/home/ubuntu/Capstone-SIS/gasPrices/gasPrices/spiders')
import gas_price

gas_price = GasPriceSpider()

def get_gasPrice(location):
    if (location.lower() == "hamilton" or location.lower() == "mississauga" or location.lower() == "toronto"):
        os.chdir("/home/ubuntu/Capstone-SIS/gasPrices")
        os.system("scrapy crawl gassp -a location=" + location + " -o gas_prices.json")
        result = gas_price.read_gasPrice()
        return result
    else:
        result = "Invalid location"
        return result
