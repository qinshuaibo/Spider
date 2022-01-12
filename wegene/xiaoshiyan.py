# -*- coding: utf-8 -*-
# @Time    : 2020/6/18 16:01
# @Author  : qinshuaibo
import requests
from bs4 import BeautifulSoup
import json
import time
import random
import urllib

url = 'https://www.wegene.com/demo2/male/ajax/json'
# 'referer': 'https://www.wegene.com/demo2/male/report/%E5%81%A5%E5%BA%B7%E9%A3%8E%E9%99%A9'
# 请求的首部信息
headers = {
    'path': '/demo2/male/ajax/list/',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'x-requested-with': 'XMLHttpRequest',
    'cookie': 'c=Cud5Sn8Y-1592288838157-7b14abace4059-986461526; gr_user_id=d1eec11a-a0b8-4a65-9a25-ce2304756dd4; grwng_uid=2ed3f255-1e1e-493b-bf53-84a907ea7285; com_wegene_ZSESID=31e976lkdac6s3qtfcpi6jm1re; Hm_lvt_3ce65b2e07e6fcd47243cdcdb5f2d02b=1592288883,1592355343,1592368669; a8b79ac6da5a5179_gr_session_id=310f190d-7e9f-4217-a438-f5c073219af5; a8b79ac6da5a5179_gr_session_id_310f190d-7e9f-4217-a438-f5c073219af5=true; Hm_lpvt_3ce65b2e07e6fcd47243cdcdb5f2d02b=1592456764; _fmdata=F4%2BIJx8rx2cVE1frFdPKFURMgqxQQDaWKT2wwNLyjMGNjdo5HSM%2B6Yl6t1G58DbQLO44W8VsuqzgezLR6sSqYckN6I2TIm%2FDTAwmePFQRpU%3D; _xid=U4R9Xi6uGyHuls3YLML8452g%2F0PULQBlVBmDFrWlqAup8GP0e1vzDyc9iBLZow5RnzF%2B%2BAL6hqX6MFyW0NNDsA%3D%3D',
    'referer': 'https://www.wegene.com/demo2/male/detail/66',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36',
}
# timeout = random.choice(range(80, 180))

# 利用requests对象的get方法，对指定的url发起请求
# 该方法会返回一共Response对象
res = requests.get(url, headers = headers)
# d = res.json()
res.encoding = 'utf-8'
# 打印获取到的网页源码
print(res.text)
# 查看网页连接状态
print(res.status_code)
# 利用bs4进行提取网页信息，其实就是BeautifulSoup
soup = BeautifulSoup(res.text, 'lxml')
# 找出class属性值为mod list padding 的div
report_list = soup.find('div', {'class': 'tab-pane active tab-pane-1'})

# 找出col-sm-8 report-list下的所有li标签
projects = report_list.find_all('dd')
# projects_titles = []
projects_source = []

# 遍历news
for i in projects:
    try:
        # 提取项目标题
        # titles = i.find('div', {'class': 'title'}).find('div').get_text().strip()
        # #提取项目倍数
        source = i.find('span', {'class': 'color-wegene-blue font-weight-bold'}).find('span').get_text().strip()
        # 存储爬取结果
        # projects_titles.append(titles)
        projects_source.append(source)
        print(projects_source)
        # print(projects_source)

    except AttributeError as e:
        continue
