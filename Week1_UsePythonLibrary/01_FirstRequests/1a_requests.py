# 使用requests库获取豆瓣影评

import requests

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 ' \
             'Safari/537.36'  # 通过\来换行

header = {'user-agent': user_agent}

myurl = 'https://movie.douban.com/top250'

response = requests.get(myurl, headers=header)  # headers这个参数的作用是让requests尽可能模拟浏览器

print(response.text)
print(f'返回码是: {response.status_code}')  # 返回网页的状态码
