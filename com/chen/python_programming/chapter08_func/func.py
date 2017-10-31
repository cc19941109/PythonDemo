def add(names):
    names.append('cc')

def add1(names):
    x = names[:]
    x.append('cc')

names = [1,2,3]

add1(names)
print(names)

