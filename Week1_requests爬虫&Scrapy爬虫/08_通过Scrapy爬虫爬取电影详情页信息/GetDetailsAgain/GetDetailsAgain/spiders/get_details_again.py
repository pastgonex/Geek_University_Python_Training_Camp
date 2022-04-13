import scrapy
from bs4 import BeautifulSoup as bs
from GetDetailsAgain.items import GetdetailsagainItem


class GetDetailsAgainSpider(scrapy.Spider):
    name = 'get_details_again'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    # def parse(self, response):
    #     pass

    # 爬虫启动时, 引擎自动调用该方法, 并且只会被调用一次, 用于生成初始的请求对象(Request)
    # start_requests()方法读取start_urls列表中的URL并生成Request 对象, 发送给引擎
    # 引擎再指挥其他组件向网站服务器发送请求, 下载网页
    def start_requests(self):
        for i in range(0, 10):
            url = f'https://movie.douban.com/top250?start={i * 25}'
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        bs_info = bs(response.text, 'html.parser')
        title_list = bs_info.find_all('div', attrs={'class': 'hd'})

        for i in title_list:
            item = GetdetailsagainItem()
            title = i.find('a', ).find('span').get_text()
            link = i.find('a', ).get('href')
            item['title'] = title
            item['link'] = link
            yield scrapy.Request(url=link, meta={'item': item}, callback=self.parse2)

    def parse2(self, response):
        item = response.meta['item']
        bs_info = bs(response.text, 'html.parser')
        details = bs_info.find('div', attrs={'class': 'related-info'}).get_text().strip()
        item['details'] = details
        yield item
