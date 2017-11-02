import numpy as np

x = np.array([(1.5, 2, 3),
              (4, 5, 6)])
print(x)
print(x.shape)
print(x.itemsize)
print(x.size)

c = np.array([[1+1.j, 2-2.3j], [3, 4]], dtype=np.complex128)
print(c)
print(c.dtype)
