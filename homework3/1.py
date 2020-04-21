# 写一个程序，读取键盘输入的任意行文字信息，当输入空行时结束输入，
# 将读入的字符串存于列表;然后将列表里面的内容写入到文件input.txt中；
import os

list = []
a = input()
while a.strip() != "":
    list.append(a)
    a = input()
path = os.getcwd()
f = open(path + "/homework3/input.txt", "w")
for i in list:
    f.write(i+"\n")
