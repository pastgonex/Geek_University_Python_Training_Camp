# 参数
# multiprocessing.Process(group=None, target=None,name=None,args=(),kwargs={})

# - group, 分组, 实际上很少使用
# - target, 表示调用对象, 你额可以传入方法的名字
# - name, 别名, 相当于给这个进程取一个名字
# - args, 表示被调用对象的位置参数元组, 比如target是函数a, 他有两个参数m,n, 那么args就传入(m,n)即可
# - kwargs, 表示调用对象的字典

from multiprocessing import Process


def f(name):
    print(f'hello {name}')


if __name__ == '__main__':
    p = Process(target=f, args=('nbq',))
    p.start()
    p.join()

# join([timeout])
# 如果可选参数 timeout是 None(默认值), 则该方法将阻塞
# 知道调用join()方法的进程终止, 如果timeout是一个正数,
# 他最多会阻塞timeout秒
# 请注意, 如果进程终止或方法超市, 则该方法返回None
# 检查进程的exitcode以确定他是否终止
# 一个进程可以合并多次
# 进程无法并入自身, 因为这回导致死锁
# 尝试在启动进程之前合并进程是错误的---> join() 不能在 start() 之前