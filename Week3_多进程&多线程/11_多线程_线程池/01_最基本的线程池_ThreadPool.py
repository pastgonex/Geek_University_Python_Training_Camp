import requests
from multiprocessing.dummy import Pool as ThreadPool

urls = [
    'http://www.baidu.com',
    'http://www.sina.com.cn',
    'http://www.163.com',
    'http://www.qq.com',
    'http://www.taobao.com',
]

# 开启线程池
pool = ThreadPool(4)

# 获取urls的结果
results = pool.map(requests.get, urls)
print(results)

# 关闭线程池等待任务完成退出  先关闭, 再join()
pool.close()
pool.join()

for i in results:
    print(i.status_code)
    print(i.url)
    # status_code    url  text
