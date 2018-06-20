# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field,Item

class LianjiaItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    community = Field()
    model = Field()
    area = Field()
    price = Field()
    average_price = Field()
    url = Field()
    city = Field()
    focus_num = Field()