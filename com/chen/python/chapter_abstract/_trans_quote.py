names = ['cc','zf']
n = names[:]

print(n is names)
print(n == names)

y = names

print(y is names)
print(y == names)


y[0] = 'test'

print(names)