import scrapy
from bs4 import BeautifulSoup as bs
from GetDetails.items import GetdetailsItem


class GetDetailsSpider(scrapy.Spider):
    name = 'get_details'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def start_requests(self):
        for i in range(0, 10):
            url = f'https://movie.douban.com/top250?start={i * 25}&filter='
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        bs_info = bs(response.text, 'html.parser')
        title_list = bs_info.find_all('div', attrs={'class': 'hd'})

        for i in title_list:
            item = GetdetailsItem()  # 实例化
            title = i.find('a', ).find('span', ).text
            link = i.find('a', ).get('href')
            item['title'] = title
            item['link'] = link
            yield scrapy.Request(url=link, meta={'item': item}, callback=self.parse2)

    # 解析详情页
    def parse2(self, response):
        item = response.meta['item']  # 通过key取value
        bs_info = bs(response.text, 'html.parser')
        # get_text() 获取具体内容      strip() 去掉空格和两端的特殊符号
        details = bs_info.find('div', attrs={'class': 'related-info'}).get_text().strip()
        item['details'] = details
        yield item  # 每一个电影最终返回到 items.py 进行处理
