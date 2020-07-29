# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScrapyClusterPipeline:
    def process_item(self, item, spider):
        # 默认就可以存入settings.py中 redis的设置
        return item

# redis 存储了item
# 在Terminal中 redis-cli
# keys *    查看redis中所有的key
# type cluster:item  查看 cluster:item的类型   cluster:item是key
# lpop cluster:item  查看 cluster:item的内容
# keys *
