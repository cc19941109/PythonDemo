x1 = [1,2,3,4,5,1
]
x2 = list("abcdef")

y = {a:b for (a,b) in zip(x2, x1)}

print(y)

for value in y.values():
    print(value)

for key,value in y.items():
    print(key,value)


# 消除重复值
for value in set(y.values()):
    print(value)

