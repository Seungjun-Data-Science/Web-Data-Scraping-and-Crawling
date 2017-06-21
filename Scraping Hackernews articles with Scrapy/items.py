from scrapy import Item, Field


class HackernewsItem(Item):
	title = Field()
	url = Field()