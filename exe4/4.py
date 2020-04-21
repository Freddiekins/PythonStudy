# (继续上面的练习)模拟用户登录:5个同学的姓名,账号和密码(加密后的),保存在一个文件上;
# 系统提示,请输入登录同学姓名, 正确后,请输入账号, 正确后,提示请输入密码（输入明文）;
# 如果都正确,打印提示, 您登录成功(失败);
import os
import base64

path = os.getcwd()
f = open(path + "/exe4/4.txt")
list = f.readlines()
li = []
mark = 0
newList = []
for i in list:
    i = i.strip()
    li = i.split()
    newList.append(li)
a = input("输入姓名：")
for i in newList:
    if a == i[0]:
        mark = 1
        b = input("输入账号：")
        if b == i[1]:
            c = input("输入密码：")
            m = bytes(map(ord, i[2]))
            de = base64.b64decode(m).decode('utf-8')
            if c == de:
                print('密码正确')
            else:
                print('密码错误')
        else:
            print("账号错误")
if mark == 0:
    print("姓名错误")
