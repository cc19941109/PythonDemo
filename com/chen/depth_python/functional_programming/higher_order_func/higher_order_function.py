func = lambda x:abs(x)

def add(x,y,z):
    return z(x)+z(y)

x = 1
y =-2

result = add(x,y,func)
print(result)
