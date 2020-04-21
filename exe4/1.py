# 定义一个10个元素的列表，通过列表自带的函数，实现元素在尾部插入和头部插入并记录程序运行的时间；
# 用deque来实现，同样记录程序所耗费的时间；输出这2个时间的差值；
# 提示：列表原生的函数实现头部插入数据：list.insert(0, v)；list.append（2）)
import datetime
from collections import deque


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = datetime.datetime.now()
list1.insert(0, 0)
list1.append(11)
b = datetime.datetime.now()
print(b-a)

list2 = deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
x = datetime.datetime.now()
list2.appendleft(0)
list2.append(11)
y = datetime.datetime.now()
print(y-x)
