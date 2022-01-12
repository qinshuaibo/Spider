# -*- coding:utf-8 -*-
"""
Author:秦帅波
time:2021/8/17 9:08
desc:抓取网页中列表模块,如"癌症分期"和对应链接
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
print(views)
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
    print(b.select_one('.tagPopup').text.strip(), b.select_one('.tag')['href'])  # 获取标签及对应链接
    # print(i.select_one('tag')['href'])
print(len(lable_name))
print(len(lable_link))


# title = views.find('li', class_='tagPopup').text.strip()  # 要记住提取文字的方法,strip()是指去掉两旁空格
# print(title)
# # link1 = soup.find('a', class_='tag').get_text
# link1 = soup.select_one('.tag')['href']
# # for link in soup.select('[href*=format="info"]'):
# #     print(link.getText(), link['href'])
# print(link1)

'''写入文件'''
# with open('title.txt', 'w') as f:  # 保存数据,write()必须是str格式 w:写；r:读；a+：追加
#     f.write(title)


