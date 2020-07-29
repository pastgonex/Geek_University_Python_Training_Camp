import pretty_errors  # 美化异常输出

# class UserInputError(Exception):
#     def __init__.py(self, ErrorInfo):
#         super().__init__.py(self, ErrorInfo) # ErrorInfo 是用来接收错误信息的
#         self.errorInfo = ErrorInfo
#
#     def __str__(self):
#         return self.errorInfo
#
#
# userInput = 'a'
#
# try:
#     if not userInput.isdigit():
#         raise UserInputError('用户输入错误')
# except UserInputError as ue:
#     print(ue)
# finally:
#     del userInput

# >>TODO 美化异常
# def foo():
#     1 / 0
#
# foo()

# 原始文件操作流程
# file1 = open('a.txt', encoding='utf8')  # 打开文件
# try:
#     data = file1.read()  # 读取文件内容
# finally:
#     file1.close()  # 关闭文件

# python中更加优雅的方式
with open('a.txt', encoding='utf8') as file2:
    data = file2.read()
    print(data)

