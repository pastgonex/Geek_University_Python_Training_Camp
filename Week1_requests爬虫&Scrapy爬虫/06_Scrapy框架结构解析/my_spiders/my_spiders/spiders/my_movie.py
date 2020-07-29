import scrapy

from my_scrapy.items import MyScrapyItem

class MyMovieSpider(scrapy.Spider):
    name = 'my_movie'
    allowed_domains = ['douban.com']
    start_urls = ['http://douban.com/']

    def parse(self, response):
        pass
