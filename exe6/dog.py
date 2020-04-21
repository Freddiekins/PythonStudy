class dog(object):
    num = 0
    hp = 80
    damage = 15

    def __init__(self, num):
        self.num = num

    def hurt(self):
        self.hp -= 10
        if self.hp <= 0:
            self.damage = 0
