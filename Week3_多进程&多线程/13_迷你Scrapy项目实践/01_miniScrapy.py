import requests
from lxml import etree
from queue import Queue
import threading
import json
from fake_useragent import UserAgent


class CrawlThread(threading.Thread):
    """
    爬虫类
    """

    def __init__(self, thread_id, queue):  # 接收两个参数
        super().__init__()
        self.thread_id = thread_id
        self.queue = queue

    def run(self):
        """
        重写run方法
        """
        print(f'启动线程：{self.thread_id}')
        self.scheduler()
        print(f'结束线程：{self.thread_id}')

    # 模拟任务调度
    def scheduler(self):
        ua = UserAgent(verify_ssl=False)
        while True:
            if self.queue.empty():  # 队列为空不处理
                break
            else:
                page = self.queue.get()  # 先进先出的, 所以从0-10的
                print('下载线程为：', self.thread_id, " 下载页面：", page)
                url = f'https://book.douban.com/top250?start={page * 25}'
                headers = {
                    'User-Agent': ua.random
                }
                try:
                    # downloader 下载器
                    response = requests.get(url, headers=headers)
                    dataQueue.put(response.text)  # 把下载到的text放入 数据队列
                except Exception as e:
                    print('下载出现异常', e)


class ParserThread(threading.Thread):
    """
    页面内容分析
    """

    def __init__(self, thread_id, queue, file):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.queue = queue
        self.file = file

    def run(self):
        print(f'启动线程：{self.thread_id}')
        while not flag:
            try:
                item = self.queue.get(False)  # 参数为false时队列为空，抛出异常
                if not item:
                    pass
                self.parse_data(item)
                self.queue.task_done()  # get之后检测是否会阻塞
            except Exception as e:
                pass
        print(f'结束线程：{self.thread_id}')

    def parse_data(self, item):
        '''
        解析网页内容的函数
        :param item:
        :return:
        '''
        try:
            html = etree.HTML(item)
            books = html.xpath('//div[@class="pl2"]')
            for book in books:
                try:
                    title = book.xpath('./a/text()')
                    link = book.xpath('./a/@href')
                    response = {
                        'title': title,
                        'link': link
                    }
                    # 解析方法和scrapy相同，再构造一个json
                    json.dump(response, fp=self.file, ensure_ascii=False)
                except Exception as e:
                    print('book error', e)

        except Exception as e:
            print('page error', e)


dataQueue = Queue()  # 存放解析数据的queue   对 requests.get().text 做处理
flag = False

if __name__ == '__main__':
    # 将结果保存到一个json文件中
    output = open('book.json', 'a', encoding='utf-8')

    # 任务队列，存放网页的队列
    pageQueue = Queue(20)
    for page in range(0, 11):
        pageQueue.put(page)

    # 爬虫线程
    crawl_threads = []
    crawl_name_list = ['crawl_1', 'crawl_2', 'crawl_3']
    for thread_id in crawl_name_list:
        thread = CrawlThread(thread_id, pageQueue)
        thread.start()
        crawl_threads.append(thread)  # 把每个线程放入list, 用来最后关闭线程

    # 解析线程
    parse_thread = []
    parser_name_list = ['parse_1', 'parse_2', 'parse_3']
    for thread_id in parser_name_list:
        thread = ParserThread(thread_id, dataQueue, output)
        thread.start()
        parse_thread.append(thread)  # 把每个线程放入list, 用来最后关闭线程

    # 结束crawl线程
    for t in crawl_threads:
        t.join()  # 父进程等待子进程结束

    # 结束parse线程
    flag = True
    for t in parse_thread:
        t.join()  # 父进程等待子进程结束

    output.close()  # 关闭文件
    print('退出主线程')
