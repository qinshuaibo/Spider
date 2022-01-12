# -*- coding: utf-8 -*-
# @Time    : 2020/6/16 17:33
# @Author  : qinshuaibo
# -*- coding: utf-8 -*-
# @Time    : 2020/6/16 16:48
# @Author  : qinshuaibo  说明：虎扑是静态加载网站
import requests
from bs4 import BeautifulSoup
import csv
import urllib3
from datetime import datetime

# 请求的首部信息
headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'}
url = 'https://voice.hupu.com'
# url = 'https://www.wegene.com/demo2/male/report/%E5%81%A5%E5%BA%B7%E9%A3%8E%E9%99%A9'
# 利用requests对象的get方法，对指定的url发起请求
# 该方法会返回一共Response对象
res = requests.get(url, headers = headers)
# 通过Response对象的text方法获取网页的文本信息
print(res.text)

# 利用bs4进行提取网页信息，其实就是BeautifulSoup
soup = BeautifulSoup(res.text, 'lxml')
# 找出class属性值为news-list的div
news_list = soup.find('div', {'class': 'news-list'})
print(news_list)
# 找出news-list下的所有li标签
news = news_list.find_all('li')
news_titles = []
news_source = []
# 遍历news
for i in news:
    try:
        # 提取新闻标题
        title = i.find('h4').get_text().strip()
        # 提取新闻来源
        source = i.find('span', {'class': 'comeFrom'}).find('a').get_text().strip()
        # 存储爬取结果
        news_titles.append(title)
        news_source.append(source)
        print('新闻标题:', title)
        # print('新闻来源:',source)
        print('新闻来源:', source)
        print()
        with open(r"D:\aaa.txt", "w", encoding = 'utf-8') as file:
            for title in news_titles:
                file.writer(title.string + '\n')
    except AttributeError as e:
        continue

with open(r"D:\aaa.txt", "w", encoding = 'utf-8') as file:
    for title in news_titles:
        file.writer(title.string + '\n')
# #用append打开一个csv文件，旧的数据不会被删除
# with open('index.csv', 'w', encoding='utf-8') as csv_file:
#     csv_ouput = csv.writer(csv_file)
#     csv_ouput.writerows(news_titles)
