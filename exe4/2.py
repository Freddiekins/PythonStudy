# 定义一个函数，判断一个输入的日期，是当年的第几周，周几？
# 将程序改写一下，能针对我们学校的校历时间进行计算（校历第1周，2月17-2月23；校历第27周，8月17-8月23；）
import datetime


def date():
    list = input().split()
    a = int(list[0])
    b = int(list[1])
    c = int(list[2])
    dt = datetime.datetime(a, b, c)
    list2 = dt.isocalendar()
    Str = str(list2[0])+'年'+'第'+str(list2[1])+'周的'+'周'+str(list2[2])
    print(Str)


def sclDate():
    list = input().split()
    a = 2020
    b = int(list[0])
    c = int(list[1])
    dt2 = datetime.datetime(a, b, c)
    dt1 = datetime.datetime(a, 2, 17)
    w = int((dt2-dt1).days / 7) + 1
    str2 = '校历第' + str(w) + '周'
    print(str2)


date()
sclDate()
