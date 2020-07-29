def chain(num):
    for i in range(num):
        yield i


num = 5
y = chain(num)
next(y)  # 取下一个值
list(y)  # 取完所有值, 并且强制转换成列表
# next(y)
