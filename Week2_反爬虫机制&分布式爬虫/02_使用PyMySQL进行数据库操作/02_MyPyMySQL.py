# 开始-创建connection-获取cursor-CRUD(查询并获取数据)-关闭cursor-关闭连接

import pymysql

dbInfo = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'db': 'python_geek'
}

sqls = ['select 1', 'select version()']

result = []


class ConnDB(object):
    def __init__(self, dbInfo, sqls):
        self.host = dbInfo['host']
        self.port = dbInfo['port']
        self.user = dbInfo['user']
        self.password = dbInfo['password']
        self.db = dbInfo['db']
        self.sqls = sqls

    def run(self):
        conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db
        )
        # 游标建立就开启了一个隐形的事物
        cur = conn.cursor()
        try:
            for command in self.sqls:
                cur.execute(command)
                result.append(cur.fetchone())
            # 关闭游标
            cur.close()
            conn.commit()
        except:
            conn.rollback()  # 如果失败, 则数据回滚, 相当于什么都没有发生
        # 关闭数据库连接
        conn.close()


# 除了类似与C语言的主程序的入口之外
# 如果作为模块导入, 那么这一部分不会被执行, 只有单独执行这一部分才会执行
if __name__ == "__main__":
    db = ConnDB(dbInfo, sqls)
    db.run()
    print(result)
