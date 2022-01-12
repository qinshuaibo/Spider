# -*- coding: utf-8 -*-
# @Time    : 2020/6/16 16:48
# @Author  : qinshuaibo
# from urllib import request
import requests
from bs4 import BeautifulSoup
import json
import time
import random
import urllib

url = 'https://www.wegene.com/demo2/male/ajax/list/'
# 'referer': 'https://www.wegene.com/demo2/male/report/%E5%81%A5%E5%BA%B7%E9%A3%8E%E9%99%A9'
# 请求的首部信息
headers = {
    'path': '/demo2/male/ajax/list/',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'x-requested-with': 'XMLHttpRequest',
    'cookie': 'c=Cud5Sn8Y-1592288838157-7b14abace4059-986461526; gr_user_id=d1eec11a-a0b8-4a65-9a25-ce2304756dd4; grwng_uid=2ed3f255-1e1e-493b-bf53-84a907ea7285; com_wegene_ZSESID=31e976lkdac6s3qtfcpi6jm1re; Hm_lvt_3ce65b2e07e6fcd47243cdcdb5f2d02b=1592288883,1592355343,1592368669; a8b79ac6da5a5179_gr_session_id=82129c2b-7e8d-4c08-ae10-cf7eb080f16c; a8b79ac6da5a5179_gr_session_id_82129c2b-7e8d-4c08-ae10-cf7eb080f16c=true; _fmdata=F4%2BIJx8rx2cVE1frFdPKFURMgqxQQDaWKT2wwNLyjMGNjdo5HSM%2B6Yl6t1G58DbQvAnQQWkHt5nk5o3SUYqlZyUwGUc9qqi9XUT8BVPCp2U%3D; _xid=X9tDj8wFoDDflVOBgO0ob6BMBkqIdNCQmXFh3aMabsQunDSHCK1PksOHJ6UgxPakKyLN%2FjPaXVz775O0bFPMUw%3D%3D; Hm_lpvt_3ce65b2e07e6fcd47243cdcdb5f2d02b=1592532793',
    'referer': 'https://www.wegene.com/demo2/male/report/%E5%81%A5%E5%BA%B7%E9%A3%8E%E9%99%A9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36',
}
# timeout = random.choice(range(80, 180))

# 利用requests对象的get方法，对指定的url发起请求
d = {'key1': 'value1', 'key2': 'value2'}
# 该方法会返回一共Response对象
res = requests.post(url, data = d)
# d = res.json()
res.encoding = 'utf-8'
d = res.json()
articles = d['gene_report']
# for article in articles:
#     yield article['title']
print(articles)
# 打印获取到的网页源码
print(res.text)
# 查看网页连接状态
print(res.status_code)
# 利用bs4进行提取网页信息，其实就是BeautifulSoup
# soup = BeautifulSoup(res.text, 'lxml')
# 找出class属性值为mod list padding 的div
# report_list = soup.find('div', {'class': 'mod list padding-left-50 padding-right-50 padding-bottom-20 border-top-none'})


# #遍历news
# for i in projects:
#     try:
#         #提取项目标题
#         titles = i.find('div', {'class': 'title'}).find('div').get_text().strip()
#         # #提取项目倍数
#         # source = i.find('span', {'class': 'color-blue'}).find('i').get_text().strip()
#         #存储爬取结果
#         projects_titles.append(titles)
#         # projects_source.append(source)
#         print(projects_titles)
#         # print(projects_source)
#
#     except AttributeError as e:
#         continue
"""
file_path = "D:shiyan.html"
with open(file_path,'w',encoding='utf-8') as f:
    f.write(data)
"""
