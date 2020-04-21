# 对一篇英文文章，进行词频统计，输出前10个出现频率最高的单词；
import os


def getText():
    path = os.getcwd()
    f = open(path + "/homework3/text.txt")
    text = f.read()
    text = text.lower()
    for i in text:
        if i.isalnum() is False and i.isspace() is False:
            text = text.replace(i, " ")
    return text


dict = {}
t = getText()
words = t.split()
for i in words:
    if i in dict:
        dict[i] = dict[i] + 1
    else:
        dict.update({i: 1})
list = sorted(dict.items(), key=lambda x: x[1], reverse=True)
print(list)
for i in range(10):
    print(list[i])
