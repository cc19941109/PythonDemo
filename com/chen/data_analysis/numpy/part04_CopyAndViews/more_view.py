import numpy as np

a = np.arange(12)
a.shape = 3,4
c = a.view()

print(c.shape)

c.shape = 2,6

print(c)
print(c.shape)

print('- - - -- - ')

print(a)
print(a.shape)

print('- - - -- - ')

a[0,1] = 123
print(c)
print('- - - -- - ')

print(a)

print('- - - -- - ')
