import requests
from time import sleep
import pandas as pd
from bs4 import BeautifulSoup as bs
from lxml import etree


def get_details(detail_url):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)' \
                 'Chrome/83.0.4103.116 Safari/537.36'

    header = {'user-agent': user_agent}

    response = requests.get(detail_url, headers=header)

    # selector = etree.HTML(response.text)  # xml细化处理
    # filename = selector.xpath('//*[@id="content"]/h1/span[1]/text()')
    # plan_date1 = selector.xpath('//*[@id="info"]/span[10]/text()')
    # plan_date2 = selector.xpath('//*[@id="info"]/span[11]/text()')
    # rating = selector.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')
    bs_info = bs(response.text, 'html.parser')
    temp = bs_info.find('span', attrs={'property': 'v:itemreviewed'})
    filename = temp.text
    plan_date = ''
    count = 0
    for date in bs_info.find_all('span', attrs={'property': 'v:initialReleaseDate'}):
        if count > 0:
            plan_date += ','
        plan_date += date.text
        count += 1
    temp = bs_info.find('div', attrs={'class': 'rating_self clearfix'})
    rating = temp.find('strong', attrs={'class': 'll rating_num'}).text
    if count == 1:
        mylist = [(filename, plan_date,' ', rating,detail_url)]
    else:
        flag = 0
        plan_date1 = ''
        plan_date2 = ''
        for i in range(len(plan_date)):
            if plan_date[i] != ',':
                plan_date1 += plan_date[i]
            else:
                i += 1
                flag = i
                break
        for i in range(flag, len(plan_date)):
            plan_date2 += plan_date[i]
        mylist = [(filename, plan_date1, plan_date2, rating,detail_url)]

    info = pd.DataFrame(data=mylist)
    info.to_csv('./movie1.csv', mode='a', encoding='utf_8_sig', header=False, line_terminator=None, index=False)


def index_solve(myurl):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)' \
                 'Chrome/83.0.4103.116 Safari/537.36'

    header = {'user-agent': user_agent}

    response = requests.get(myurl, headers=header)

    bs_info = bs(response.text, 'html.parser')

    for tag in bs_info.find_all('div', attrs={'class': 'hd'}):
        atag = tag.find('a', )
        print(atag.get('href'))
        print(atag.find('span', ).text)
        get_details(atag.get('href'))


urls = tuple(f'https://movie.douban.com/top250?start={page * 25}&filter=' for page in range(10))

for url in urls:
    print(url)

init_list = [('电影名称', '上映日期', ' ', '评分','电影网址')]
init_title = pd.DataFrame(data=init_list)
init_title.to_csv('./movie1.csv', header=False, sep=',', encoding='utf_8_sig', index=False, line_terminator=None,
                  mode='w')

sleep(10)

page_count = 1
for url in urls:
    print(f'第{page_count}页')
    page_count += 1
    sleep(2)
    index_solve(url)
