import numpy as np

a = np.array([1., 2., 2., 5.])
print(a)

print(a ** 3)

print(10*a)
print(np.sin(a))
print(a>2)
print(a.itemsize)
print(a.dtype)


b = np.array([[1,2],[2,3]])
print(b**2)