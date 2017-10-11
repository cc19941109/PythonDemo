
import functools
numbers = [1,2,3,4,5,3,2,4,1,4]
x = functools.reduce(lambda x,y:x+y,numbers)
print(x)

y  = filter(lambda x:x>2,numbers)

print(list(y))
print(y)