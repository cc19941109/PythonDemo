import numpy as np

a = np.ones((2,3), dtype=int)
print(a)
a*=3
print(a)

b = np.random.random((2,3))
print(b)

b+=a
print(b)

a +=b
print(a)