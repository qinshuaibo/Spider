# -*- coding: utf-8 -*-
# @Time    : 2020/6/17 13:52
# @Author  : qinshuaibo

import requests
from bs4 import BeautifulSoup
import csv
import urllib3
from datetime import datetime

# 请求的首部信息
heads = {
    'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
url = 'https://www.abstractsonline.com/pp8/#!/9045/presentation/10540'
# url = 'https://www.wegene.com/demo2/male/report/%E5%81%A5%E5%BA%B7%E9%A3%8E%E9%99%A9'
# 利用requests对象的get方法，对指定的url发起请求
# 该方法会返回一共Response对象
res = requests.get(url, headers = heads, timeout = 10)
# 查看网页响应状态，能否正常访问
print(res.status_code)
# 通过Response对象的text方法获取网页的文本信息
print(res.text)
# print(res.encoding)
res.encoding = 'utf-8'
# 利用bs4进行提取网页信息，其实就是BeautifulSoup
soup = BeautifulSoup(res.text, 'html.parser')
# 找出class属性值为news-list的div
span7 = soup.find('div', {'class': 'span7'})
print(span7)
# 找出news-list下的所有dd标签
news = span7.find_all('dd')
"""
之前报错find_all，是指上一步的soup.find没有匹配到信息，
应该是里面的参数不对，这需要自己去重新解析网页，如果设置的参数没问题，有可能是获取网页的时候
"""
news_titles = []
news_source = []
# 遍历news
for i in news:
    try:
        # 提取新闻标题
        title = i.find('presenter').get_text().strip()
        # 提取新闻来源
        # source = i.find('span',{'class':'comeFrom'}).find('a').get_text().strip()
        # 存储爬取结果
        news_titles.append(title)
        # news_source.append(source)
        print('新闻标题:', title)
        # print('新闻来源:',source)
        print()
    except AttributeError as e:
        continue
