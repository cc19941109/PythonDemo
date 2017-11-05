import numpy as np

x = np.arange(4)
xx = x.reshape(4,1)
y = np.ones(5)
print(y)
z = np.ones((3,4))

print(x.shape)
print(y.shape)

print(xx.shape)
print(y.shape)
print((xx+y).shape)

print('------ -- - -- - - -- - ')
print(xx)
print(" - -- -  ")
print(xx+y)
print(x+z)
print(z+x)