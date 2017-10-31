import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int64, order='c')
print(a.strides)

b = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int64, order='f')
print(b.strides)

c = np.array([[1, 2, 3,4], [4, 5, 6,7]], dtype=np.int64, order='f')
print(c.strides)



