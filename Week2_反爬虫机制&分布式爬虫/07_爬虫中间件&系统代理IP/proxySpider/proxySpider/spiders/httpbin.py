import scrapy
from proxySpider.items import ProxyspiderItem


# export http_proxy='http://52.179.231.206:80'
# setting增加scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware
# 通过Request.meta['proxy'] 读取 http_proxy环境变量加载代理

class HttpbinSpider(scrapy.Spider):
    name = 'httpbin'
    allowed_domains = ['httpbin.org']
    # 通过ip查看请求的ip地址
    start_urls = ['http://httpbin.org/ip']

    # 通过 header 查看 user=agent
    # start_urls = ['http://httpbin.org/headers']

    def parse(self, response):
        print(response.text)
