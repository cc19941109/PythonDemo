
def add(x,y):
    return x+y

params = (1,2)

result = add(*params)
print(result)


def hello(greeting,name):
    print(greeting,",",name)


p = {'name':"cc",'greeting':'hello'}
hello(**p)