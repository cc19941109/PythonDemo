scope = {'x':2,'y':3}

z1 = eval('x*y',scope)
print(z1)

exec('x = 10') in scope

z1 = eval('x*y',scope)
print(z1)