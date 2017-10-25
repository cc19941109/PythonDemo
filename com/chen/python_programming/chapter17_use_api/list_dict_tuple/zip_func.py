
list1 = [1]*5
print(list1)

list2 = ['a','b','c','d','e']

t=(list1,list2)
x = zip(t)
result = list(x)

print('\n- - -')
print(result)
print('- - - \n')
