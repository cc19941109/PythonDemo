import numpy as np

a = np.arange(12)

b = a
print(b is a)

b.shape = 3,4
print(b.shape)
print(a.shape)

def f(x):
    print(id(a))

print(id(a))
f(a)
c = a.view()

print(c)
print(c is a )