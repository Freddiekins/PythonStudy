from human import human
from dog import dog
import random


class fight(object):

    def __init__(self, human, dog):
        self.human = human
        self.dog = dog

    def fight(self):
        mark = random.randint(0, 1)
        while len(self.human) and len(self.dog):
            if mark == 0:
                d = random.choice(self.dog)
                d.hurt()
                print('%d号狗被攻击,剩余%d生命值' % (d.num, d.hp))
                if d.hp <= 0:
                    print('%d号狗倒地' % d.num)
                    del self.dog[self.dog.index(d)]
                mark = 1
            elif mark == 1:
                h = random.choice(self.human)
                h.hurt()
                print('%d号人被攻击,剩余%d生命值' % (h.num, h.hp))
                if h.hp <= 0:
                    print('%d号人倒地' % h.num)
                    del self.human[self.human.index(h)]
                mark = 0
        if len(self.human):
            print('人胜')
        else:
            print('狗胜')


list1 = []
list2 = []
h1 = human(1)
h2 = human(2)
d1 = dog(1)
d2 = dog(2)
d3 = dog(3)
list1.append(h1)
list1.append(h2)
list2.append(d1)
list2.append(d2)
list2.append(d3)
f = fight(list1, list2)
f.fight()
