from multiprocessing import Pool
import time
from traceback import format_exc
import multiprocessing
from traceback import format_exception_only


def f(x):
    return x * x


if __name__ == "__main__":
    with Pool(processes=4) as pool:  # 进程池包含个进程
        result = pool.apply_async(f, args=(10,))  # 执行一个子进程
        print(result.get(timeout=2))  # 显示执行结果

        result = pool.apply_async(time.sleep, args=(10,))
        print(result.get(timeout=2))  # 这个地方会有异常, 休眠10s, 但是时间限制是1s