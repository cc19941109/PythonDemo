import numpy as np

x = np.arange(9.0)
print(x)
y = np.split(x,3)
print(type(y))
for key in y :
    print(key)
    print(" -- - - -")

