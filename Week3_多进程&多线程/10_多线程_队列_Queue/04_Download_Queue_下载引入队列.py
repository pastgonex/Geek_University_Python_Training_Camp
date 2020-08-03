import os
import queue
import threading
import requests
from fake_useragent import UserAgent


class DownloadThread(threading.Thread):
    def __init__(self, q):
        super().__init__()
        self.q = q

    def run(self):
        while True:
            url = self.q.get()  # 从队列取出一个元素
            print(f'{self.name} begin download {url}')
            self.download_file(url)  # 下载文件
            self.q.task_done()  # 下载完成发送信息

    def download_file(self, url):
        ua = UserAgent()
        headers = {"User-Agent": ua.random}
        r = requests.get(url, stream=True, headers=headers)
        fname = os.path.basename(url) + '.html'
        with open(fname, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if not chunk: break
                f.write(chunk)


if __name__ == '__main__':
    urls = ['http://www.baidu.com',
            'http://www.python.org',
            'http://www.douban.com']

    q = queue.Queue()

    for i in range(5):
        t = DownloadThread(q)  # 启动5个线程
        t.setDaemon(True)  # 即使关闭终端, 程序依然可以运行
        t.start()

    for url in urls: # 将网址放入队列
        q.put(url)

    q.join()
