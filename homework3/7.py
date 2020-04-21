# 在2个文件中存放了英文计算机技术文章(可以选择2篇关于Python技术文件操作处理技巧的2篇英文技术文章),
# 请读取文章内容,进行词频的统计;并分别输出统计结果到另外的文件存放;
# 比较这2篇文章的相似度(如果词频最高的前10个词,重复了5个,相似度就是50%;重复了6个,相似度就是60% ,......);
import os


def getText1():
    path = os.getcwd()
    f = open(path + "/homework3/text.txt")
    text = f.read()
    text = text.lower()
    for i in text:
        if i.isalnum() is False and i.isspace() is False:
            text = text.replace(i, " ")
    return text


def getText2():
    path = os.getcwd()
    f = open(path + "/homework3/text2.txt")
    text = f.read()
    text = text.lower()
    for i in text:
        if i.isalnum() is False and i.isspace() is False:
            text = text.replace(i, " ")
    return text


newL1 = []
newL2 = []
dict1 = {}
t1 = getText1()
words = t1.split()
for i in words:
    if i in dict1:
        dict1[i] = dict1[i] + 1
    else:
        dict1.update({i: 1})
list1 = sorted(dict1.items(), key=lambda x: x[1], reverse=True)

dict2 = {}
t2 = getText2()
words = t2.split()
for i in words:
    if i in dict2:
        dict2[i] = dict2[i] + 1
    else:
        dict2.update({i: 1})
list2 = sorted(dict2.items(), key=lambda x: x[1], reverse=True)

for i in range(10):
    newL1.append(list1[i][0])
    newL2.append(list2[i][0])
c = [x for x in newL1 if x in newL2]
x = len(c)
print("相似度为", x*10, "%")
