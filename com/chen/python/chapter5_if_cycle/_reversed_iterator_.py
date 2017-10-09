list1 = [3, 4, 5]
y = reversed(list1)

print('y type :',type(y))

print('====')
for item in y:
    print('first :',item)
print('====')

y1 = list(y)

print(y1)
print(type(y1))
print(type(y))

print('====')
for item in y:
    print('second :',item)
print('====')

for item in reversed(list1):
    print(item)
