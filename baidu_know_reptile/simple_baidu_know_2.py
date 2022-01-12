# -*- coding:utf-8 -*-
"""
Author:秦帅波
time:2021/7/8 8:57
desc:
"""
# 导入BaiduSpider
from baiduspider import BaiduSpider
from pprint import pprint
import time
import pandas as pd

pd_reader = pd.read_csv('E:/1_文件管理/a问答数据搜集/数据汇总/没有答案的问题筛检之后剩余1584条.csv', encoding = 'utf-8', header = None)

number = list(pd_reader.iloc[:, 2])
question = list(pd_reader.iloc[:, 3])

print(len(number))
print(len(question))

# 实例化BaiduSpider
spider = BaiduSpider()

# 搜索网页
# pprint(spider.search_web(query = u'做无创基因检验时需要空腹吗?'))  # 爬取网页问题
# pprint(spider.search_zhidao(query = u'健康人群可以做哪些基因检测?'))  # 爬取百度知道问题

'''从列表中获取相关问题'''
# for i, j in zip(a1, a2):
#     print(i + ':', j, end = '')
#     pprint(spider.search_zhidao(query = j))
#     time.sleep(2)  # 添加时间间隔


# print('a的类型：', type(a))  # 类型为dict

'''从字典a中提取title和url,先从字典中提取子集'''
# p1 = {key: value for key, value in a.items() if key in a}
# print(p1.keys())

# print('result子集', a['results'])  # 输出key为reults的子集
# print('子集类型：', type(a['results']))  # results的子集类型list
for j in question:
    a = spider.search_zhidao(query = j)
    sub_content = []
    sub_link = []
    sub_answer = []
    # 从result中提取子集对应的title和url，简单起见，其实也可以改成从列表中第一个
    for i in a['results']:
        print(i)
        # print('列表中子集的类型：', type(i))  # 子集类型为dict
        print('子集中对应问题内容：', i['title'])
        # print('子集中对应问题链接：', i['url'])
        # print('子集中对应问题答案：', i['des'])

        sub_content.append(i['title'])  # 把标题添加到子内容列表中
        sub_link.append(i['url'])  # 把标题对应的链接添加到子内容列表中
        sub_answer.append(i['des'])  # 把标题对应的答案添加到子内容列表中
    print('第一个元素', sub_content[0])
    print('第一个元素对应的答案', sub_answer[0])

    # print('长度', len(sub_content))

# for i in list:
#     print(i)
#     for page in range(1,2):
#         try:
#             pprint(spider.search_zhidao(query=i, pn=page))
#         except Exception as KeyError:
#             print('error')
