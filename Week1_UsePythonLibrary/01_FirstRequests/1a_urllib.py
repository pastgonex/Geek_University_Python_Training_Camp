from urllib import request # 这样引入, 可以像下面这种方式直接使用
# import urllib.request   #内部库

# GET 方法
resp = request.urlopen('http://httpbin.org/get')
print(resp.read().decode())

# POST方法
resp = request.urlopen('http://httpbin.org/post', data=b'key=value', timeout=10)
print(resp.read().decode())

# cookie

from http import cookiejar

# 创建一个cookiejar对象
cookie = cookiejar.CookieJar()

# 创建cookie处理器
handler = request.HTTPCookieProcessor(cookie)

# 创建Opener对象
opener = request.build_opener(handler)
