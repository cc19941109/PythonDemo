

strings = ['abc','bcd','def','efg','fgh','ghi']

for index,string in enumerate(strings):
    if 'ef' in string:
        strings[index] = 'hello'
    index += 1

print(strings)