import numpy as np

x = np.arange(8.0)

print(x)
y = np.split(x,[3,5,6,10])
print(type(y))

for key in y:
    print(key)
    print("- - - - --  - ")


