# 计算1～100000之间所有素数的个数， 要求如下:
# - 编写函数判断一个数字是否为素数，然后统计素数的个数；
# -对比1: 对比使用多进程和不使用多进程两种方法的统计速度。
# -对比2：对比开启4个多进程和开启10个多进程两种方法的速度。
import time
import multiprocessing


def prime(num):
    mark = 1
    if num == 1:
        return False
    else:
        for x in range(2, num // 2 + 1):
            if num % x == 0:
                mark = 0
        if mark == 1:
            return True
        else:
            return False


def threads(num):
    pool = multiprocessing.Pool(num)
    count = 0
    start = time.time()
    for i in range(1, 100000):
        if pool.apply(prime, args=(i,)) is True:
            count += 1
    pool.close()
    pool.join()
    print('质数个数为' + str(count))
    print('运行时间', end='')
    print(time.time() - start)


def no_thread():
    count = 0
    start = time.time()
    for i in range(1, 100000):
        if prime(i):
            count += 1
    print('质数个数为' + str(count))
    print('运行时间', end='')
    print(time.time() - start)


if __name__ == '__main__':
    no_thread()
    threads(4)
    threads(10)
