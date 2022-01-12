# -*- coding: utf-8 -*-
# @Time    : 2020/6/16 14:33
# @Author  : qinshuaibo
"""
这是汇总版，前面已经验证过可以爬取，然后只需要把代码嵌套进去就行了
"""
import requests
from bs4 import BeautifulSoup
from browsermobproxy import Server
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import csv

# 实例化Options对象
chrome_options = Options()
# 把Chrome浏览器设置为静默模式
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(options=chrome_options)
driver2 = webdriver.Chrome()
# driver.get('https://www.wegene.com/demo2/male/report/%E5%81%A5%E5%BA%B7%E9%A3%8E%E9%99%A9')#遗传性疾病
# driver.get('https://www.wegene.com/demo2/male/report/%E8%BF%90%E5%8A%A8%E5%9F%BA%E5%9B%A0')#运动基因
# driver.get('https://www.wegene.com/demo2/male/report/%E8%90%A5%E5%85%BB%E4%BB%A3%E8%B0%A2')#营养代谢
# driver.get('https://www.wegene.com/demo2/male/report/%E8%8D%AF%E7%89%A9%E6%8C%87%E5%8D%97')#药物指南
# driver.get('https://www.wegene.com/demo2/male/report/%E9%81%97%E4%BC%A0%E7%89%B9%E5%BE%81')#遗传特征
# driver.get('https://www.wegene.com/demo2/male/report/%E7%9A%AE%E8%82%A4%E7%89%B9%E6%80%A7')#皮肤特征
driver.get(
    'https://www.wegene.com/demo2/male/report/%E5%BF%83%E7%90%86%E7%89%B9%E8%B4%A8')  # 心理特质

time.sleep(5)
# 获取完整渲染的网页源代码
pageSource = driver.page_source
# 打印pageSource的类型
print(type(pageSource))
# 打印pageSource
# print(pageSource)
"""
#疾病名称
titles = driver.find_elements_by_xpath("//div[@class='title']")
titles_shuliang = len(titles)
for u in titles:
    print(u.text)
"""
# print(titles_shuliang)
# //*[@id="app"]/div[2]/div/div/div[2]/div[3]/div/ul/li[2]/a
# //*[@id="app"]/div[2]/div/div/div[2]/div[3]
# 超链接
# 获取所有链接标签
links = driver.find_elements_by_xpath(
    "//div[2]/div/div/div[2]/div[2]/div/ul/li/a")

# 列表长度，一共有多少个链接标签
length = len(links)
# print('项目链接数量:',length)
for link in links:
    url = link.get_attribute('href')
    # print(url, ';', end='')
    print(url, ',', end='')
    driver2.get(url)
    time.sleep(5)
    # 检测的项目
    names = driver2.find_elements_by_xpath("//div[1]/div/div/div/div/h2")
    for name in names:
        # print(name.text, ';', end='')
        print(name.text, ',', end='')

    # 检测的基因
    genes = driver2.find_elements_by_xpath("//div[2]/div/dl/dd/span")
    time.sleep(5)
    length = len(genes)
    # print('检测基因数量: ',length,',', end='')
    # for gene in genes:
    # print(gene.text,',',end='')
    # print(';', end='')
    # print(',', end='')

    # 位点
    locals = driver2.find_elements_by_xpath("//div[@class='gene-position']")
    # //*[@id="10485"]/div[2]/div[2]/div/div[2]/div/ul/li[1]/div[1]/div[1]
    time.sleep(5)
    # locals_2 = driver2.find_elements_by_xpath("//div[@class='gene-name']")
    length = len(locals)
    print('位点数量：', length, ',', end='')
    for local in locals:
        print(local.text, ',', end='')
        # print(local.text, ';', end='')
    # print(';', end='')

    local_types = driver2.find_elements_by_xpath("//div[@class='gene-name']")
    length = len(local_types)
    # print('基因型数量:', length,',', end='')
    for local_type in local_types:
        print(local_type.text, ',', end='')
    # 位点对应的详情
    # locals_2 = driver2.find_elements_by_xpath("//div[2]/div[2]/div/div/div[2]/ul/li/div[2]/div")
    locals_2 = driver2.find_elements_by_xpath("//div[@class='toggle']/div")
    for local_2 in locals_2:
        print(local_2.get_attribute("innerText"), ',', end='')
    """
    for Type in local_types:
        print(Type.get_attribute("innerText"),',', end='')

    # print(';')
    # print(',')
    """
    print('\n')
    # 把爬取到的数据写入csv文件
    # with open('wegene.csv','w',newline='') as file:
    #     writer = csv.writer(file)
    #     writer.writerow(data.keys())

# 关闭浏览器
driver.close()
driver2.close()