# 定义一个函数，函数接收一个数组，并把数组里面的数据从小到大排序
# (冒泡排序,  也可以直接使用相关的函数);
import random


def sort(list):
    print("原数组：", list)
    list.sort()
    print("排序后：", list)


list = []
for i in range(10):
    list.append(random.randint(0, 100))
sort(list)
