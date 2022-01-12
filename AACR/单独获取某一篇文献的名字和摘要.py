# -*- coding: utf-8 -*-
# @Time    : 2020/7/15 8:33
# @Author  : qinshuaibo 这是动态网页
import requests
from bs4 import BeautifulSoup
from browsermobproxy import Server
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import csv
import codecs
# 实例化Options对象
chrome_options = Options()
# 把Chrome浏览器设置为静默模式
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)
driver2 = webdriver.Chrome()
driver.get('https://www.abstractsonline.com/pp8/#!/9045/presentation/10679')
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
titles = driver.find_element_by_xpath("//div/div[2]/div[2]/dl/dd[2]")
print(titles.text)

# titles_shuliang = len(titles)
# print(titles_shuliang)
# for u in titles:
#     print(u.text)

# //*[@id="app"]/div[2]/div/div/div[2]/div[3]/div/ul/li[2]/a
# //*[@id="app"]/div[2]/div/div/div[2]/div[3]
# 超链接
# 获取所有a标签
links = driver.find_elements_by_xpath("//div/div[2]/div[2]/table/tbody/tr/td[2]/a")
# 列表长度，一共有多少个a标签
length = len(links)
print(length)

for link in links:
    url = link.get_attribute('href')
    print(url)
    driver2.get(url)
    contents = driver2.find_element_by_xpath("//div/div[2]/div[2]/dl/dd[2]")
    print(contents.text)
    # for content in contents:
    #     print(content.text)

# 关闭浏览器
driver.close()
driver2.close()