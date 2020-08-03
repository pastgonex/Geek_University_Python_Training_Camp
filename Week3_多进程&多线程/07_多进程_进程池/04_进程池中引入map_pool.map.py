from multiprocessing import Pool
import time


def f(x):
    return x * x


if __name__ == "__main__":
    with Pool(processes=4) as pool:
        print(pool.map(f, range(10)))  # 输出 "[0,1,4,....,81]"

        it = pool.imap(f, range(10))  # map输出为列表, imap处输出为迭代器
        print(it)
        print(next(it))
        print(next(it))

        print(it.next(timeout=1))  # 设置超时时间
