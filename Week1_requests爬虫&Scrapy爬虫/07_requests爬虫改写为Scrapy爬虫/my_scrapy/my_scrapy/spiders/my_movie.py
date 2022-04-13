import scrapy
from bs4 import BeautifulSoup as bs
from my_scrapy.items import MyScrapyItem


class MyMovieSpider(scrapy.Spider):
    name = 'my_movie'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    #   注释默认的parse函数
    #   def parse(self, response):
    #        pass

    # 爬虫启动时，引擎自动调用该方法，并且只会被调用一次，用于生成初始的请求对象（Request）。
    # start_requests()方法读取start_urls列表中的URL并生成Request对象，发送给引擎。
    # 引擎再指挥其他组件向网站服务器发送请求，下载网页
    def start_requests(self):
        for i in range(0, 10):
            url = f'https://movie.douban.com/top250?start={i * 25}'
            yield scrapy.Request(url=url, callback=self.parse)
            # url 请求访问的网址
            # callback 回调函数，引擎回将下载好的页面(Response对象)发给该方法，执行数据解析
            # 这里可以使用callback指定新的函数，不是用parse作为默认的回调参数

    # 解析函数
    def parse(self, response):
        items = []
        soup = bs(response.text, 'html.parser')
        title_list = soup.find_all('div', attrs={'class': 'hd'})
        # for i in range(len(title_list)):
        # 在Python中应该这样写
        for i in title_list:
            # 在items.py定义
            item = MyScrapyItem()
            title = i.find('a').find('span', ).text
            link = i.find('a').get('href')
            item['title'] = title
            item['link'] = link
            items.append(item)
        return items
        # yield scrapy.Request(url=link, meta={'item': item}, callback=self.parse2)

    # # 解析具体页面
    # def parse2(self, response):
    #     item = response.meta['item']
    #     soup = bs(response.text, 'html.parser')
    #     content = soup.find('div', attrs={'class': 'related-info'}).get_text().strip()
    #     item['content'] = content
    #     yield item
