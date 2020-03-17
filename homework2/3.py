# 编写一个函数, 传入一个数字列表, 输出列表中的奇数;
# 数字列表请用随机数函数生成;
import random


def odd(list):
    print("列表中所有的数有：", end="")
    for i in list:
        print(i, end=" ")
    print()
    print("列表中的奇数有：", end="")
    for i in list:
        if i % 2 != 0:
            print(i, end=" ")


list = []
for i in range(10):
    list.append(random.randint(0, 100))
odd(list)
