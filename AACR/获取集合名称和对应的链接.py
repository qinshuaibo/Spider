# -*- coding: utf-8 -*-
# @Time    : 2020/7/14 18:55
# @Author  : qinshuaibo
import requests
from bs4 import BeautifulSoup
from browsermobproxy import Server
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import csv
import codecs
#实例化Options对象
chrome_options = Options()
#把Chrome浏览器设置为静默模式
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)
driver2 = webdriver.Chrome()
driver.get('https://www.aacr.org/meeting/aacr-annual-meeting-2020/aacr-virtual-annual-meeting-i/')
time.sleep(5)
#获取完整渲染的网页源代码
pageSource = driver.page_source
#打印pageSource的类型
print(type(pageSource))
#打印pageSource
# print(pageSource)
#集合名称
# titles = driver.find_elements_by_xpath("//div[@class='title']")
# titles = driver.find_elements_by_xpath("//body/div[7]/div[2]/div/ul[1]/li/a")
titles = driver.find_elements_by_xpath("//div[@class='first-section section clearfix']/ul/li/a")


titles_shuliang = len(titles)
print(titles_shuliang)
for title in titles:
    print(title.text)

# //*[@id="app"]/div[2]/div/div/div[2]/div[3]/div/ul/li[2]/a
# //*[@id="app"]/div[2]/div/div/div[2]/div[3]
#超链接
#获取所有a标签
links = driver.find_elements_by_xpath("//div[@class='first-section section clearfix']/ul/li/a")

for link in links:
    url = link.get_attribute('href')
    print(url)
    # driver2.get(url)
    # content = driver2.find_element_by_xpath("//div[2]/div/dl[1]/dd/span")
#列表长度，一共有多少个a标签
length = len(links)
print(length)

#写入CSV文件
# f = open('aaa.csv','w',encoding='utf-8')
# csv_writer=csv.writerow(f)
# csv_writer.writerow(["项目名", "链接"]
# def data_write_csv("D"\a.csv", datas):  # file_name为写入CSV文件的路径，datas为要写入数据列表
#     file_csv = codecs.open(file_name, 'w+', 'utf-8')  # 追加
#     writer = csv.writer(file_csv, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
#     for data in datas:
#         writer.writerow(data)
#     print("保存文件成功，处理结束")
"""
#遍历列表循环，使程序可以逐一点击
for i in range(0, length):
    #每次循环内部都重新获取a标签
    links = driver.find_elements_by_xpath("//div[2]/div/div/div[2]/div[3]/div/ul/li/a")
    #把列表中的a标签赋给link
    link = links[i]
    #提取a标签中的链接，这里提取到的链接是文本无法点击
    url = link.get_attribute('href')
    #在这不能使用click，因为没用，直接用浏览器打开
    driver.get(url)
    #留出加载时间
    time.sleep(1)
    #用text的意思是输出纯文本
    genes = driver.find_element_by_xpath("//div[@class='title']").text

    content = driver.find_element_by_xpath("//span[@class='color-wegene-blue font-weight-bold']")
    print (url.get_attribute("href"))
"""

#关闭浏览器
driver.close()