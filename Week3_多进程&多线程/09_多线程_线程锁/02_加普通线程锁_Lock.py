import threading
import time

num = 0

mutex = threading.Lock()  # 定义一个锁


class MyThread(threading.Thread):
    def run(self):
        global num
        time.sleep(1)

        if mutex.acquire(1):  # 加一个锁
            num = num + 1
            print(f'{self.name}: num value is {num}')
        mutex.release()  # 解锁


if __name__ == '__main__':
    for i in range(10):
        t = MyThread()
        t.start()
