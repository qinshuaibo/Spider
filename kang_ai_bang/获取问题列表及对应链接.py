# -*- coding:utf-8 -*-
"""
Author:秦帅波
time:2021/8/17 17:28
desc:把问题列表对链接写入csv文件
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
from pandas import  DataFrame
import numpy as np

url = "http://ask.globecancer.com/tags.html"   # 要爬取的抗癌帮列表网页
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ 92.0.4515.131 Safari/537.36'}
req = requests.get(url, headers=headers)  # 提交网页请求
# soup = BeautifulSoup(req,'lxml')  TypeError: object of type 'Response' has no len()
# req返回的是response对象，BeautifulSoup无法解析response对象,可以解析response.content,content为bytes字节类型
# soup = BeautifulSoup(req.content, 'lxml')
soup = BeautifulSoup(req.text, "html.parser")
# print(soup.prettify)  可以更好地展示网页内容
# views = soup.find('ul', class_='tag-list__itembody taglist--inline multi')
# views = soup.find('div', class_='tag-list__itemWraper')
views = soup.find('div', class_='row tag-list mt20')  # 找到列表页面中所有的相关内容
# print(views)
# print(type(views))  # <class 'bs4.element.Tag'> 子迭代类型也是
# print(views.find_all('li'))  # 找到二级标题

a = views.find_all('li')
lable_name = []  # 存储名字
lable_link = []  # 存储对应访问链接
for i in a:

    # print(i,'\n')
    b = BeautifulSoup(str(i), "html.parser")
    # print(type(i))  # <class 'bs4.element.Tag'>
    # print(b.get('href'))  # 获取相对应的链接  应该先解析
    # print(b.select_one('.tagPopup').text.strip())  # 获取相对应的内容
    lable_name.append(b.select_one('.tagPopup').text.strip())
    # print(b.select_one('.tag')['href'])  # 获取对应链接
    lable_link.append(b.select_one('.tag')['href'])
    print('标签名称:', b.select_one('.tagPopup').text.strip(),'对应链接:', b.select_one('.tag')['href'])
    # print(i.select_one('tag')['href'])

print('标签名称数量:', len(lable_name))
print('标签链接:', len(lable_link))

question_name = []
question_link = []
for lable, link in zip(lable_name, lable_link):

    print('标签名称:', lable)  # 输出模块对应名称
    url = link
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ 92.0.4515.131 Safari/537.36'}
    req = requests.get(url, headers=headers)  # 提交网页请求
    soup = BeautifulSoup(req.text, "html.parser")
    views = soup.find('div', class_='news-list')  # 找到列表页面中所有的相关内容
    # print(views)
    a = views.find_all('h4')
    for i in a:
        # print(i,'\n')
        b = BeautifulSoup(str(i), "html.parser")
        question_name.append(b.select_one('.news__item-title').text.strip())
        question_link.append(b.select_one('.mr10')['href'])
        print('问题描述:', b.select_one('.news__item-title').text.strip(), '问题链接:', b.select_one('.mr10')['href'])  # 该模块下面的问题和链接
print('所有问题数量:', len(question_name))
a=set(question_name)
print('去掉重复数据后数量:',len(a))
"""写入csv文件"""
# frequence_array=np.array(question_name)[:,np.newaxis]
# amplitude_array=np.array(question_link)[:,np.newaxis]
# print("frequence_array.shape",frequence_array.shape)
# concatenate_array=np.concatenate((frequence_array,amplitude_array),axis=1)
# print("concatenate_array",concatenate_array)
# print("concatenate_array",concatenate_array.shape)
# data=DataFrame(concatenate_array,columns=["frequence","amplitude"])
# data.to_csv("data/demo.csv", encoding='utf-8_sig')