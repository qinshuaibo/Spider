# -*- coding:utf-8 -*-
"""
Author:秦帅波
time:2021/11/5 15:21
desc:
"""


for content, link in zip(sub_content, sub_link):
            print(content, link)
            req = requests.get(link, headers = headers)  # 提交网页请求
            req.encoding = 'gbk'  # 百度知道网页编码格式为‘GBK’
            soup = BeautifulSoup(req.text, "html.parser", from_encoding = 'gbk')  # 百度知道网页编码格式为‘GBK’
            views = soup.find('ul', class_ = 'list-34 related-ul')  # 找到列表页面中所有的相关内容
            # views = soup.find('li', class_ = 'relate-li')  # 找到列表页面中所有的相关内容
            a = views.find_all('span', class_ = 'related-restrict-title')  # 找到对应限制的标签‘related-restrict-title’，能够更加具体
            for i in a:
                b = BeautifulSoup(str(i), "html.parser")
                print('子问题对应内容：', b.select_one(".related-restrict-title").text.strip())  # 获取对应内容
            # print(views)
            # print(type(views))  # bs4.element.Tag
            # print(a)
            # b = BeautifulSoup(str(a), "html.parser")
            # print('b的类型', type(b))  # bs4.element.Tag