# 自己实现的使用 Beautiful 来获取 电影的上映日期
import requests

from bs4 import BeautifulSoup as bs

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)' \
             'Chrome/83.0.4103.116 Safari/537.36'

header = {'user-agent': user_agent}

myurl = 'https://movie.douban.com/top250'

response = requests.get(myurl, headers=header)

bs_info = bs(response.text, 'html.parser')

for tag in bs_info.find_all('div', attrs={'class': 'hd'}):
    atag = tag.find('a')
    print(atag.find('span').text, end=' ')
    res = requests.get(atag.get('href'), headers=header)
    bs_temp = bs(res.text, 'html.parser')
    for tagSpan in bs_temp.find_all('span', attrs={'property': 'v:initialReleaseDate'}):
        print(tagSpan.get('content'), end=' ')
    print("")
