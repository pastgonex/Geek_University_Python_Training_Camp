import jieba.analyse

text = '机器学习, 需要一定的数学基础, 需要掌握的数学基础知识特别多, ' \
       '如果从头到尾开始学, 估计大部分人来不及, 我建议学习最基础的数学知识'

# 基于TF-IDF算法进行关键词抽取
tfidf = jieba.analyse.extract_tags(text,
                                   topK=5,  # 权重最大的topK个关键词
                                   withWeight=True  # 返回每个关键字的权重值
                                   )

# 基于TextRank算法进行关键字抽取
textrank = jieba.analyse.textrank(text,
                                  topK=5,
                                  withWeight=True)

import pprint  # pprint模块提供了打印出任何python数据结构的类和方法

pprint.pprint(tfidf)
print('*' * 50)
pprint.pprint(textrank)

# tf-idf 算法更加精确
