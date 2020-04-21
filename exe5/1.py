# 编写一个装饰器，能计算其他函数的运行时间
import random
import time


def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("运行时间为%s" % (end - start))
    return wrapper


@timer
def sec():
    time.sleep(random.randrange(1, 3))
    print('This is sec')


sec()
