import numpy as np

# a = np.random.random((3,4))

a = np.arange(0, 15).reshape((3, 5))
print(a)
print(a.max(axis=1))
print(a.min(axis=0))
print(a.sum(axis=0))
print(a.cumsum(axis=1))


print(a.sum(axis=1))

# help(np.max)
# help(np.cumsum)
