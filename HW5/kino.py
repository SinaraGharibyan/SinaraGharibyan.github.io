# -*- coding: utf-8 -*-
import scrapy


class KinoSpider(scrapy.Spider):
    name = 'kino'
    allowed_domains = ['http://www.imdb.com/chart/top']
    start_urls = ['http://www.imdb.com/chart/top/']

    def parse(self, response):
        rank = response.css("td.titleColumn::text").re("\d+")
        
        title = response.css("td.titleColumn a::text").extract()
        url = response.css("td.titleColumn a::attr(href)").re("(.*)[?]")
        
        year = response.css("td.titleColumn span.secondaryInfo::text").extract()
        rating = response.css("td.ratingColumn strong::text").extract()
        
        sum_rating = 0.0        	
        n = len(title)
        for i in range(n):
        	r = float(rating[i])
        	
        	sum_rating = r+sum_rating

        	yield {
        			
        		"rank": int(float(rank[i])),
        		"title": title[i],
        		"url": "http://www.imdb.com"+url[i],
        		"year": int(float(year[i].replace("(", "").replace(")",""))),
        		"rating": float(rating[i])
        			
        	}
        if(n > 0):
        		yield { "average rate": sum_rating/n}	