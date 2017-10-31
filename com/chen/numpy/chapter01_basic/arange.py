import numpy as np

x = np.arange(0, 150, 2,dtype=np.float64)

help(np.arange)
print(x)

y = x.reshape(15,5)
print(y)

z= np.arange(10000).reshape(100,100)

# 禁用自动省略
# np.set_printoptions(threshold=np.nan)
print(z)
