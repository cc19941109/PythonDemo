
list1 = [1]*5
print(list1)
list1 = [1,3,1,1,2]

list2 = ['a','b','c','d','e']

result = []
for i in range(5):
    a = 'value'
    b = 'label'
    x = list1.pop()
    y = list2.pop()
    result.append({a:x,b:y})

result.reverse()
print(result)
print(list2)
print(list1)