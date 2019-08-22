import scrapy
from ..items import TutorialItem
from datetime import date


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
        rows = response.xpath('//div [@class="OptionsChain-chart borderAll thin"]/table/tr')
        items['currentstockprice'] = currentstockprice
        
        
        for row in rows:
             print(row)
             args = (row.xpath('td/a/@href').get(),row.xpath('td/text()').get(),row.xpath('td[9]/text()').get())
             print('Option chain url %r and last price %r and Strike prices is %r' % args)
             optionschainscrap = row.xpath('td/a/@href').get()
             lastprice = row.xpath('td/text()').get()
             strikeprice=row.xpath('td[9]/text()').get()
             expirationdate=row.xpath('td/a/text()').get()
             optionschain=optionschainscrap[48:63]
             today = date.today()
             items['optionschain'] = optionschain
             items ['lastprice'] = lastprice
             items ['strikeprice']=strikeprice
             items['expirationdate']=expirationdate
             items['todaysdate']=today
             
             
             yield items
        
        next_page = response.xpath ('//*[@id="quotes_content_left_lb_NextPage"]/@href').get()
        if next_page is not None:
            print("Onto next page")
            yield response.follow (next_page,callback = self.parse)

                 
        
            
              
        
        # //*[@id="optionchain"]/div[5]/table/tbody/tr[1]/td[9]
        # //*[@id="optionchain"]/div[5]/table/tbody/tr[2]/td[9]