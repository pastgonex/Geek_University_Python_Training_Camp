class Open:
    def __enter__(self):  # 首先是进入
        print("open")

    def __exit__(self, type, value, trace):  # 无论如何, __exit__中的内容最后都会执行
        print('close')

    def __call__(self):  # 把 Open类 伪装成函数使用
        pass


# 双下划线的是 魔术方法

with Open() as f:
    pass

# 上下文协议
# 其实with 就是调用了 __enter__  和 __exit__


