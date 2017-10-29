
x = [x for x in range(10)]
print(x)
print(x[-5:1:-1])
print(x[1:5:1])

y =x
print(y)

x[2] = 1231
print(y)