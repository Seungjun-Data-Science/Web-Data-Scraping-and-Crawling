# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from soompi.items import HackernewsItem

class HackernewsSpider(CrawlSpider):
	name = 'hackernews'
	allowed_domains = ['ycombinator.com']
	start_urls = ['https://news.ycombinator.com/']

	rules = [
	Rule(LinkExtractor(allow=['news.ycombinator.com/newest'], unique=True),
	# callback: whenever you find sth that matches the pattern, call the specified func
	callback='parse_item',
	# follow: find links and call the func repeatedly
	follow=True)
	]


	def parse_item(self, response):

		selector_list = response.css('td.title')

		for selector in selector_list:
			item = HackernewsItem()

			item['title'] = selector.xpath('a/text()').extract()
			item['url'] = selector.xpath('a/@href').extract()
			
			yield item
