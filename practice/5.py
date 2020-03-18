# 一个文件内容的如下,请按照行读取文件的内容,  将分数排序后输出;
f = open("read.txt", encoding='utf-8')
data = f.readlines()
f.close()
list1 = data[1].split()
list2 = data[2].split()
list3 = data[3].split()
list = [list1, list2, list3]
list.sort(key=lambda score: score[2])
print("姓名    学号    成绩")
for i in list:
    str = i[0]+"    "+i[1]+"    "+i[2]
    print(str)
