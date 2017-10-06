
def square(x):
    x = 19
    return  x*x

s2 = square

x = 10
print(s2(x))
print("x = {0}".format(x))

def change(x):
    x[0] = 'hello world'


x= [1,23,4]

change(x)

print(x)
