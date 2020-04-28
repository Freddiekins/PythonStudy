# 给定一个文件，请用正则表达式，逐行匹配提取其中的URL链接信息，并保存到另外一个文件中；
import re
import os

path = os.getcwd()
f = open(path + '/exe7/webspiderUrl.txt', encoding='utf-8')
list = f.readlines()
f.close()
f = open(path + '/exe7/1.txt', 'w')
for i in list:
    i = i.strip()
    ret = re.search(r"http.*\.\w*", i)
    if ret:
        li = ret.group().split(';')
        for x in li:
            x = x.strip()
            url = x + '\n'
            f.write(url)
f.close()
