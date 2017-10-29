a = list('ad1dcor21fc')

print(a)

for x in range(len(a)) :
    try:
        y = int(a[x])
        a[x] = y
    except Exception:
        pass

print(a)


result = a.pop()

print(a)
print(result)


a.pop(1)
print(a)

