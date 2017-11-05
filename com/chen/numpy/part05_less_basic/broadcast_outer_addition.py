import numpy as np

a= np.array([0.,1.,2.,3.])
b= np.array([0.,10.,20.,30.])

print(a,a.shape)
x = a[:,np.newaxis]
print(x,x.shape)

x1 = a[:np.newaxis]+b
print(x1)


x2 = a[:,np.newaxis]+b
print(x2)
