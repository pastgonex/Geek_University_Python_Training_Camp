import time
import requests
from fake_useragent import UserAgent

ua = UserAgent(verify_ssl=False)
headers = {
    'User-Agent': ua.random,
    # F12 点登录之后, 点basic 复制 Referer
    'Referer': 'https://accounts.douban.com/passport/login_popup?login_source=anony'
}

s = requests.Session()
# 会话对象, 在同一个Session实例发出的所有请求之间保持cookie
# 期间使用urllib3 的connection pooling功能
# 向同一主机发送多个请求, 底层的TCP连接将会被重用, 从而带来显著的性能提升
login_url = 'https://accounts.douban.com/passport/setting'
from_data = {
    'ck': '',
    'name': '15055495@qq.com',
    'password': 'test123test456',
    'remember': 'false',
    'ticket': ''
}

response = s.post(login_url, data=from_data, headers=headers)

print(response.text)

# 登录后可以进行后续的请求
# url2 = 'https://accounts.douban.com/passport/setting'

# response2 = s.get(url2,headers=headers)
# response3 = nesession.get(url3,headers=headers,cookies=s.cookies)

# with open('profile.html','w+') as f:
#     f.write(response2.text)
