import pandas as pd
import numpy as np

group = ['x', 'y', 'z']
df = pd.DataFrame({
    'group': [group[x] for x in np.random.randint(0, len(group), 10)],
    'age': np.random.randint(15, 50, 10),
    'salary': np.random.randint(5, 50, 10)
})

# 导出为.xlsx文件
df.to_excel(excel_writer=r'file.xlsx')
# 设置Sheet名称
df.to_excel(excel_writer=r'file.xlsx', sheet_name='nbq1')

# 设置索引, 设置参数index=False 就可以在导出时把这种索引去掉
df.to_excel(excel_writer=r'file.xlsx', sheet_name='nbq2', index=False)

# 设置要导出的列
df.to_excel(excel_writer=r'file.xlsx', sheet_name='nbq3', index=False,
            columns=['group', 'age'])

# 设置编码格式
encoding = 'utf-8'  # mac/linux
encoding = 'gbk'  # windows

# 缺失值处理
na_rap = 0  # 缺失值填充为0

# 无穷值处理
inf_rep = 0

# 导出为 .csv文件
# to_csv()

# 性能
df.to_pickle('file.pkl')  # pickle的性能时excel的10倍多

df.agg(sum)  # 快
df.agg(lambda x: x.sum())  # 慢
