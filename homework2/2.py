# 编写一个函数,接收n个数字，求这些参数数字的和;
def sum():
    n = 0
    list = input().split()
    for i in list:
        n = n + int(i)
    print(n)


sum()
