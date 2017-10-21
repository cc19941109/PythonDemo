double_func = lambda s: s * 2

result = map(double_func, [1, 2, 3, 4, 5])
print(result)
for x in result:
    print(x, end=' ')

print('\n - - - - - - - ')

plus = lambda x, y: (x or 0) + (y or 0)

result2 = map(plus, [1, 2, 3], [4, 5])
print(list(result2))

