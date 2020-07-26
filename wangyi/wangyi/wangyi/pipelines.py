# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient
import json


class WangyiPipeline:
    def open_spider(self, spider):
        if spider.name == 'job':
            self.file = open("wangyi.json", "w")

    def process_item(self, item, spider):
        if spider.name == 'job':
            item = dict(item)

            str_data = json.dumps(item, ensure_ascii=False) + ",\n"

            self.file.write(str_data)
        return item

    def close_spider(self, spider):
        if spider.name == 'job':
            self.file.close()


class WangyiSimplePipeline:
    def open_spider(self, spider):
        if spider.name == 'job_simple':
            self.file = open("wangyisimple.json", "w")

    def process_item(self, item, spider):
        if spider.name == 'job_simple':
            item = dict(item)

            str_data = json.dumps(item, ensure_ascii=False) + ",\n"

            self.file.write(str_data)
        return item

    def close_spider(self, spider):
        if spider.name == 'job_simple':
            self.file.close()


class MongoPipeline:
    # 将数据写入mongodb数据库,不区分爬虫
    def open_spider(self, spider):
        # ip等之类的可以从setting配置文件中写好后导入
        self.client = MongoClient('127.0.0.1', 27017)
        self.db = self.client['itcast']
        self.col = self.db['wangyi']
    
    def process_item(self, item, spider):
        data = dict(item)
        self.col.insert(data)
        return item

    def close_spider(self, spider):
        self.client.close()
