# 管道
# 官方文档
# Pipe() 函数返回一个由管道连接的连接对象, 默认情况下是双工(双向）

from multiprocessing import Process, Pipe


def f(conn):
    conn.send(['倪彬琪', '刘亦菲'])
    conn.close()


if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    p.join()

# 返回的两个连接对象 Pipe() 表示管道的两端
# 每个连接对象都有send() 和 recv() 方法(相互之间的)
# 请注意, 如果两个进程(或线程) 同时尝试读取或写入管道的同一端,
# 则管道总的数据可能会损坏, 当然, 同时使用管道的不同端的进程, 不存在损坏的风险
# 管道是 队列的底层
# 还是建议使用队列
