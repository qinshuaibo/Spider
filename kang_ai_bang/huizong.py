# -*- coding:utf-8 -*-
"""
Author:秦帅波
time:2021/8/17 13:28
desc:汇总爬取
"""

import requests
from bs4 import BeautifulSoup
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
    # print('标签名称:', b.select_one('.tagPopup').text.strip(),'对应链接:', b.select_one('.tag')['href'])
print('标签名称数量:', len(lable_name))
print('标签链接:', len(lable_link))

question_name = []
question_link = []
for lable, link in zip(lable_name, lable_link):
    # print('标签名称:', lable)  # 输出模块对应名称
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
        # print('问题描述:', b.select_one('.news__item-title').text.strip(), '问题链接:', b.select_one('.mr10')['href'])  # 该模块下面的问题和链接
print('所有问题数量:', len(question_name))

all_answer_list = []
for name, answer_link in zip(question_name, question_link):  # 获取问题对应的答案
    print('问题名称:', name, '问题对应答案链接:', answer_link)  # 输出问题和对应链接
    with open(r'data/cunchu.txt','a',encoding='utf-8') as f:
        f.write('问题名称：'+ name)
        f.write('问题对应答案链接：'+ answer_link)
    url = answer_link
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ 92.0.4515.131 Safari/537.36'}
    req = requests.get(url, headers=headers)  # 提交网页请求
    soup = BeautifulSoup(req.text, "html.parser")


    views = soup.find('div', class_='comment-wrap art-content')  # 找到列表页面中所有的相关内容
    if views != None:
        # a = views.find_all('p')
        a = views.find_all('answercontent')
        soup1 = BeautifulSoup(str(views), "html.parser")
        # list.append(soup1.select_one(".answercontent").text.strip())
        print('问题对应的答案:', soup1.select_one(".answercontent").text.strip())
        with open(r'data/cunchu.txt', 'a', encoding='utf-8') as f:
            f.write('问题对应的答案:' + soup1.select_one(".answercontent").text.strip())
            # list = []
            # for i in a:
            #     # print('获取的标签', i, '\n')
            #     b = BeautifulSoup(str(i), "html.parser")
            #     list.append(soup.select_one(".answercontent").text.strip())
            #     # list.append(b.string)
            # # print('问题对应的答案:', set(list))
            # #     print('问题对应的答案:', soup.select_one(".answercontent").text.strip(),'\n')  # 获取对应内容
            # #     print('问题对应的答案:', b.string, '\n')  # 获取对应内容
            # if len(list) != 0:
            #     print('问题对应的答案:', set(list))
            #
            # else:
            #     pass
        # else:
        #     print("答案为空")
        #     all_answer_list.append("答案为空")
            # pass
    # except Exception as e:
    else:
        views = soup.find('div', class_='work-show-box')
        if views != None:
            a = views.find_all('p')
            soup1 = BeautifulSoup(str(a), 'html.parser')
            list = []
            for i in soup1:
                # print('获取的标签:', i, '\n')
                b = BeautifulSoup(str(i), "html.parser")
                list.append(i.string)
            # if len(list) != 0:
            print('问题对应的答案:', list)
            with open(r'data/cunchu.txt', 'a', encoding='utf-8') as f:
                f.write('问题对应的答案:' + str(list))
            # else:

                # pass
        # else:
        #     print("答案为空")
        #     pass
        # continue




# title = views.find('li', class_='tagPopup').text.strip()  # 要记住提取文字的方法,strip()是指去掉两旁空格
# print(title)
# # link1 = soup.find('a', class_='tag').get_text
# link1 = soup.select_one('.tag')['href']
# # for link in soup.select('[href*=format="info"]'):
# #     print(link.getText(), link['href'])
# print(link1)

# with open('title.txt', 'w') as f:  # 保存数据,write()必须是str格式 w:写；r:读；a+：追加
#     f.write(title)


