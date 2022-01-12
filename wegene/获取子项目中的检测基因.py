# -*- coding: utf-8 -*-
# @Time    : 2020/6/19 13:13
# @Author  : qinshuaibo
"""先试一下对其中一个子链接进行访问，看看能不能得到检测基因和位点信息"""
import requests
from bs4 import BeautifulSoup
from browsermobproxy import Server
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import time
import csv

# 实例化Options对象
chrome_options = Options()
# 把Chrome浏览器设置为静默模式
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(options = chrome_options)
driver2 = webdriver.Chrome()
driver2.get('https://www.wegene.com/demo2/male/detail/66')
# driver.get('https://www.wegene.com/demo2/male/report/%E5%81%A5%E5%BA%B7%E9%A3%8E%E9%99%A9')
time.sleep(3)
# 获取完整渲染的网页源代码
pageSource = driver2.page_source
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
print(titles_shuliang)
"""
# //*[@id="app"]/div[2]/div/div/div[2]/div[3]/div/ul/li[2]/a
# //*[@id="app"]/div[2]/div/div/div[2]/div[3]
# 超链接
# 获取所有a标签,在这个里面其实没用，
# links = driver.find_elements_by_xpath("//div[2]/div/div/div[2]/div[3]/div/ul/li/a")
# 列表长度，一共有多少个链接
# length = len(links)
# print(length)
"""
for link in links:
    url = link.get_attribute('href')
    print(url)
    driver2.get(url)
    content = driver2.find_element_by_xpath("//div[2]/div/dl[1]/dd/span")
"""
# //*[@id="app"]/div[1]/div/div/div/div/h2
# 检测的项目名
# names = driver2.find_elements_by_xpath("//div[@class='col-md-12']/h2")
names = driver2.find_elements_by_xpath("//div[1]/div/div/div/div/h2")
for name in names:
    print(name.text)

# 检测的基因
genes = driver2.find_elements_by_xpath("//div[2]/div/dl/dd/span")
# genes = driver.find_elements_by_xpath("//span[@class='color-wegene-blue font-weight-bold']/span")
length = len(genes)
print('检测基因数量: ', length)
for gene in genes:
    print(gene.text)
# 位点
# locals = driver2.find_elements_by_xpath("//div[2]/div[2]/div/div[2]/div/ul/li//div/div")
locals = driver2.find_elements_by_xpath("//div[@class='gene-position']")
# //*[@id="10485"]/div[2]/div[2]/div/div[2]/div/ul/li[1]/div[1]/div[1]
length = len(locals)
print('位点数量： ', length)
for local in locals:
    print(local.text)
# types = driver2.find_elements_by_xpath("//div[2]/div[2]/div/div[2]/div/ul/li[1]/div[2]/ol/li/b")
# 基因位点的所属基因型
# types = driver2.find_elements_by_xpath("//div[2]/div[2]/div/div[2]/div/ul/li/div/ol/li/b")
# //*[@id="10485"]/div[2]/div[2]/div/div[2]/div/ul/li[1]/div[2]/ol/li[1]/blo
""""这属于点击的问题,可以通过js修改display属性为black"""

# local_types = driver2.find_elements_by_xpath("//div[@class='toggle',style="display:none;"]/ol/li[1]/b")
js = "document.getElementsByClassName('toggle')[1].style.display='block';"
driver2.execute_script(js)
time.sleep(3)

local_types = driver2.find_elements_by_xpath("//div[@class='toggle']/ol/li[1]/b")

length = len(local_types)
print('位点基因型', length)
for Type in local_types:
    print(Type.text)


# 写入CSV文件中
# with open('wegene.txt', mode='w', encoding='utf-8') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow(['项目名','检测的基因','位点'])
#     for data in datalist:
def __init__(self):
    file = open('data/wegene.csv', 'w', newline = '')
    self.writer = csv.writer(file)
    self.writer.writerow(['项目名', '检测的基因', '位点详情'])


# 关闭浏览器
driver.close()
