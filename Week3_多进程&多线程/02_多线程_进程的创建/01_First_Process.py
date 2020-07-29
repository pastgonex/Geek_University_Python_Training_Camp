# only for linux mac
# fork()

import os

os.fork()
print('111111')

# 执行结果
# 111111
# 111111

# fork函数一旦运行就会生出一条新的进程, 2个进程一起执行导致输出了2行


