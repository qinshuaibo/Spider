# -*- coding: utf-8 -*-
# @Time    : 2020/7/14 20:33
# @Author  : qinshuaibo
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
driver3 = webdriver.Chrome()
driver.get('https://www.aacr.org/meeting/aacr-annual-meeting-2020/aacr-virtual-annual-meeting-i/')
time.sleep(5)
# 获取完整渲染的网页源代码
pageSource = driver.page_source
# 打印pageSource的类型
print(type(pageSource))
# 打印pageSource
# print(pageSource)

# 集合名称
titles = driver.find_elements_by_xpath("//div[@class='first-section section clearfix']/ul/li/a")
titles_shuliang = len(titles)
print(titles_shuliang)


# 获取所有集合链接
all_links = driver.find_elements_by_xpath("//div[@class='first-section section clearfix']/ul/li/a")
# 列表长度，一共有多少个a标签
length = len(all_links)
print('集合链接数量:', length)
for all_link in all_links:
    all_link = all_link.get_attribute('href')
    # 集合名称
    # titles = driver.find_elements_by_xpath("//div[@class='first-section section clearfix']/ul/li/a")
    # for title in titles:
    #     print(title.text)
    print(all_link)
    driver2.get(all_link)
    time.sleep(10)
# 开始循环，在集合的链接中获取子链接
    # urls = links.get_attribute('href')
    links = driver2.find_elements_by_xpath("//div/div[2]/div[2]/table/tbody/tr/td[2]/a")

    # 列表长度，一共有多少个a标签
    length = len(links)
    print('该集合中包含的链接数量:',length)
    # urls = links.get_attribute('href')
    for url in links:
        url = url.get_attribute('href')
        driver3.get(url)
        time.sleep(15)
        # 获取集合中论文名字
        names = driver3.find_elements_by_xpath("//div/div[1]/div/div[3]/div[1]/h1")
        length_names = len(names)
        # 对名字进行筛选，因为有的不需要
        name_list = []
        for name in names:
            if len(name.get_attribute("innerText")) > 20:
                name_list.append(name.get_attribute("innerText"))
                print(name.get_attribute("innerText"))
                contents = driver3.find_elements_by_xpath("//div/div[2]/div[2]/dl/dd[3]")

                for content in contents:
                    print(content.get_attribute("innerText"))
        print(len(name_list))
        print('\n')

# 关闭浏览器
driver.close()
driver2.close()
driver3.close()