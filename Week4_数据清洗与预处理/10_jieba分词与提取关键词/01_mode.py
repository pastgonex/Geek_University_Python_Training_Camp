import jieba

strings = ['我叫倪彬琪', 'Python训练营真有趣!']

for string in strings:
    result = jieba.cut(string, cut_all=False)  # 默认就是精确模式
    print('Default Mode: ' + '/'.join(list(result)))

for string in strings:
    result = jieba.cut(string, cut_all=True)  # 全模式 用于搜索
    print('Full Mode: ' + '/'.join(list(result)))

result = jieba.cut('钟南山院士接受采访新冠不会二次爆发')  # 默认是 精确模式
print('/'.join(list(result)))
# "新冠" 在词典中没有, 但是被 Viterbi 算法识别出来了

result = jieba.cut_for_search('小明硕士毕业于中国科学院计算所, 后在日本京都大学深造')  # 搜索引擎模式
print('Search Mode: ' + '/'.join(list(result)))
print(result)  # 返回的结果是一个生成器
