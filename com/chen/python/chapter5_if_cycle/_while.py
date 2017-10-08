
name  = ''
# while not name.strip():
while not name or name.isspace():
    name = input("name:")
print('hello',name)