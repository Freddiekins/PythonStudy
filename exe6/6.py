# 用面向对象,实现一个学生Python成绩管理系统;
# 学生的信息存储在文件中;学生信息的字段有(班级,学号,姓名, Python成绩)
# 实现对学生信息及成绩的增,删,改,查方法;
import os


class student(object):
    def read(self):
        info = []
        path = os.getcwd()
        f = open(path + '/exe6/info.txt')
        list = f.readlines()
        for i in list:
            info.append(i.split())
        print(info)
        f.close()

    def insert(self, cla, num, name, score):
        path = os.getcwd()
        f = open(path + '/exe6/info.txt', 'a+')
        strs = cla + ' ' + num + ' ' + name + ' ' + score + '\n'
        f.write(strs)
        f.close()

    def delete(self, num):
        path = os.getcwd()
        f = open(path + '/exe6/info.txt')
        list = f.readlines()
        f = open(path + '/exe6/info.txt', 'w+')
        for i in range(len(list)):
            li = list[i].split()
            if num == li[1]:
                del list[i]
                break
        f.writelines(list)
        f.close()

    def search(self, num):
        path = os.getcwd()
        f = open(path + '/exe6/info.txt')
        list = f.readlines()
        for i in range(len(list)):
            li = list[i].split()
            if num == li[1]:
                print(li)
        f.close()

    def update(self, num, score):
        path = os.getcwd()
        f = open(path + '/exe6/info.txt')
        list = f.readlines()
        f = open(path + '/exe6/info.txt', 'w+')
        for i in range(len(list)):
            li = list[i].split()
            if num == li[1]:
                strs = li[0] + ' ' + li[1] + ' ' + li[2] + ' ' + score + '\n'
                del list[i]
                list.append(strs)
                break
        f.writelines(list)
        f.close()


s = student()
s.read()
s.insert('1802', '07', 'f', '79')
s.delete('02')
s.search('03')
s.update('04', '99')
