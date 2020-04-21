# 从键盘输入5个同学的账号和密码,然后将他们的姓名,账号和密码(密码需要加密)保存到一个文件中;
# Tom   admin   XXXXX
# Jack   root   XXXXX
import os
import base64

list = []
newList = []
c = []
a = input()
while a.strip() != "":
    list.append(a)
    a = input()
for i in list:
    x = i.split()
    code = bytes(x[2], 'utf-8')
    ec = base64.b64encode(code)
    c.append(ec)
    st = x[0] + ' ' + x[1] + ' '
    newList.append(st)
path = os.getcwd()
f = open(path + "/exe4/3.txt", "a")
for i in range(len(list)):
    f.write(newList[i])
    f.close()
    f = open(path + "/exe4/3.txt", "ab")
    f.write(c[i])
    f.close()
    f = open(path + "/exe4/3.txt", "a")
    f.write("\n")
