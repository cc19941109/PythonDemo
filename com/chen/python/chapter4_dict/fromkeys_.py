y = {}
x = y.fromkeys(['name', 'age'])

print(x)
print(y)

z = dict.fromkeys(['name','age'],'unknown')
print(z)


print(z.get('name','cc'))
print(z.get('name1','cc'))

print(z)

