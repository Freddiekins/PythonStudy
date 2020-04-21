class human(object):
    hp = 100
    damage = 10

    def __init__(self, num):
        self.num = num

    def hurt(self):
        self.hp -= 15
        if self.hp <= 0:
            self.damage = 0
