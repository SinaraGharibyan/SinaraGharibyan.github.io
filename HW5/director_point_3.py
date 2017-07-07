# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import scrapy


class TunSpider(scrapy.Spider):
    name = 'tun'
    allowed_domains = ['imdb.com']
    start_urls = ['http://www.imdb.com/chart/top/']
    
    

    def parse(self, response):
    	urls = response.css("td.titleColumn a::attr(href)").re("(.*)[?]")
    	new_url=[]
    	for i in range(0,10):
    		x='http://www.imdb.com'+urls[i]
    		new_url.append(x)
    	for url in new_url:

    	    yield response.follow(url, self.parse_author)	
    def parse_author(self, response):
    	
    	yield{'director':response.css('div.credit_summary_item span a span.itemprop::text').extract_first()}


    	

    	

    		
    	
    			
    	
    	
    	
