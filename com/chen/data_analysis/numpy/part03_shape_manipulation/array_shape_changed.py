import  numpy as np

a = np.floor(10*np.random.random((3,4)))
print(a)

print(a.ravel())

x = a.reshape(2,6)
print(x)


y = a.T

print(y)