# -*- coding:utf-8 -*-
"""
Author:秦帅波
time:2021/8/17 10:44
desc: 获取问题对应答案
"""
import requests
from bs4 import BeautifulSoup

# url = "http://ask.globecancer.com/q-1088.html"   # 要爬取的问题对应网页上面的答案
# url = "http://ask.globecancer.com/q-663.html"   # 要爬取的问题对应网页上面的答案
# url = "http://ask.globecancer.com/q-1430.htmll"  # 胰腺癌对应的问题链接
# url = "http://ask.globecancer.com/article-15282.html"  # 验证答案为什么会重复给出
# url = "http://ask.globecancer.com/article-14963.html"  # 当没有答案时怎么处理
url = "http://ask.globecancer.com/article-15486.html"  # work-show-box
# url = "http://ask.globecancer.com/q-155.html"  # 没有p
# url = "http://ask.globecancer.com/q-1582.html"  # 多个p
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ 92.0.4515.131 Safari/537.36'}
req = requests.get(url, headers=headers)  # 提交网页请求
# soup = BeautifulSoup(req,'lxml')  TypeError: object of type 'Response' has no len()
# req返回的是response对象，BeautifulSoup无法解析response对象,可以解析response.content,content为bytes字节类型
# soup = BeautifulSoup(req.content, 'lxml')
soup = BeautifulSoup(req.text, "html.parser")

'''comment-wrap art-content'''
"""
views = soup.find('div', class_='comment-wrap art-content')  # 找到列表页面中所有的相关内容
# print(views)  # type(views))  # <class 'bs4.element.Tag'> 子迭代类型也是
if views == None:
    print(1)
a = views.find_all('answercontent')
print(views)
print('a的内容', a)
soup1 = BeautifulSoup(str(views), "html.parser")
print('问题对应的答案:',soup1.select_one(".answercontent").text.strip())
"""

# for i in soup:
#     print('获取的标签:', i, '\n')
#     b = BeautifulSoup(str(i), "html.parser")
#     # print('问题对应的答案:', soup.select_one(".answercontent").text.strip())  # 获取对应内容
#     print('问题对应的答案:', b.select_one(".p").text.strip())  # 获取胰腺癌分期对应答案内容


views = soup.find('div', class_='work-show-box')
# soup1 = BeautifulSoup(str(views), 'html.parser')
# print(soup1.string)
a = views.find_all('p')
print(a)
soup1 = BeautifulSoup(str(a), 'html.parser')

if views != None:
    a = views.find_all('p')
    soup1 = BeautifulSoup(str(a), 'html.parser')
    print('问题对应的答案', soup1.string)
    list = []
    for i in soup1:
        # print('获取的标签:', i, '\n')
        b = BeautifulSoup(str(i), "html.parser")
        # print()
        list.append(b.string)
    # if len(list) != 0:
    print('问题对应的答案:', list)
else:
    print(' ')
# if len(list)!=0:
#     print(list)
# else:
#     pass

    # print(b.get('href'))  # 获取相对应的链接  应该先解析
    # print(b.select_one('.news__item-title').get_text)  # 获取相对应的内容
    # print(b.select_one('.news__item-title').text.strip())  # 获取相对应的内容
    # print('对应链接:', b.select_one('.mr10')['href'])  # 获取对应链接
    # print(b.select_one('.news__item-title').text.strip(), b.select_one('.mr10')['href'])
    # print(i.select_one('tag')['href'])
# <h4 class="news__item-title mt0"><a class="mr10" target="_blank" href="http://ask.globecancer.com/q-663.html">食管恶性肿瘤食管下段鳞癌T3N0M0IIA期是什么期？</a></h4>

# title = soup.find('h1', class_='title-article').text.strip()  # 要记住提取文字的方法,strip()是指去掉两旁空格
# for i in views:
# title = views.find('li', class_='tagPopup').text.strip()  # 要记住提取文字的方法,strip()是指去掉两旁空格
# print(title)
# link1 = soup.find('a', class_='tag').get_text
# # for link in soup.select('[href*=format="info"]'):
# #     print(link.getText(), link['href'])
# print(link1)

# with open('title.txt', 'w') as f:  # 保存数据,write()必须是str格式 w:写；r:读；a+：追加
#     f.write(title)




