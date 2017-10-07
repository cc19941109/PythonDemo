
from copy import deepcopy
x = dict(name = 'cc',age = 19,info = [1,2,3])

y = x.copy()
# y = deepcopy(x)

print(x)
print(x==y)
print(x is y)

y['name'] = 'dd'
y['info'].remove(1)

print(y)
print(x)

del y['name']

print(y)
print(x)

z = [1,2,3]
z.remove(1)
print(z)