from sklearn import datasets  # 引入数据集

# 鸢尾花数据集
iris = datasets.load_iris()
print(iris)  # 字典

x, y = iris.data, iris.target  # data对应的value给x, target对应的value 给y
print('*' * 50)
print(x)
print('*' * 50)
print(y)

#  查看特征
iris.feature_names
print(iris.feature_names)
print('*' * 50)

# 查看标签
iris.target_names
print(iris.target_names)
print('*' * 50)

# 按照3比1的比例划分训练集和测试集
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

# load_xxx 各种数据集
# load_boston Boston房屋价格, 回归
# load_digits 手写体 分类
# load_iris 鸢尾花 分类聚类
