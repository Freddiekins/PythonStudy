# 定义一个狗类,里面有一个 列表成员变量(列表的元素是字典),
# 分别记录了 3种颜色的狗的颜色, 数量,和价格;
# 实现狗的买卖交易方法;  打印输出经过2-3次买卖方法后,剩下的各类狗的数量;


class dog(object):
    list = []
    list.append({'black': [5, 200], 'yellow': [7, 300], 'white': [9, 400]})

    def trade(self):
        print(self.list)
        a = input('输入要购买的颜色和数量').split()
        self.list[0][a[0]][0] -= int(a[1])
        b = input('输入要购买的颜色和数量').split()
        self.list[0][b[0]][0] -= int(b[1])
        print(self.list)


d = dog()
d.trade()
