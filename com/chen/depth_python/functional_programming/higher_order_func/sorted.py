# 经过 sorted 排序的原序列不变
# 返回的是一个新的列表
x = [12,3,5,2,6,9,7,14,23,12]
y = sorted(x)
print(y)
print(x)

s1 = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
print(s1)

s2 = sorted([36, 5, -12, 9, -21], key=abs)
print(s2)

s3 = sorted([36, 5, -12, 9, -21], key=lambda x:x**2+20*x)
print('s3:',s3)

