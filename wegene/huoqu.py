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

driver = webdriver.Chrome(options = chrome_options)
driver2 = webdriver.Chrome()
driver.get('https://www.wegene.com/demo2/male/report/%E5%81%A5%E5%BA%B7%E9%A3%8E%E9%99%A9')  # 遗传性疾病
# driver.get('https://www.wegene.com/demo2/male/report/%E8%BF%90%E5%8A%A8%E5%9F%BA%E5%9B%A0')#运动基因

time.sleep(5)
# 获取完整渲染的网页源代码
pageSource = driver.page_source
# 打印pageSource的类型
print(type(pageSource))
# 打印pageSource
# print(pageSource)
# 疾病名称
"""
titles = driver.find_elements_by_xpath("//div[@class='title']")
titles_shuliang = len(titles)
for u in titles:
    print(u.text)
"""
# print(titles_shuliang)
# //*[@id="app"]/div[2]/div/div/div[2]/div[3]/div/ul/li[2]/a
# //*[@id="app"]/div[2]/div/div/div[2]/div[3]
# 超链接
# 获取所有a标签
links = driver.find_elements_by_xpath("//div[2]/div/div/div[2]/div[3]/div/ul/li/a")
# links = driver.find_elements_by_xpath("//div[@class='mod list padding-left-50 padding-right-50 padding-bottom-20 border-top-none']")
# 列表长度，一共有多少个a标签
length = len(links)
print('项目链接数量:', length)
for link in links:
    url = link.get_attribute('href')
    # print(url, ';', end='')
    print(url, ',', end = '')
    driver2.get(url)
    time.sleep(5)
    # 获取完整渲染的网页源代码
    # pageSource = driver2.page_source
    # 打印pageSource的类型
    # print(type(pageSource))
    # 打印pageSource
    # print(pageSource)
    # 检测的项目
    names = driver2.find_elements_by_xpath("//div[1]/div/div/div/div/h2")
    for name in names:
        # print(name.text, ';', end='')
        print(name.text, ',', end = '')

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
    length = len(locals)
    print('位点数量：', length, ',', end = '')
    for local in locals:
        print(local.text, ',', end = '')
        # print(local.text, ';', end='')
    # print(';', end='')
    local_types = driver2.find_elements_by_xpath("//div[@class='toggle']/ol/li[1]/b")
    # //*[@id="10485"]/div[2]/div[2]/div/div[2]/div/ul/li[1]/div[2]/ol/li[1]/b
    length = len(local_types)
    print('基因型数量:', length, ',', end = '')
    for Type in local_types:
        print(Type.get_attribute("innerText"), ',', end = '')
    # print(';')
    # print(',')
    print('\n')
    # 把爬取到的数据写入csv文件
    # with open('wegene.csv','w',newline='') as file:
    #     writer = csv.writer(file)
    #     writer.writerow(data.keys())

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
    time.sleep(5)
    genes = driver2.find_elements_by_xpath("//div[2]/div/dl[1]/dd/span")
    for gene in genes:
        print(gene.text)
    # 位点
    locals = driver2.find_elements_by_xpath("//div[2]/div[2]/div/div[2]/div/ul/li/div/div")
    # //*[@id="10485"]/div[2]/div[2]/div/div[2]/div/ul/li[1]/div[1]/div[1]
    for local in locals:
        print(local.text)
    #用text的意思是输出纯文本
    # genes = driver.find_element_by_xpath("//div[@class='title']").text

    # content = driver.find_element_by_xpath("//span[@class='color-wegene-blue font-weight-bold']")
    # print (url.get_attribute("href"))
"""
# 关闭浏览器
driver.close()
driver2.close()
