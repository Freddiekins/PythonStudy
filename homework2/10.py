# 编写一个函数cacluate, 可以实现2个数的运算(加,减 乘,除)


def cacluate():
    print("请输入两个数：")
    list = input().split()
    x = int(list[0])
    y = int(list[1])
    a = int(input("输入1加法运算，输入2减法运算，输入3乘法运算，输入4乘法运算\n"))
    if a == 1:
        print(list[0], "+", list[1], "=", x+y)
    elif a == 2:
        print(list[0], "-", list[1], "=", x-y)
    elif a == 3:
        print(list[0], "*", list[1], "=", x*y)
    else:
        print(list[0], "/", list[1], "=", x/y)


cacluate()
