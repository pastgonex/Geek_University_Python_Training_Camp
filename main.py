import numpy as np

import matplotlib.pyplot as plt

# 折线
x_1 = np.array([2011, 2012, 2013, 2014, 2015, 2016, 2017])
y_1 = np.array([58000, 60200, 63000, 71000, 84000, 90500, 107000])
y_2 = [52000, 54200, 51500, 58300, 56800, 59500, 62700]

#  条形图
bar_x = ['a', 'b', 'c', 'd']
bar_y = [20, 10, 30, 25]

# 直方图
s = np.random.randn(500)
print("***")
figure, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
print("***")
axes[0].plot(x_1, y_1)
print("***")
axes[1].bar(bar_x, bar_y)

plt.savefig('1.png')
plt.show()