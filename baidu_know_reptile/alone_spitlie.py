# -*- coding:utf-8 -*-
"""
Author:秦帅波
time:2021/8/19 9:25
desc: 对百度知道具体页面内容下面的相关问题进行抓取
"""
import requests
from bs4 import BeautifulSoup

url = "https://zhidao.baidu.com/question/1867478026920727227.html?fr=iks&word=1A%C6%DA%B7%CE%B0%A9%D7%F6%C1%CB%BB%F9%D2%F2%BC%EC%B2%E2%D3%D0NF1%BA%CDVHL%CD%BB%B1%E4&ie=gbk"  # 要爬取的百度知道对应网页
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ 92.0.4515.131 Safari/537.36'}
req = requests.get(url, headers = headers)  # 提交网页请求
# soup = BeautifulSoup(req,'lxml')  TypeError: object of type 'Response' has no len()
# req返回的是response对象，BeautifulSoup无法解析response对象,可以解析response.content,content为bytes字节类型
# soup = BeautifulSoup(req.content, 'lxml')
req.encoding = 'gbk'  # 百度知道网页编码格式为‘GBK’
soup = BeautifulSoup(req.text, "html.parser", from_encoding = 'gbk')  # 百度知道网页编码格式为‘GBK’
# print(soup.prettify)  可以更好地展示网页内容

# views = soup.find('ul', class_ = 'list-34 related-ul')  # 找到列表页面中所有的相关内容
# a = views.find_all('span', class_ = 'related-restrict-title')  # 找到对应限制的标签‘related-restrict-title’，能够更加具体

# print(views)
# print(type(views))  # bs4.element.Tag
# print(a)
# b = BeautifulSoup(str(a), "html.parser")
# print('b的类型', type(b))  # bs4.element.Tag
# for i in a:
#     b = BeautifulSoup(str(i), "html.parser")
#     print('对应内容：', b.select_one(".related-restrict-title").text.strip())  # 获取对应内容


views3 = soup.find('div',class_ = 'line content')  # 找到列表页面中所有的相关内容
a3 = views3.find_all('div', accuse = 'aContent')  # 找到对应限制的标签‘best-text mb-10’，能够更加具体
# a3 = views3.find_all('div',class_ = 'wgt-best-arrowdown')  # 找到对应限制的标签‘related-restrict-title’，能够更加具体

print('输出该页面看', views3)
print('当前页面类型', type(views3))  # bs4.element.Tag
print('抓取对应的元素', a3)

for i in a3:
    b3 = BeautifulSoup(str(i), "html.parser")
    print('对应内容1', i.text)
    # print('对应内容2：', b3.select_one(".best-text mb-10").get_text())  # 获取对应内容 .text.strip()
