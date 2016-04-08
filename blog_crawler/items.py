# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


def serialize_set(value):
    return {k: 1 for k in value}


class BlogCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    blog_time = scrapy.Field()
    content = scrapy.Field()
    category = scrapy.Field(serializer=serialize_set)
    tag = scrapy.Field(serializer=serialize_set)
    crawl_time = scrapy.Field()
