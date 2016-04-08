#!/usr/bin/env python
# coding=utf-8
import scrapy
from scrapy.http.request import Request
import time

from blog_crawler import utils
from blog_crawler.items import BlogCrawlerItem

__author__ = 'hbprotoss'


class AilmsSpider(scrapy.Spider):
    name = "ailms"
    allowed_domain = ["ailms.me"]
    start_urls = ["http://blog.ailms.me/"]

    # def start_requests(self):
    #     req = Request(url="http://blog.ailms.me/")
    #     req.meta["proxy"] = self.settings["HTTP_PROXY"]
    #     yield req

    def parse(self, response):
        # print response.body
        item = BlogCrawlerItem()
        article_selectors = response.xpath('//article')
        for article_selector in article_selectors:
            item["url"] = utils.str_from_xpath(article_selector, 'header/h1/a/@href')
            item["title"] = utils.str_from_xpath(article_selector, 'header/h1/a//text()')
            item["blog_time"] = utils.str_from_xpath(article_selector, 'header/div/span[@class="date"]//text()')
            item["category"] = utils.set_from_xpath(article_selector,
                                                    'header/div/span[@class="categories-links"]/a//text()')
            item["tag"] = utils.set_from_xpath(article_selector, 'header/div/span[@class="categories-links"]/a//text()')
            item["content"] = utils.str_from_xpath(article_selector, 'div[@class="entry-content"]//text()')
            item["crawl_time"] = utils.standard_time(int(time.time()))
            yield item

        next_page_url = utils.str_from_xpath(response, '//div[@class="nav-previous"]/a/@href')
        yield self.make_requests_from_url(next_page_url)
