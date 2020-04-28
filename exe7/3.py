import requests
import re
import wget
import os
from urllib.parse import quote

res = requests.get('http://www.listeningexpress.com/studioclassroom/ad/')
result = re.findall(r"20\d\d-\d\d-\d\d[\w\s'\\]*\.mp3", res.text)
url = 'http://www.listeningexpress.com/studioclassroom/ad/'
path = os.getcwd() + '/exe7/mp3files'
for r in result:
    downloadpath = url + quote(r)
    print(downloadpath)
    wget.download(downloadpath, out=r)
