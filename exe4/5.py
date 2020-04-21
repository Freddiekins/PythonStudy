# 通过Python来模拟实现一个txt文件的拷贝过程;
import os

path = os.getcwd()
f = open(path + "/exe4/4.txt")
list = f.readlines()
f.close()
f = open(path + "/exe4/5.txt", "w")
f.writelines(list)
