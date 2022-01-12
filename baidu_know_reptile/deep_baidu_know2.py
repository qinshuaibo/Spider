# -*- coding:utf-8 -*-
"""
Author:秦帅波
time:2021/8/19 9:12
desc: 获取网页中第一个问题对应的答案
"""
# 导入BaiduSpider
from baiduspider import BaiduSpider
from pprint import pprint
import time
import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv
start = time.time()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ 92.0.4515.131 Safari/537.36'}

# 读取数据
data = pd.read_csv('data/待爬虫的问题.csv', encoding = 'utf-8')

id_1 = list(data.iloc[:, 0])
sentence_1 = list(data.iloc[:, 1])

print(len(id_1))
print(len(sentence_1))

# 实例化BaiduSpider
spider = BaiduSpider()

# 搜索网页
# pprint(spider.search_web(query = u'做无创基因检验时需要空腹吗?'))  # 爬取网页问题
# pprint(spider.search_zhidao(query = u'健康人群可以做哪些基因检测?'))  # 爬取百度知道问题


'''从列表中获取相关问题'''
for i, j in zip(id_1, sentence_1):
    print(i, j, end = ' ')

    with open(r'data/storage_answer.txt', 'a', encoding = 'utf-8') as f:  # 写入文件
        f.write(str(i) + str(j) + '\n')
    # pprint(spider.search_zhidao(query = j))

    a = spider.search_zhidao(query = j)
    time.sleep(5)  # 添加时间间隔
    '''从字典a中提取title和url,先从字典中提取子集'''
    # p1 = {key: value for key, value in a.items() if key in a}
    # print(p1.keys())  # p1的key值dict_keys(['results', 'total'])

    # print(a['results'])  # 输出key为reults的子集
    # print('子集类型：', type(a['results']))  # results的子集类型list

    # 从result中提取子集对应的title和url，简单起见，其实也可以改成从列表中第一个
    sub_content = []  # 存储子问题对应的问题内容
    sub_link = []  # 存储子问题对应链接
    for i in a['results']:
        # print(i)
        # print('列表中子集的类型：', type(i))  # 子集类型为dict
        print('子集中对应问题内容：', i['title'])
        # print('子集中对应问题链接：', i['url'])  # 这个没必要打印输出了
        with open(r'data/text.txt', 'a', encoding = 'utf-8') as f:
            f.write('子集中对应问题内容：' + i['title'] + '\n')
            f.write('子集中对应问题链接：' + i['url'] + '\n')
        sub_content.append(i['title'])  # 把标题添加到子内容列表中
        sub_link.append(i['url'])  # 把标题对应的链接
    try:
        req = requests.get(sub_link[0], headers = headers)  # 提交网页请求
        req.encoding = 'gbk'  # 百度知道网页编码格式为‘GBK’
        soup = BeautifulSoup(req.text, "html.parser")  # 百度知道网页编码格式为‘GBK’
        views = soup.find('div', class_ = 'line content')  # 找到列表页面中所有的相关内容
    # views = soup.find('li', class_ = 'relate-li')  # 找到列表页面中所有的相关内容


        a = views.find_all('div', accuse = 'aContent')  # 找到对应限制的标签‘related-restrict-title’，能够更加具体
        for i in a:
            b = BeautifulSoup(str(i), "html.parser")
            print('问题对应的答案：', b.text)  # 获取对应内容
            sub_question =[]
            sub_question.append(sub_content[0])
            sub_answer = []
            sub_answer.append(b.text)

            # with open(r'data/example.csv', 'a', encoding = 'utf-8') as csvfile:
            with open(r'data/storage_answer.txt', 'a', encoding = 'utf-8') as f:
                # writer = csv.writer(csvfile)
                # writer.writerow(sub_question)
                # writer.writerow(sub_answer)
                f.write('对应的问题：' + sub_content[0] + '\n')
                f.write('对应的答案：' + b.text + '\n')
    except Exception as e:
        pass

end = time.time()
print('程序运行时间：', end - start)

# a = spider.search_zhidao(query = u'健康人群可以做哪些基因检测?')
# print('a的类型：', type(a))  # 类型为dict


# url = "https://zhidao.baidu.com/question/428564093492376292.html?fr=iks&word=%BD%A1%BF%B5%C8%CB%C8%BA%BF%C9%D2%D4%D7%F6%C4%C4%D0%A9%BB%F9%D2%F2%BC%EC%B2%E2%3F&ie=gbk"  # 要爬取的百度知道对应网页
# url = "https://zhidao.baidu.com/question/1118499904139622779.html?fr=iks&word=%BD%A1%BF%B5%C8%CB%C8%BA%BF%C9%D2%D4%D7%F6%C4%C4%D0%A9%BB%F9%D2%F2%BC%EC%B2%E2%3F&ie=gbk"

# soup = BeautifulSoup(req,'lxml')  TypeError: object of type 'Response' has no len()
# req返回的是response对象，BeautifulSoup无法解析response对象,可以解析response.content,content为bytes字节类型
# soup = BeautifulSoup(req.content, 'lxml')

# print(soup.prettify)  可以更好地展示网页内容
# views = soup.find('ul', class_='tag-list__itembody taglist--inline multi')
# views = soup.find('div', class_='tag-list__itemWraper')
