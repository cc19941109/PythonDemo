y = [x * x for x in range(10) if x % 3 == 0]
print(y)

z = [(x, y) for x in range(3) for y in range(8, 11)]
print(z)

boys = ['chris', 'arnold', 'bob']
girls = ['alice', 'bernice', 'clarice']

com = [b + '+' + g for b in boys for g in girls if b[0] == g[0]]
print(com)

if y:
    pass
else:
    pass
