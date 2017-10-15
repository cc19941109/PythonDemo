class MuffledCalculator:
    muffled = True
    def calc(self, expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print('division by zero is illegal')
            else:
                raise

calculator = MuffledCalculator()
x = calculator.calc('1/0')
print(x)
