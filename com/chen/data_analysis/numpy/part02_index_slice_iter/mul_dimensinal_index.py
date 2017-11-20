import numpy as np


def lin(x, y):
    return 10 * x + y


b = np.fromfunction(lin,(5,4),dtype=int)

print(" -- - - -- - -- - -- ")

print(b[2,3])

print(" - -- - -- - -- - -- ")

print(b[0:3,2])

print(" - -- - -- - -- - -- ")

print(b[:,1])

print(" - -- - -- - -- - -- ")

y = b[1:3,1:3]
print(y)

print(" - -- - -- - -- - -- ")

print(b[-1])
print(b[-2,...])



print(type(y))