# 分解元组/序列

alist = ['cc',18,'desc',(1,2,3)]
name ,age,*desc = alist

print(name)
print(desc)

name ,age,desc,(x,y,z) = alist
print(x)
print(y)
print(z)

