x, y, *z = 1, 2, 3, 4, 5

print('x =', x)
print('y =', y)
print('z =', z)

x, y, *z = 3, 4

print('x =', x)
print('y =', y)
print('z =', z)

*a, b, c = 1, 2, 3, 4, 5

print('a =', a)
print('b =', b)
print('c =', c)

*a, b, *c = 1, 2, 3, 4, 5
# SyntaxError: two starred expressions in assignment

print('a =', a)
print('b =', b)
print('c =', c)
