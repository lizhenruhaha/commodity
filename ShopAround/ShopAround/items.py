# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JdItem(scrapy.Item):
    store_names = scrapy.Field()
    shop_names = scrapy.Field()
    prices = scrapy.Field()
    shop_urls = scrapy.Field()
    pic_urls = scrapy.Field()
    search_name = scrapy.Field()


class YhdItem(scrapy.Item):
    store_names = scrapy.Field()
    shop_names = scrapy.Field()
    prices = scrapy.Field()
    shop_urls = scrapy.Field()
    pic_urls = scrapy.Field()
    search_name = scrapy.Field()


class KaolaoItem(scrapy.Item):
    store_names = scrapy.Field()
    shop_names = scrapy.Field()
    prices = scrapy.Field()
    shop_urls = scrapy.Field()
    pic_urls = scrapy.Field()
    search_name = scrapy.Field()