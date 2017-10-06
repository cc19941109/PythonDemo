import operator  # 首先要导入运算符模块

a1 = operator.gt(1, 2)  # 意思是greater than（大于）
a2 = operator.ge(1, 2)  # 意思是greater and equal（大于等于）
a3 = operator.eq(1, 2)  # 意思是equal（等于）
a4 = operator.le(1, 2)  # 意思是less and equal（小于等于）
a5 = operator.lt(1, 2)  # 意思是less than（小于）

print(a1)
print(a2)
print(a3)
print(a4)
print(a5)