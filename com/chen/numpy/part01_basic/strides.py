import numpy as np

x = np.array([[0, 1, 2, 3, 4],
              [5, 6, 7, 8, 9]], dtype=np.int32)

print(x.strides)

y = np.array([[0, 1, 2, 3, 4, 5],
              [5, 6, 7, 8, 9, 10]], dtype=np.int32)
print(y.strides)
