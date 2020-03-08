# 定义2个列表，并初始化；
# 找出这2个列表中，相同的元素并输出；
list1 = [1, 3, 96, 7, 4, 5, 16]
list2 = [7, 5, 9, 18, 2, 96, 8]
print("相同的值：", end="")
for i in list1:
    for j in list2:
        if i == j:
            print(i, end=" ")
