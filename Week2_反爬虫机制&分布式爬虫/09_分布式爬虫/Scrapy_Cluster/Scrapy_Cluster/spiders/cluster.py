import scrapy
import json
from Scrapy_Cluster.items import ScrapyClusterItem


class ClusterSpider(scrapy.Spider):
    name = 'cluster'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/ip']

    def parse(self, response):
        print(json.loads(response.text)['origin'])
        item = ScrapyClusterItem()
        item['ip'] = json.loads(response.text)['origin']
        yield item
