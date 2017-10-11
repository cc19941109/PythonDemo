def foo():
    def bar():
        print('hello world')
    bar()

foo()

def mul(factor):
    x = 1
    def mulByfFactor(number):
        nonlocal x
        x +=1
        return number*factor+x
    return mulByfFactor

func = mul(10)
print(func(2))