from multiprocessing import Process, Queue
import os, time


def write(q):
    print('启动Write子进程: %s' % os.getpid())
    for i in ['a', 'b', 'c', 'd']:
        q.put(i)  # 写入队列
        time.sleep(1)
    print('结束Write子进程: %s' % os.getpid())


def read(q):
    print('启动Read子进程: %s' % os.getpid())
    # 写入之后读取
    # while True:  # 阻塞, 等待获取Write的值
    #     if not q.empty():
    #         value = q.get(True)  # block=True
    #         print(value)
    #     else:
    #         break

    # 读写同时进行, 需要在父进程手动 terminate()
    while True:  # 阻塞, 等待获取Write的值
        value = q.get(True)
        print(value)
    print('结束Read子进程: %s' % os.getpid())  # 这句话是不执行的

    if __name__ == '__main__':
        # 父进程创建队列, 并传递给子进程
        q = Queue()
        pw = Process(target=write, args=(q,))
        pr = Process(target=read, args=(q,))

        # 写入之后读
        # pw.start()
        # pw.join()  # 等待子进程结束
        # pr.start()
        # pr.join()

        # 写 读 同时进行,   当写入结束后, 读取也可以结束了-> terminate()
        pw.start()
        pr.start()
        pw.join()
        # pr进程是一个死循环, 无法等待其结束, 只能强行结束
        # (写进程结束了, 所以读进程也可以结束了)
        # pw.join()---> 等待pw结束,  pw结束了, pr也可以结束了
        pr.terminate()
        print('父进程结束')

    # 输出结果
    # 启动Write子进程: 85464
    # 启动Read子进程: 9896
    # a
    # b
    # c
    # d
    # 结束Write子进程: 85464
    # 父进程结束
