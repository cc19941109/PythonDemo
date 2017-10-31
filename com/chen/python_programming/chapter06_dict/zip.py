a = [1, 2, 3]
b = list("abc")
x = zip(a, b)
print(dict(x))

print("- - - - - ")
print(x,type(x))
for q,s in zip(a,b):
    print(q,s)


for q,s in x:
    print(type(x))
    print(q,s)

print("- - - - - ")
help(zip)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

l1 = list(zip(*matrix))
print(l1)

l2 = [[row[i] for row in matrix] for i in range(4)]
print(l2)

