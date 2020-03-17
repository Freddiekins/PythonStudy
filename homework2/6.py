# 定义一个函数, 打印输出n以内的斐波那契数列;


def nums(n):
    a = 0
    b = 1
    sum = 0
    print(a, b, end=" ")
    while sum < n:
        sum = a + b
        if sum > n:
            break
        print(sum, end=" ")
        a = b
        b = sum


a = int(input("输入一个数字："))
nums(a)
