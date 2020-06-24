# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyscrapyItem(scrapy.Item):

        # 小说名称
        novelName=scrapy.Field()
        # 作者名称
        authorName = scrapy.Field()
        # 小说内容页链接
        novelContent=scrapy.Field()

