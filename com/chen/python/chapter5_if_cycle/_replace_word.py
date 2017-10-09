
strings = ['abc','bcd','def','efg','fgh','ghi']

index = 0
for string in strings:
    if 'ef' in string:
        strings[index] = 'hello'
    index += 1

print(strings)