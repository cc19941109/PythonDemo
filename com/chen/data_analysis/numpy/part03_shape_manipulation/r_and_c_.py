import numpy as np

a = np.r_[1:4, 0, 4]
print(a)

# help(np.r_)


b = np.c_[np.array([1, 2, 3]), np.array([4, 5, 6])]
print(b)

c = np.c_[np.array([1, 2, 3])]
print(c)

d = np.c_[np.array([[1, 2, 3]]), 0, 0, np.array([[4, 5, 6]])]
print(d)
