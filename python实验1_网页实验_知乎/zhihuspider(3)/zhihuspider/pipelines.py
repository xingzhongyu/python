# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient
from zhihuspider.items import User,Posts

class ZhihuspiderPipeline:
    def open_spider(self,spider):
        mongo=MongoClient()
        self.UserCollection=mongo["zhihu3"]["users"]
        self.PostCollection=mongo["zhihu3"]["posts"]
    def process_item(self, item, spider):
        if isinstance(item,User):
            self.UserCollection.insert(dict(item))
            # print(item)
        elif isinstance(item,Posts):
            self.PostCollection.insert(dict(item))
            # print(item)
        # self.collection.insert(dict(item))
        return item
