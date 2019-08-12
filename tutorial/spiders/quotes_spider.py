import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://www.nasdaq.com/symbol/aapl/option-chain',
        
    ]

    def parse(self, response):
        rows = response.xpath('//div [@class="OptionsChain-chart borderAll thin"]/table//tr') 
        print(type(rows[5]))
        for row in rows:
         print(row.css('td').get()) 

            
              
        
        