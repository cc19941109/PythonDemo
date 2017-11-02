import numpy as np

a = np.arange(15).reshape(3, 5)

print(a)

print(a.shape)
print(a.ndim)
print(a.dtype.name)
print(a.itemsize)
print(a.size)
x = type(a)
print(x)
y = type(x)
print(y)
print(type(y))

print("-  -- - - - - - - -- - -")
a = np.array([[6, 7, 8],
              [1, 2, 3]])

print(a.shape)
print(a.ndim)
print(a.dtype)
print(a.itemsize)
print(a.size)
x = type(a)
print(x)
