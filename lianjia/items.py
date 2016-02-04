# -*- coding: utf-8 -*-
import scrapy

class lianjiaItem(scrapy.Item):
    name_of_community = scrapy.Field()
    layout_of_house = scrapy.Field()
    price_of_house = scrapy.Field()
    area_of_house = scrapy.Field()
    time_of_construction = scrapy.Field() #该字段将会分为：1、房屋所属楼层 2、 建设时间
