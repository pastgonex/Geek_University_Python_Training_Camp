# 翻页的处理

import requests
from bs4 import BeautifulSoup as bs  # bs4是第三方库需要使用pip命令安装


# Python 使用def定义函数, myurl是函数的参数
def get_url_name(myurl):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)' \
                 'Chrome/83.0.4103.116 Safari/537.36'

    header = {'user-agent': user_agent}
    response = requests.get(myurl, headers=header)
    bs_info = bs(response.text, 'html.parser')

    # Python 中使用 for in 形式的循环, Python使用缩进来做语句块分割
    for tags in bs_info.find_all('div', attrs={'class': 'hd'}):
        for atag in tags.find_all('a'):
            # 获取所有链接
            print(atag.get('href'))
            # 获取电影名字
            print(atag.find('span', ).text)


# 生成包含所有页面的元组
urls = tuple(f'https://movie.douban.com/top250?start={page * 25}&filter=' for page in range(10))

# print(urls)

for url in urls:
    print(url)

# 控制请求的频率, 引入了time模块
from time import sleep

sleep(5)

count_page = 0
for page in urls:
    count_page+=1
    print(f'第{count_page}页')
    sleep(5)
    get_url_name(page)
