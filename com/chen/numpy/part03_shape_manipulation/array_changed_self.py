import numpy as np

a = np.floor(10*np.random.random((3,4)))

print(a)

x = a.resize((6,1))

print("\n - -- - -- - - \n")
print(x)
print(a)
help(np.resize)