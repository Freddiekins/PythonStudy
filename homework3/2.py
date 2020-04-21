# 写一个程序，从input.txt中读取之前输入的数据，存入列表中，再加上行号打印显示；格式如下
import os

path = os.getcwd()
f = open(path + "/homework3/input.txt")
list = f.readlines()
for i in list:
    i = i.strip()
for i in range(len(list)):
    print(i+1, end="")
    print("."+list[i], end="")
