# 生成器
gen_number = (i for i in range(0,2))
# print(type(gen_number))
# print(gen_number)
print(next(gen_number))
print(next(gen_number))

try:
    print(next(gen_number))
except StopIteration:
    print('最后一个元素')

