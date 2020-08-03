# 条件锁: 该机制会使线程等待, 只有满足条件时, 才能释放n个线程

import threading


def condition():
    ret = False
    r = input('>>>')
    if r == 'yes':
        ret = True
    return ret


def func(conn, i):  # 第一个参数是锁, 第二个参数是数字, 随意
    # print(i)
    conn.acquire()
    conn.wait_for(condition)  # 这个方法接受一个函数的返回值
    print(i + 100)
    conn.release()


c = threading.Condition()  # 创建一个条件锁
for i in range(10):
    t = threading.Thread(target=func, args=(c, i,))
    t.start()

# 条件锁的原理跟设计模式中的生产者／消费者（Producer/Consumer）模式类似
