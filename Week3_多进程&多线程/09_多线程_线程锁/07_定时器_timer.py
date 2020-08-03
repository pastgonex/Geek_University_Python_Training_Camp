import threading


def hello():
    print('hello world')


t = threading.Timer(1, hello)  # 表示1秒后执行hello函数
t.start()
