import scrapy
from ..items import TutorialItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    val = input("Enter stock symbol of interest: ") 
    start_urls = [
        'https://www.nasdaq.com/symbol/{}/option-chain'.format(val),
        'https://www.nasdaq.com/symbol/{}/option-chain?dateindex=1'.format(val),
        'https://www.nasdaq.com/symbol/{}/option-chain?dateindex=2'.format(val),
        'https://www.nasdaq.com/symbol/{}/option-chain?dateindex=3'.format(val),
        'https://www.nasdaq.com/symbol/{}/option-chain?dateindex=4'.format(val),
        'https://www.nasdaq.com/symbol/{}/option-chain?dateindex=5'.format(val),
        'https://www.nasdaq.com/symbol/{}/option-chain?dateindex=6'.format(val),
        'https://www.nasdaq.com/symbol/{}/option-chain?dateindex=7'.format(val),
        'https://www.nasdaq.com/symbol/{}/option-chain?dateindex=8'.format(val),
        'https://www.nasdaq.com/symbol/{}/option-chain?dateindex=9'.format(val),
        'https://www.nasdaq.com/symbol/{}/option-chain?dateindex=10'.format(val),
        'https://www.nasdaq.com/symbol/{}/option-chain?dateindex=11'.format(val),

        
    ]

    def parse(self, response):
        items = TutorialItem()
        currentstockprice = response.xpath('//div[@id="qwidget_lastsale"]/text()').get()
        print(currentstockprice)
        rows = response.xpath('//div [@class="OptionsChain-chart borderAll thin"]/table/tr')
        items['currentstockprice'] = currentstockprice
        
        for row in rows:
            
             args = (row.xpath('td/a/@href').get(),row.xpath('td/text()').get())
             print('Option chain url %r and last price %r' % args)
             optionschainscrap = row.xpath('td/a/@href').get()
             lastprice = row.xpath('td/text()').get()
             optionschain=optionschainscrap[48:63]
             items['optionschain'] = optionschain
             items ['lastprice'] = lastprice
             
             yield items
        
        next_page = response.xpath ('//*[@id="quotes_content_left_lb_NextPage"]/@href').get()
        if next_page is not None:
            print("Onto next page")
            yield response.follow (next_page,callback = self.parse)

                 
        
            
              
        
        