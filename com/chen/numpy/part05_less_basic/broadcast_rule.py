import numpy as np

a = np.array([1., 2., 3.])
b = np.array([[4., 5., 6.],[1.,2.,3.]])
print(a * b)

c = 3

print(b * c)

# The code in the second example is more efficient than that
#  in the first because broadcasting moves less memory around during
# the multiplication (b is a scalar rather than an array).
