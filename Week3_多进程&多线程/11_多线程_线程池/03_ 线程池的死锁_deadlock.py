import time
from concurrent.futures import ThreadPoolExecutor


def wait_on_b():
    time.sleep(5)
    print(b.result())  # b will never complete because it is waiting on a
    return 5


def wait_on_a():
    time.sleep(5)
    print(a.result())  # a will never complete because it is waiting on b
    return 6


executor = ThreadPoolExecutor(max_workers=2)

a = executor.submit(wait_on_b)
b = executor.submit(wait_on_a)

# 当回调已关联一个Future 然后再等待另一个Future 的结果就会发生死锁
# https://docs.python.org/zh-cn/3.7/library/concurrent.futures.html#threadpoolexecutor
