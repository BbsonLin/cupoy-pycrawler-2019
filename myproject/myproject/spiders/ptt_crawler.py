# -*- coding: utf-8 -*-
import scrapy


class PttCrawlerSpider(scrapy.Spider):
    name = 'ptt_crawler'
    allowed_domains = ['www.ptt.cc']
    start_urls = ['http://www.ptt.cc/']

    def parse(self, response):
        pass
