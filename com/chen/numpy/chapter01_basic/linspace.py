import numpy as np

a = np.ones(3,dtype=np.int32)

b = np.linspace(0,np.pi,3)
print(b)
c = a+b
print(c)

d = np.exp(a*1j)

print(d)
print(d.dtype)

a = np.random.random((2,3))
print(a)
print(a.max())
print(a.min())

help(np.linspace)