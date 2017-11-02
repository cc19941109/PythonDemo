import numpy as np

a = np.floor(10 * np.random.random((2, 12)))

print(a)

c = np.hsplit(a, (3, 4))
for item in c:
    print(item)
    print(" -- - - - -- - ")

b = np.hsplit(a, 3)
print(type(b))

for key in b:
    print(key)
    print(" - -- - - -- - - ")
