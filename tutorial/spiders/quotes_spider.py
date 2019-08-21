import scrapy
from ..items import TutorialItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    val = input("Enter your value: ") 
    start_urls = [
        'https://www.nasdaq.com/symbol/{}/option-chain'.format(val),
        
    ]

    def parse(self, response):
        items = TutorialItem()
        rows = response.xpath('//div [@class="OptionsChain-chart borderAll thin"]/table/tr')
        
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
        
        next_months = response.xpath('//*[@id="OptionsChain-dates"]/a')
        for next_month in next_months:
            print(next_month)

        
            
              
        
        