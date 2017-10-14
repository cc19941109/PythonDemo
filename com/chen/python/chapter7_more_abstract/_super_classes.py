class Player:
    name ='cc'
    def play(self):
        print('Player play')

class Calculator(Player):
    def calculate(self,expression):
        print(expression, '=',eval(expression))
    def talk(self):
        print('calculator talk ...')
    def play(self):
        print('Calculator play ..',)

class Talker(Player):
    'test Talker doc....'
    def talk(self):
        print('i can talk.....')
    def play(self):
        print("Talker play...")


class TalkingCalculator(Talker,Calculator,):
    pass


tc = TalkingCalculator()
tc.calculate('1+3')
tc.talk()
tc.play()


print('\n - - - - ','next hasattr test',' - - - - \n')
print(hasattr(tc,'talk'))
print(hasattr(tc,'speak'))

print('\n - - - - ','next getattr test',' - - - - \n')
print(callable(getattr(tc,'talk',None)))
print(callable(getattr(tc,'k',None)))

# print(getattr(tc,'k'))
# AttributeError: 'TalkingCalculator' object has no attribute 'k'

print('\n - - - - ','next __dict__ test',' - - - - \n')

print(Talker.__dict__)

# print(Player.__getattribute__())



