# 编写一个程序，读取文件中保存的10个学生成绩名单信息(学号,姓名, Python课程分数); 然后按照分数从高到低进行排序输出
import os

path = os.getcwd()
f = open(path + "/homework3/score.txt", encoding='utf-8')
data = f.readlines()
f.close()
list = []
for i in range(len(data)):
    li = data[i].split()
    list.append(li)
list.sort(key=lambda score: score[2], reverse=True)
print("姓名    学号    成绩")
for i in list:
    str = i[0]+"    "+i[1]+"    "+i[2]
    print(str)
