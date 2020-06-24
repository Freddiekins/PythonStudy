# 有100个同学的分数：数据请用随机函数生成
# A  利用多线程程序（比如，5个线程，每个线程负责输出20条记录），快速输出这100个同学的信息
# B 利用线程池来实现
import random
import threading

list = []
for i in range(100):
    list.append(random.randint(10, 100))


def output(num):
    global list
    for i in range(num, num+20):
        lock.acquire()
        strs = '第' + str(i+1) + '名学生的成绩：' + str(list[i])
        print(strs)
        lock.release()


if __name__ == '__main__':
    threads = []
    lock = threading.Lock()
    for i in range(5):
        t = threading.Thread(target=output, args=(20*i,))
        threads.append(t)
    for i in threads:
        i.start()
    for i in threads:
        i.join()
