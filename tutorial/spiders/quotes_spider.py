import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://www.nasdaq.com/symbol/aapl/option-chain?dateindex=1',
        
    ]

    def parse(self, response):
        rows = response.xpath('//div [@class="OptionsChain-chart borderAll thin"]/table/tr')
        storage = {}
        for row in rows:
            #  print (row.get())
            #  print(row.xpath('td/a/@href').get())
            #  print(row.xpath('td/text()').get())
             args = (row.xpath('td/a/@href').get(),row.xpath('td/text()').get())
             print('Option chain url %r and last price %r' % args)
             optionschain = row.xpath('td/a/@href').get()
             lastprice = row.xpath('td/text()').get()
             storage[optionschain[48:63]] = lastprice
        return storage
             

            
              
        
        