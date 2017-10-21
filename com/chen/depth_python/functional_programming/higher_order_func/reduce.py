from functools import reduce

add = lambda x,y:x+y

result = reduce(add,[1,2,3,3,4,5])
print(result)

result2 =sum([1,2,3,4,5])
print(result2)

result3 = reduce(lambda x,y:x+y,[1,2,3,4])
print(result3)
