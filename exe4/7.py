# 使用python代码统计一个文件夹中所有文件的总大小
import os
sum = 0


def fun(path):
    global sum
    files = os.listdir(path)
    for i in files:
        if os.path.isfile(path + '/' + i):
            sum += os.path.getsize(path + '/' + i)
        else:
            fun(path + '/' + i)


pa = os.getcwd()
fun(pa)
print(sum)
