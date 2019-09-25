# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TutsplusSpider(CrawlSpider):
    name = 'tutsplus'
    allowed_domains = ['code.tutsplus.com/categories']
    start_urls = ['http://code.tutsplus.com/categories/']

    rules = (
        Rule(LinkExtractor(restrict_xpath="//a[@class='alphadex__item-link']"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpath="//a[@class='pagination__button pagination__next-button']"), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
