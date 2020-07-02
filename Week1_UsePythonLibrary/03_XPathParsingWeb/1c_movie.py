import requests
import lxml.etree

# 爬取页面详细信息

# 电影详细页面
url = 'https://movie.douban.com/subject/1292052'

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)' \
             'Chrome/83.0.4103.116 Safari/537.36'

# 声明为字典, 使用字典的语法赋值
header = {}
header['user-agent'] = user_agent  # 相当于  {'user-agent':user_agent}
response = requests.get(url, headers=header)

# lxml细化处理
selector = lxml.etree.HTML(response.text)

# 电影名称
file_name = selector.xpath('//*[@id="content"]/h1/span[1]/text()')
print(f'电影名称: {file_name}')

# 上映日期
plan_date = selector.xpath('//*[@id="info"]/span[10]/text()')
# print('上映日期: {0}'.format(plan_date))
print(f'上映日期: {plan_date}')

# 评分
rating = selector.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')
print(f'评分: {rating}')

mylist = [file_name,plan_date,rating]

import pandas as pd

movie1 = pd.DataFrame(data=mylist)

# windows需要使用GBK字符集
movie1.to_csv('./movie1.csv',mode='a',encoding='GBK',index=False,header=False)






