# http协议的get方法
import requests

r = requests.get('https://github.com')
print(r.status_code)
print(r.headers['accept-ranges'])

# r.text
# r.encoding
# r.json()

# http协议的post方法
# httpbin是专门进行http的学习和调试的网站
r = requests.post('http://httpbin.org/post', data={'key': 'value'})
print(r)
print(r.json())  # 将返回的结果json化处理
