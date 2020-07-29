import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    database='python_geek',
    charset='utf8mb4'
)

# 获得cursor游标对象
con1 = conn.cursor()

# 操作的行数
count = con1.execute('select * from tb1;')
print(f'查询到{count}条记录')

# 获得一条查询结果
result = con1.fetchone()  # fetch one 只获取一条   游标向下走 1 个单位
print(result)

# 获得所有查询结果
print(con1.fetchall())  # fetch all 获取所有 游标走到最后

print(con1.fetchall())  # () 空元组

con1.close()  # 先关闭游标
conn.close()  # 然后关闭数据库的连接

# 执行批量插入
# values = [(id, 'testuser' + str(id)) for id in range(4, 21)]
# cursor.executemany('INSERT INTO' + TABLE_NAME + 'values(%s,%s)', values)
