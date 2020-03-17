# 随机生成20个学生的成绩; 判断这20个学生成绩的等级; 用函数来实现;
# A---成绩>=90;
# B-->成绩在 [80,90)
# C-->成绩在 [70,80)
# D-->成绩<70
import random


def score(list):
    level = []
    print("学生成绩：", list)
    for i in list:
        if i >= 90:
            level.append('A')
        elif i >= 80 and i < 90:
            level.append('B')
        elif i >= 70 and i < 80:
            level.append('C')
        else:
            level.append('D')
    print("成绩等级：", level)


list = []
for i in range(20):
    list.append(random.randint(10, 100))
score(list)
