items = [('cc', 12), ('dd', 15)]
items2 = [['cc', 12], ['dd', 15]]

d = dict(items)
print(d)
del d['dd']
print(d)
print('dd in d?','dd' in d)

e = dict(items2)
print(e)

print(d['cc'])

string = 'ss'

print(dict(name='cc', age=14))
print(dict(cc=12, dd=15))

s = dict(_=12, cc=15)
print("s",s)

items3 = [((1,2),12),(2,13)]
items4 = [((),12),(2,13)]
d1 =dict(items3)
d2 =dict(items4)
print(d1)
print(d2)
print(type(d1))
print('---------')


