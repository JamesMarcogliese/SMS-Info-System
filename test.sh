#!/bin/bash
echo "This is a shell script"
cd gasPrices
pwd
scrapy crawl gasp -o gasp.json
python ./gasPrices/spiders/gas_prices.py
echo "I am done running reading"
