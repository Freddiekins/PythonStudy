# 给定100个企业网站首页链接地址（用1中给出的URL地址）；请爬取每个页面上，企业介绍的链接地址；
# 说明，满足企业介绍网址的条件是， 标题包含：企业介绍，关于我们，企业发展，发展历史，企业概况等关键字的URL地址；
# 提示：要用到requests库，BeautifulSoup库
from bs4 import BeautifulSoup
import os
import urllib.request

path = os.getcwd()
f = open(path + '/exe7/1.txt')
list = f.readlines()
li = []
for i in range(100):
    url = list[i].strip()
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    xp = soup.find_all('a')
    for x in xp:
        if '企业介绍' in x or '关于我们' in x or '企业发展' in x or '发展历史' in x or '企业概况' in x:
            xx = x.get('href')
            if 'www' not in xx:
                urls = url + '/' + xx
            else:
                urls = xx
            if urls not in li:
                li.append(urls)
    for u in li:
        print(u)
    li.clear()
