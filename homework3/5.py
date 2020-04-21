# 文件综合编程题目
import os

path = os.getcwd()
f = open(path + "/homework3/blowing in the wind.txt")
data = f.readlines()
f.close()
data.insert(0, "Blowin' in the wind    Bob Dylan\n\n")
data.append("1962 by Warner Bros.Inc.")
f = open(path + "/homework3/blowing in the wind.txt", "w")
f.writelines(data)
for i in data:
    print(i, end="")
