# 从网络上下载一张图片，保存到计算机的指定目录；（requests和os模块）
import requests
import os

html = requests.get('https://p1.ssl.qhimg.com/t010d78ce148a22c3b2.jpg')
path = os.getcwd()
f = open(path + '/exe4/file.jpg', 'wb')
f.write(html.content)
