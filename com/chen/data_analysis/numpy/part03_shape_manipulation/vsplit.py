import numpy as np

a = np.floor(10 * np.random.random((4, 4)))

print(a)

x = np.vsplit(a,(4,4))

for item in x:
    print(x)
    print("  - - -- - - - ")



