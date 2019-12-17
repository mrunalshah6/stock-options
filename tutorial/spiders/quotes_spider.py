import scrapy
from ..items import TutorialItem
from datetime import date
import requests
import json


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    val = input("Enter stock symbol of interest: ") 
    r = requests.get('https://query2.finance.yahoo.com/v7/finance/options/{}?formatted=true&crumb=whhcJDUUyvF&lang=en-US&region=US&straddle=false&corsDomain=finance.yahoo.com'.format(val))
    json_data = json.loads(r.text)
    results = json_data['optionChain']['result'][0]
    
    # for date in results['expirationDates']:
    #     print (date)
       
    
    start_urls = ['https://finance.yahoo.com/quote/{}/options?p={}&straddle=false&date={}'.format(val,val,results['expirationDates'][0]),
                  'https://finance.yahoo.com/quote/{}/options?p={}&straddle=false&date={}'.format(val,val,results['expirationDates'][1]),
                  'https://finance.yahoo.com/quote/{}/options?p={}&straddle=false&date={}'.format(val,val,results['expirationDates'][2]),
                  'https://finance.yahoo.com/quote/{}/options?p={}&straddle=false&date={}'.format(val,val,results['expirationDates'][3]),
                  'https://finance.yahoo.com/quote/{}/options?p={}&straddle=false&date={}'.format(val,val,results['expirationDates'][4]),
                  'https://finance.yahoo.com/quote/{}/options?p={}&straddle=false&date={}'.format(val,val,results['expirationDates'][5]),
                  'https://finance.yahoo.com/quote/{}/options?p={}&straddle=false&date={}'.format(val,val,results['expirationDates'][6]),
                  'https://finance.yahoo.com/quote/{}/options?p={}&straddle=false&date={}'.format(val,val,results['expirationDates'][7]),
                  'https://finance.yahoo.com/quote/{}/options?p={}&straddle=false&date={}'.format(val,val,results['expirationDates'][8]),
                  'https://finance.yahoo.com/quote/{}/options?p={}&straddle=false&date={}'.format(val,val,results['expirationDates'][9]),
                  'https://finance.yahoo.com/quote/{}/options?p={}&straddle=false&date={}'.format(val,val,results['expirationDates'][10])]

    def parse(self, response):
        items = TutorialItem()
        rows = response.xpath('//*[@id="Col1-3-OptionContracts-Proxy"]/section/section[1]/div[2]/div/table/tbody/tr')
        for row in rows:
                optionschain = row.xpath('td[1]/a/text()').get()
                strikeprice = row.xpath('td[3]/a/text()').get()
                lastprice = row.xpath('td[4]/text()').get()
                volume = row.xpath('td[9]/text()').get()
                
                print("Options chain {}".format(optionschain))
                print("Strike Price {}".format(strikeprice))
                print("Last Price {}".format(lastprice))
                print("Volume {}".format(volume))
                today = date.today()
                #print("Today's date {}".format(today))
                items['optionschain'] = optionschain
                items ['lastprice'] = lastprice
                items ['strikeprice']=strikeprice
                #items['expirationdate']=expirationdate
                items['todaysdate']=today
                yield items

            # next_page = response.xpath ('//*[@id="quotes_content_left_lb_NextPage"]/@href').get()
            # if next_page is not None:
            #     print("Onto next page")
            #     yield response.follow (next_page,callback = self.parse)


                




        # def parse(self, response):
        #     items = TutorialItem()
        #     currentstockprice = response.xpath('//div[@id="qwidget_lastsale"]/text()').get()
        #     rows = response.xpath('//div [@class="OptionsChain-chart borderAll thin"]/table/tr')
        #     items['currentstockprice'] = currentstockprice
            
            
        #     for row in rows:
        #          print(row)
        #          args = (row.xpath('td/a/@href').get(),row.xpath('td/text()').get(),row.xpath('td[9]/text()').get())
        #          print('Option chain url %r and last price %r and Strike prices is %r' % args)
        #          optionschainscrap = row.xpath('td/a/@href').get()
        #          lastprice = row.xpath('td/text()').get()
        #          strikeprice=row.xpath('td[9]/text()').get()
        #          expirationdate=row.xpath('td/a/text()').get()
        #          optionschain=optionschainscrap[48:63]
        #          today = date.today()
        #          items['optionschain'] = optionschain
        #          items ['lastprice'] = lastprice
        #          items ['strikeprice']=strikeprice
        #          items['expirationdate']=expirationdate
        #          items['todaysdate']=today
                
        #          yield items
            
        #     next_page = response.xpath ('//*[@id="quotes_content_left_lb_NextPage"]/@href').get()
        #     if next_page is not None:
        #         print("Onto next page")
        #         yield response.follow (next_page,callback = self.parse)

                 