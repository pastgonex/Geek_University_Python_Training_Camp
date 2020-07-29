# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# 注册到settings.py文件的 ITEM_PIPELINES中, 激活组件
class XpathDetailedPipeline:
    # 每一个item管道组件都会调用该方法, 并且返回一个item对象实例或raise DropItem异常
    def process_item(self, item, spider):
        title = item['title']
        link = item['link']
        details = item['details']
        output = f'{title}|\t{link}|\t{details}|\n\n'
        with open('./getAgain.txt', 'a+', encoding='utf_8_sig') as article:
            article.write(output)
            article.close()
        return item
