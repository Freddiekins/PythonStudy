# 生成一个大文件ip.txt,要求1200行，每行随机为172.25.254.1---172.25.254.254之间的ip地址;
# 读取ip.txt文件统计这个文件中ip出现频率排前10的ip
import random
import os


def crtIp():
    list = []
    for i in range(1200):
        x = random.randint(1, 254)
        ipstr = '172.25.254.' + str(x) + '\n'
        list.append(ipstr)
    path = os.getcwd()
    f = open(path + '/exe4/ip.txt', "w+")
    f.writelines(list)
    f.close()


crtIp()
path = os.getcwd()
f = open(path + '/exe4/ip.txt')
li = f.readlines()
ipdict = dict()
for i in li:
    i = i.strip()
    if i in ipdict:
        ipdict[i] += 1
    else:
        ipdict[i] = 1
sorted_ip = sorted(ipdict.items(), key=lambda x: x[1], reverse=True)[:10]
print(sorted_ip)
