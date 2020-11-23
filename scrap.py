import scrapy
from ..items import ScrapItem 
import json
class QuotesSpider(scrapy.Spider):
    name = "Scrap"
    start_urls = [
        '',
        #put your url
    ]

    def parse(self, response):
       
        for quote in response.css('body'): 
        #the links find from the page
            linkf=quote.css("a.ln24.result-title::attr(href)").getall()
            for link in linkf:
            	#run the links and get response and scrape the data
                yield scrapy.Request(link,callback=self.parse_details)
        ##Going to the nextpage

    def parse_details(self, response):
    	#get the datas
        items=ScrapItem()
        items['name']=response.css("h1.sc-7kepeu-0::text").get()
        items["link"]= response.url
       #this part have so many data so define another funtion and parse it
        items["detail"]={"Rating":response.css("p.sc-1hez2tp-0.lhdg1m-2.bObnWx::text").get(),
                        "food-detail":self.parse_detail(response),
                        }
        yield items
    def parse_detail(self,response):
        a=[]
        for i in response.css(".sc-1s0saks-18.cqJHJF"): 
            b={
            str(response.css("h4.sc-1s0saks-16.ezKciv::text").get()):str(response.css("span.sc-17hyc2s-1.fnhnBd::text").get()),
            }
            a.append(json.dumps(b))
        return json.dumps(a)
