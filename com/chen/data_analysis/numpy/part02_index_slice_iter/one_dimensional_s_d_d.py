# 一维数组 切片

import numpy as np

a = np.arange(10)

b = a ** 3
print(a)
print(b)
print(a[1:7:2])
for i in a:
    print(i ** 2,end=" ")

print("- - -- - - - ")

a[:6:2] = -10
print(a)

print("- - -- - - - ")
print("- - -- - - - ")
r_a = a[::-1]
print(r_a)
print(a[::-2])

print(a[8])
