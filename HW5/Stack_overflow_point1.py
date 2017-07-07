# -*- coding: utf-8 -*-
import scrapy


class HomeSpider(scrapy.Spider):
    name = 'home'
    allowed_domains = ['https://stackoverflow.com/questions/tagged/python/']
    start_urls = []
    for i in range(1,4):
    	URL = 'https://stackoverflow.com/questions/tagged/python/?page=' + str(i) 
        start_urls.append(URL)


    def parse(self, response):
      for j in response.xpath('//*[@class="question-summary"]/div[2]/h3'):
            yield {
            'question': j.xpath('a[@class="question-hyperlink"]/text()').extract()[0],
            'url':"https://stackoverflow.com"+ j.xpath('a[@class="question-hyperlink"]/@href').extract()[0]
                
               
            }  
