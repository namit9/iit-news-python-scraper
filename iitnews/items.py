# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IitNewsItem(scrapy.Item):
  # define the fields for your item here like:
  headline = scrapy.Field()
  synopsis = scrapy.Field()
  link = scrapy.Field()
  page_no = scrapy.Field()
  college = scrapy.Field()
  pass
