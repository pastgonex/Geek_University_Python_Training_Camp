import scrapy

from bs4 import BeautifulSoup as bs
from my_attempt.items import MyAttemptItem


class MyMovieSpider(scrapy.Spider):
    name = 'my_movie'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/top250']

    # def parse(self, response):
    #     pass

    # 生成 Request 对象, 发送(yield)给引擎
    def start_requests(self):
        urls = tuple(f'https://movie.douban.com/top250?start={i * 25}' for i in range(0, 10))
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)  # parse可以自己实现

    # 解析函数
    def parse(self, response):
        soup = bs(response.text, 'html.parser')
        title_list = soup.find_all('div', attrs={'class', 'hd'})
        items = []
        for i in title_list:
            item = MyAttemptItem()
            title = i.find('a', ).find('span', ).text
            link = i.find('a', ).get('href')
            item['title'] = title
            item['link'] = link
            items.append(item)
        return items
