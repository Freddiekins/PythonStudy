# 通过Python来实现显示给定文件夹下的所有文件和文件夹,以及时间，如果是文件，显示大小
import os
import datetime

path = os.getcwd()
files = os.listdir(path)
for i in files:
    print(i, end='')
    for x in range(20-len(i)):
        print(' ', end='')
    date1 = os.path.getmtime(path + '/' + i)
    date2 = datetime.datetime.fromtimestamp(date1)
    date3 = date2.strftime('%Y/%b/%d %H:%M')
    print(date3, end='')
    if os.path.isfile(path + '/' + i):
        m = os.path.getsize(path + '/' + i)
        print("    ", m, "字节")
    else:
        print()
