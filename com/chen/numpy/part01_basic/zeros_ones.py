import numpy as np

x = np.zeros((3,2))
print(x)

y = np.ones([3,2],dtype=np.int64,order="f")
print(y)

print(x.dtype)
# 默认类型为 float64


# 随机
z = np.empty([3,4])
print(z)

help(np.empty)
print("- - -- - - - -- - - - -")
z1 = np.zeros_like(z)
print(z1)

help(np.zeros_like)

print(x.strides)