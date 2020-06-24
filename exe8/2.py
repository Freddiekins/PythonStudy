# 给定一组数据网址数据，请判断这些网址是否可以访问； 用多线程的方式来实现；
# 请查资料，Python的 requests库，如何判断一个网址可以访问；
import requests
import os


def getHtmlText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except BaseException:
        return "产生异常"


path = os.getcwd() + '/exe8/url_data.txt'
f = open(path)
list = []
for i in f.readlines():
    if ";" in i:
        li = i.split(';')
        for url in li:
            url = url.strip()
            list.append(url)
    else:
        list.append(i.strip())
for i in range(10, 20):    # 判断一部分网址，可更改
    if getHtmlText(list[i]) != '产生异常':
        print(list[i] + '    ' + '可以访问')
    else:
        print(list[i] + '    ' + '产生异常')
