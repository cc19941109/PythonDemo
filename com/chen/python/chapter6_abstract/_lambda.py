def func(x):
    return x.isalnum()

x = func('cc')
print(x)


seq = ['foo','cc','23','!','2#!']


s = filter(func,seq)
print(type(s))
for i in s:
    print(i)

print('------')
x1 = [x for x in seq if x.isalnum()]
print(x1)

print('------')
# isalnum后未加括号,输出全部了
s1 = filter(lambda y:y.isalnum,seq)
print(type(s1))
for i in s1:
    print(i)
