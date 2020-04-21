# 封装一个学生类，有姓名，有年龄，有性别，有英语成绩，数学成绩，语文成绩,
# 封装方法，求单个学生的总分，平均分，以及打印学生的信息。


class student(object):

    def __init__(self):
        self.__name = 'Tom'
        self.__age = 20
        self.__gender = 'male'
        self.__english = 85
        self.__math = 77
        self.__chinese = 81

    def __info(self):
        sum = self.__math + self.__english + self.__chinese
        print('总分为%d' % sum)
        print('平均分为%.2f' % (sum/3))
        print('姓名：%s, 年龄：%d, 性别：%s' % (self.__name, self.__age, self.__gender))
        print('英语：%d, 数学：%d, 语文：%d' % (self.__math, self.__english, self.__chinese))

    def output(self):
        self.__info()


s = student()
s.output()
