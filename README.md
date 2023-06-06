## Scrapy-Project
#### Scrapy is a fast high-level web crawling and web scraping framework, used to crawl websites and extract structured data from their pages. It can be used for a wide range of purposes, from data mining to monitoring and automated testing.

### Project Description

This project we create a  scraper to scrape data from []() to get the price of Bitcoin and save it in a csv file. This data will be used to create a graph of the price of Bitcoin over time using the Matplotlib library and data analysis using the Pandas library.

### Project Structure
    
    ```bash
    ├── scrapy.cfg
    ├── scrapy_project
    │   ├── __init__.py
    │   ├── items.py
    │   ├── middlewares.py
    │   ├── pipelines.py
    │   ├── settings.py
    │   └── spiders
    │       ├── __init__.py
    │       └── bitcoin_spider.py
    └── README.md
    ```
### Project Installation


Use the package manager [pip](https://pip.pypa.io/en/stable/) to install [virtualenv](https://virtualenv.pypa.io/en/latest/index.html).

```bash	
pip install virtualenv
```

Create a virtual environment for a project:

```bash
virtualenv <project_name> python=3.8
```

Activate the virtual environment:

```bash
source <project_name>/bin/activate # Linux
<project_name>/Scripts/activate # Windows
```
We can create a requirements.txt file that contains a list of items to be installed using pip install:

```bash
pip install -r requirements.txt
```
Remember to activate the virtual environment every time you work on the project.

The requirements.txt file should contain the following:

```bash
scrapy
scrapy-user-agents
scrapy-rotating-proxies
```

To deactivate the virtual environment (when you're done working on your project):

```bash
deactivate
```
### Create a Scrapy Project

To create a Scrapy project, run the following command:

```bash 
scrapy startproject <project_name>
```
This project is called bitcoin_price_crawler.

Now, you should have a project structure like the one above.

```bash	
scrapy.cfg
BitcoinPriceCrawler
├── __init__.py
├── items.py
├── middlewares.py
├── pipelines.py
├── settings.py
└── spiders
    ├── __init__.py
    └── bitcoin_spider.py
```
### Create a Spider


To create a spider, run the following command:

```bash
scrapy genspider <spider_name> <url>
```
This spider is called bitcoin_spider and the url is https://coinmarketcap.com/currencies/bitcoin/historical-data/.

we execute the following command:

```bash
scrapy genspider bitcoin https://coinmarketcap.com/currencies/bitcoin/historical-data/

scrapy genspider bitcoin https://coinmarketcap.com/currencies/bitcoin/
```
Now, you should have a project structure like the one above.

```bash
scrapy.cfg
BitcoinPriceCrawler
├── __init__.py
├── items.py
├── middlewares.py
├── pipelines.py
├── settings.py
└── spiders
    ├── __init__.py
    └── bitcoin_spider.py
```
### Project Code

The code for this project is in the bitcoin_spider.py file.

```python
import scrapy
from scrapy_project.items import BitcoinPriceItem

```	
The first thing we need to do is import the scrapy module and the BitcoinPriceItem class from the items.py file.

```python
class BitcoinSpider(scrapy.Spider):
    name = 'bitcoin'
    allowed_domains = ['coinmarketcap.com']
    start_urls = ['https://coinmarketcap.com/currencies/bitcoin/']
```

Next, we create a class called BitcoinSpider that inherits from the scrapy.Spider class. We set the name of the spider to bitcoin, the allowed_domains to coinmarketcap.com, and the start_urls to https://coinmarketcap.com/currencies/bitcoin/.

We idenfiy the data we want to scrape using the Chrome DevTools. We can see that the data inspect the element and left click on the element we want to scrape and select Copy -> Copy XPath.
    
```bash
//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span
```
Now, we can use the scrapy shell to test our XPath expression.

```bash
scrapy shell https://coinmarketcap.com/currencies/bitcoin/
```
```bash
response.xpath('//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
```


```bash
[<Selector xpath='//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span' data='<span class="cmc-details-panel-price__pr'>]
```
```bash

```python
def parse(self, response):
    rows = response.xpath('//table[@class="cmc-table cmc-table___11lFC cmc-table-homepage___2_guh"]/tbody/tr')
    for row in rows:
        item = BitcoinPriceItem()
        item['date'] = row.xpath('.//td[1]/div/text()').get()
        item['open'] = row.xpath('.//td[2]/div/text()').get()
        item['high'] = row.xpath('.//td[3]/div/text()').get()
        item['low'] = row.xpath('.//td[4]/div/text()').get()
        item['close'] = row.xpath('.//td[5]/div/text()').get()
        item['volume'] = row.xpath('.//td[6]/div/text()').get()
        item['market_cap'] = row.xpath('.//td[7]/div/text()').get()
        yield item
```

### Project Usage

To run the project, you need to run the following command:

```bash
scrapy crawl bitcoin
```

### Project Output

The output of the project is a csv file that contains the price of Bitcoin over time.


### Execution / debug

```bash
scrapy crawl <nombre_del_spider> -s LOG_LEVEL=DEBUG
```



```bash
pip install scrapy
```

## More about Scrapy
### SCRAPY
- [Scrapy](https://scrapy.org/) is a fast high-level web crawling and web scraping framework, used to crawl websites and extract structured data from their pages. It can be used for a wide range of purposes, from data mining to monitoring and automated testing.

### SCRAPY-SELECTOR
- [Scrapy-Selector](
https://docs.scrapy.org/en/latest/topics/selectors.html) is a library that allows you to select parts of an XML or HTML text using CSS or XPath expressions.

### SCRAPY-SPIDER
- [Scrapy-Spider](https://docs.scrapy.org/en/latest/topics/spiders.html) is a class that defines how a certain site (or a group of sites) will be scraped, including how to perform the crawl (i.e. follow links) and how to extract structured data from their pages (i.e. scraping items). In other words, Spiders are the place where you define the custom behaviour for crawling and parsing pages for a particular site (or, in some cases, a group of sites).

### SCRAPY-ITEM
- [Scrapy-Item](https://docs.scrapy.org/en/latest/topics/items.html) is a container that will be loaded with the scraped data, it is a simple container used to collect the scraped data. It is similar to a Python dict but offers additional protection against populating undeclared fields, preventing typos.

### SCRAPY-PIPELINE
- [Scrapy-Pipeline](https://docs.scrapy.org/en/latest/topics/item-pipeline.html) is a mechanism for filtering specific types of scraped data and sending them to your database, file, etc. It is a Python class that defines what actions to take for each item (normally, how to store it in a database).

### SCRAPY-SPIDER-MIDDLEWARE
- [Scrapy-Spider-Middleware](https://docs.scrapy.org/en/latest/topics/spider-middleware.html) is a framework of hooks into Scrapy’s spider processing mechanism where you can plug custom functionality to process the responses that are sent to Spiders for processing and to process the requests and items that are generated from spiders.

### SCRAPY-DOWNLOADER-MIDDLEWARE
- [Scrapy-Downloader-Middleware](https://docs.scrapy.org/en/latest/topics/downloader-middleware.html) is a framework of hooks into Scrapy’s request/response processing. It’s a light, low-level system for globally altering Scrapy’s requests and responses.

### SCRAPY-EXTENSIONS
- [Scrapy-Extensions](https://docs.scrapy.org/en/latest/topics/extensions.html) are custom components that provide Scrapy with new functionality, or extend its existing functionality. They are located in the scrapy.extensions package and are enabled through the EXTENSIONS setting.

### SCRAPY-SETTINGS
- [Scrapy-Settings](https://docs.scrapy.org/en/latest/topics/settings.html) is a module that provides a convenient way for accessing Scrapy settings and global configuration objects.

### SCRAPY-CONTRACTS
- [Scrapy-Contracts](https://docs.scrapy.org/en/latest/topics/contracts.html) is a mechanism to declare the contract of the output (items) produced by the spiders, and validate that the output complies with it.

### SCRAPY-UTILS
- [Scrapy-Utils](https://docs.scrapy.org/en/latest/topics/utils.html) is a module that provides a collection of utilities used throughout Scrapy, such as for working with URLs, XML, and temporary files.

### SCRAPY-HTTPCACHE
- [Scrapy-Httpcache](https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#module-scrapy.downloadermiddlewares.httpcache) is a middleware to cache HTTP responses for Scrapy requests. It provides the following features:

### SCRAPY-USER-AGENTS
- [Scrapy-User-Agents](https://pypi.org/project/scrapy-user-agents/) is a downloader middleware that allows to use multiple user-agents rotating them every request. This can be useful for avoiding bans or detections, or simply to keep a low profile.

### SCRAPY-ROTATING-PROXIES
- [Scrapy-Rotating-Proxies](https://pypi.org/project/scrapy-rotating-proxies/) is a Scrapy middleware to rotate proxies and user agents based on the number of requests. This can be used to avoid IP bans and to improve crawl speed.


### INSTALLATION

- [Scrapy-Installation](https://docs.scrapy.org/en/latest/intro/install.html) is a guide to install Scrapy on your system.

### TUTORIALS

- [Scrapy-Tutorials](https://docs.scrapy.org/en/latest/intro/tutorial.html) is a guide to learn Scrapy from scratch.