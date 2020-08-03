import queue

q = queue.Queue(5)
q.put(111)  # 存队列
q.put(222)
q.put(333)

print(q.get())  # 取队列
print(q.get())
q.task_done()  # 每次从queue中get一个数据之后，当处理好相关问题，最后调用该方法，
# 以提示q.join()是否停止阻塞，让线程继续执行或者退出
print(q.qsize())  # 队列中元素的个数， 队列的大小
print(q.empty())  # 队列是否为空
print(q.full())  # 队列是否满了
