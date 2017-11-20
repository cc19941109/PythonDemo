import numpy as np

a = np.arange(12).reshape(3,4)

d = a.copy()
print(a)
print(' -- - - -- - ')
print(d)

print( '  -- - -- - - -')

d[1,2] = 11111
print(a)
print(' -- - - -- - ')
print(d)

print(d.base is a)


