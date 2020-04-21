# 编写装饰器来实现，对目标函数进行装饰，分3种情况：
# 目标函数无参数无返回值，目标函数有参数，目标函数有返回值；
# 三个目标函数分别为：
# A 打印输出20000之内的素数；
# B 计算整数2-10000之间的素数的个数；
# C 计算整数2-M之间的素数的个数；
# 可以观看给的视频材料，仿照示例来做；


def outer(num):
    def inner(func):
        def wrapper(*args, **kwargs):
            if num == 1:
                print('打印输出200之内的素数')
                func()
            elif num == 2:
                print('计算整数2-10000之间的素数的个数')
                res = func()
                return res
            elif num == 3:
                print('计算整数2-M之间的素数的个数')
                return func(*args, **kwargs)
        return wrapper
    return inner


@outer(1)
def func1():
    for num in range(201):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num, end=' ')
    print()


@outer(2)
def func2():
    count = 0
    for num in range(2, 10001):
        if num == 2:
            count += 1
        else:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                count += 1
    return count


@outer(3)
def func3(m):
    count = 0
    for num in range(2, m+1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                count += 1
    print(count)


func1()
print(func2())
func3(5000)
