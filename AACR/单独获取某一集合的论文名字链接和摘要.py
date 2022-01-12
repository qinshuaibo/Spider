# -*- coding: utf-8 -*-
# @Time    : 2020/7/14 20:54
# @Author  : qinshuaibo
# -*- coding: utf-8 -*-
# @Time    : 2020/7/14 18:55
# @Author  : qinshuaibo
import requests
from bs4 import BeautifulSoup
from browsermobproxy import Server
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from docx import Document
from docx.shared import Pt
import os
import time
import csv
import codecs
# 实例化Options对象
chrome_options = Options()
# 把Chrome浏览器设置为静默模式
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)
driver2 = webdriver.Chrome()
driver.get('https://bit.ly/2ybQ01z')
time.sleep(5)
# 获取完整渲染的网页源代码
pageSource = driver.page_source
# 打印pageSource的类型
print(type(pageSource))
# 打印pageSource
# print(pageSource)
# 集合名称
# titles = driver.find_elements_by_xpath("//div[@class='title']")
# titles = driver.find_elements_by_xpath("//body/div[7]/div[2]/div/ul[1]/li/a")
titles = driver.find_elements_by_xpath("//div/div[2]/div[2]/table/tbody/tr/td[2]/a")

titles_shuliang = len(titles)
print(titles_shuliang)
for title in titles:
    if len(title.get_attribute("innerText")) > 20:
        print(title.get_attribute("innerText"))
        print(len(title.get_attribute("innerText")))

# 超链接
# 获取所有带链接的标签
links = driver.find_elements_by_xpath("//div/div[2]/div[2]/table/tbody/tr/td[2]/a")
# 列表长度，一共有多少个a标签
length = len(links)
print(length)
print("-"*50)
for link in links:
    url = link.get_attribute('href')

    # print(url)
    driver2.get(url)
    time.sleep(3)
    names = driver2.find_elements_by_xpath("//div/div[1]/div/div[3]/div[1]/h1")
    length_names = len(names)
    name_list = []      # 用来存储题目
    content_list = []   # 用来存储摘要内容
    for name in names:
        if len(name.get_attribute("innerText")) > 20:
            name_list.append(name.get_attribute("innerText"))
            # print(name.get_attribute("innerText"))
            print(name_list)
            contents = driver2.find_elements_by_xpath("//div/div[2]/div[2]/dl/dd[3]")

            for content in contents:
                content_list.append(content)
                print(content.get_attribute("innerText"))
                print('\n')

# 关闭浏览器
driver.close()
driver2.close()
