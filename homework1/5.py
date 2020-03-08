# 使用random模块，生成随机数，来初始化一个列表，元组；
# 使用了 random 模块的 randint() 函数来生成随机数，查询一下相关函数的用法；
import random

list = []
for i in range(5):
    list.append(random.randint(0, 10))
print("随机数列表：", end="")
for i in list:
    print(i, end=" ")
print()
tup = (random.randint(0, 10), random.randint(0, 10), random.randint(0, 10),
       random.randint(0, 10), random.randint(0, 10))
print("随机数元组：", end="")
for i in tup:
    print(i, end=" ")
