seq = ['foo','cc','23','!','2#!']


s1 = filter(lambda x:x.isalnum(),seq)
print(type(s1))
for i in s1:
    print(i)
