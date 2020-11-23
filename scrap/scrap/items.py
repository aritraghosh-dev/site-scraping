# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapItem(scrapy.Item):
    # define the fields item here :
    name = scrapy.Field()
    link = scrapy.Field()
    detail = scrapy.Field()
