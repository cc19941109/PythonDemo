a = [1, 2, 4, 5, 'c', '12', '"']


print(a[4:])
print(a[2])
for x in a:
    print(x, end=' ')

print()
a.append('ds')
print(a
      )


a.insert(1,9)
print(a)


b = a[:4]
print(b)

del b[2:4]
print(b)