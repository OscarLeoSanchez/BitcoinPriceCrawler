import scrapy
from scrapy.http import Request
import random
import time
import csv
import re
import logging

def write_to_csv(data):
    with open('bitcoin_data.csv', 'a', newline='', encoding='utf-8') as f:
        if len(data) != 0:
            if ~f.tell():
                writer = csv.DictWriter(f, fieldnames=data.keys())
                writer.writeheader()
            else:
                writer = csv.DictWriter(f, fieldnames=data.keys())
            writer.writerow(data)
        else:
            print('No data to write')


def read_agent_list():
    with open('user_agents.csv', 'r', encoding='utf-8') as f:
        return [line.strip() for line in f.readlines()]
    
def clear_data(data):
    if len(data) != 0:
        #recorrer el diccionario
        for key, value in data.items():
            if value is not None:
                data[key] = re.sub(r'[,¿?$¡%)a-zA-Z]', '', value)
        return data
    else:
        return None


class BitcoinSpider(scrapy.Spider):
    name = "bitcoin"
    allowed_domains = ["coinmarketcap.com"]
    start_urls = ["https://coinmarketcap.com/currencies/bitcoin/"]

    def start_requests(self):
        user_agent_list = read_agent_list()
        # while True:
        headers = {
            'User-Agent': random.choice(user_agent_list)
        }
        logging.info("Iniciando scraping...")
        for url in self.start_urls:
            yield scrapy.Request(url=url, headers=headers, callback=self.parse)
        # time.sleep()

    def parse(self, response):
        price = response.xpath('//div[@class="sc-aef7b723-0 dDQUel priceTitle"]/div[@class="priceValue "]/span/text()').get()
        price_percent_change = response.xpath('//div[@class="sc-aef7b723-0 dDQUel priceTitle"]/span[@class="sc-97d6d2ca-0 bIyrLx"]/text()').get()
        cap = response.xpath('//div[@class="statsBlockInner"]/div[@class="statsItemRight"]/div[@class="statsValue"]/text()').getall()
        logging.info(cap)
        logging.debug(type(cap))
        logging.debug('hay {} elementos en cap'.format(len(cap)))
        if len(cap) == 3:
            market_cap = cap[0]
            fd_market_cap = cap[1]
            volume = cap[2]
        else:
            
            market_cap = None
            fd_market_cap = None
            volume = None

        volume_percent_change = response.xpath('//div[@class="statsBlockInner"]/div[@class="statsItemRight"]/span/text()').get()
        vmc = response.xpath('//div[@class="statsBlockInner"]/div[@class="sc-aef7b723-0 iDBUa-D"]/div[@class="priceValue"]/text()').get()
        cex_vol = response.xpath('//div[@class="sc-aef7b723-0 dDQUel statsLabel"]/div[@class="sc-aef7b723-0 hXeEQW"]/div[@class="volValue"]/text()').get()
        dex_vol = response.xpath('//div[@class="sc-aef7b723-0 dDQUel statsLabel"]/div[@class="sc-aef7b723-0 iDBUa-D"]/div[@class="volValue"]/text()').get()


        data = {
            'date': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),
            'price': price,
            'price_percent_change': price_percent_change,
            'market_cap': market_cap,
            'fd_market_cap': fd_market_cap,
            'volume': volume,
            'volume_percent_change': volume_percent_change,
            'volume_market_cap': vmc,
            'cex_volume': cex_vol,
            'dex_volume': dex_vol
        }
        data = clear_data(data)
        print('-------------------'*50)
        print(data)
        print('-------------------'*50)

        write_to_csv(data)
