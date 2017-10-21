s1 = 'Td dafTd dTs'

title = s1.title()
print(title)


def normalize(name):
    return name.lower().capitalize()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
