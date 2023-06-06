with open('user_agents.csv', 'r', encoding='utf-8') as f:
    print([line.strip() for line in f.readlines()])


    def parse11(self, response):
        # obtener todo el contenido de la pagina
        contenido = response.body.decode('utf-8')
        # variation = response.xpath('//div[@class="sc-aef7b723-0 dDQUel priceTitle"]/span/span/text()').get()
        # variation = response.xpath('//div[@class="sc-aef7b723-0 dDQUel priceSection"]')
        # price = response.xpath('//div')
        print("*"*30)
        print(f'Variation: {contenido}')
        # print(f'Variation: {price}')
        print(response.status)
        print("*"*30)
        # extract data from the response
        # yield the extracted data

    # def parse(self, response):
    #     headers = {
    #         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    #     }
    #     yield scrapy.Request(url="https://coinmarketcap.com/currencies/bitcoin/", headers=headers, callback=self.parse_data)
        
    # def parse_data(self, response):
    #     # Obtener el precio actual de Bitcoin
    #     price = response.xpath('//div[@class="priceValue "]/span/text()').get()
    #     # variation = response.xpath('//div[@class="sc-aef7b723-0 dDQUel priceTitle"]/span/span/text()').get()
    #     print("*"*30)
    #     print(f'Price: \nVariation: {price}')
    #     print(response.status)
    #     print("*"*30)
        # contenido = response.body.decode('utf-8')
    
        # Imprimir el contenido completo
        # print(contenido)
        # with open('bitcoin.html', 'w', encoding='utf-8') as f:
        #     f.write(contenido)

    
        # Realizar cualquier otra operación con el contenido completo de la página

