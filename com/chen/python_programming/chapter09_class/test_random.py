from random import randint

def range1():
    for i in range(10):
        x = randint(1, 6)
        print(x,end=' ')

class Die():
    def __init__(self):
        self.sides = 6

    def roll_die(self,sides=6):
        x = randint(1, sides)
        print(x, end=' ')

def test(sides,num):
    x = Die()
    for i in range(num):
        x.roll_die(sides)
    print('\n')

test(20,10)