import numpy as np

a = np.arange(12.0)

c =a.view()

print(a)
print(" - - -- - - ")
print(c)
print(' - -- - - -')

print(c is a)
print(c.base is a )
print(' - -- - - -')
print(c.flags)
# The array owns the memory it uses or borrows it from another object.

print(' -- - -- - -')
b =a

print(b.flags)
