# 使用 BeautifulSoup 解析爬取到的网页

import requests
from bs4 import BeautifulSoup as bs
import bs4

# bs4 是第三方库需要使用pip命令安装

# 用户代码
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116' \
             'Safari/537.36'

# http头部信息
header = {'user-agent': user_agent}

myurl = 'https://movie.douban.com/top250'

response = requests.get(myurl, headers=header)

bs_info = bs(response.text, 'html.parser')  # 解析网页, 对response.text优化

# python 中使用 for in 形式的循环, python 使用缩进来做语句块分隔
for tags in bs_info.find_all('div',attrs={'class':'hd'}):
    for atags in tags.find_all('a',):
        print(atags.get("href"))
        print(atags.find('span',).text)





