import numpy as np

a = np.array([[1,2],
             [3,4]])

b = np.array([[0,1],
             [2,0]])

print(a*b)
x = np.dot(a,b)
print(x)
print(type(x))
print(a.dtype)
print(type(a))
# numpy.ndarray