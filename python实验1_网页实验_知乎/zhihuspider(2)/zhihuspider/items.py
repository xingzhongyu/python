# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class User(scrapy.Item):
    name = scrapy.Field()
    info = scrapy.Field()
    followers=scrapy.Field()
    like=scrapy.Field()
class Posts(scrapy.Item):
    content=scrapy.Field()
    voteCount=scrapy.Field()
class Topics(scrapy.Item):
    name=scrapy.Field()
    title=scrapy.Field()
    num=scrapy.Field()
class Topics2(scrapy.Item):
    name=scrapy.Field()
    title=scrapy.Field()
    qnum=scrapy.Field()
    des=scrapy.Field()
    followers=scrapy.Field()