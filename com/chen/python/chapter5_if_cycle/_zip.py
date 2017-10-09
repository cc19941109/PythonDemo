name = ['a', 'b', 'c', 'd']
age = [16, 17, 18]

# 当中的序列用完即停止
x = zip(name, age)

print(x)
print(type(x))

for a, b in x:
    print(a, 'is', b, 'years old')


