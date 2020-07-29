# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class GetdetailsPipeline:
    def process_item(self, item, spider):
        title = item['title']
        link = item['link']
        details = item['details']
        output = f'|{title}|\t{link}|\t{details}|\n\n'
        with open('./doubanMovie.txt','a+',encoding='utf-8') as article:
            article.write(output)
            article.close()
        return item # 输出在 终端上
