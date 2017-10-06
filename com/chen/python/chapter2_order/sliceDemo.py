numbers = [1, 2, 3, 4, 5, 6, 7, 'a', 'b', 'c', 'd', 'e', 'f', 'g']
numbers2 = [1, 2, 3, 4, 5, 6, 7]

print(numbers[-3:])
print(numbers[:3])
numbers_copy = numbers[:]
print(numbers_copy)

# TODO： 区别http/https

print(numbers[:10:2])
print(numbers[::-1])

print(numbers[10::-1])
print(numbers[:4:-1])

print(numbers2 + ['z', 'y', 'x'])
# can only concatenate list (not "str") to list

print(2 * numbers2 * 2)
print([None] * 3)

url = input('please enter the URL :')
domain = url[11:-4]
print('Domain name:' + domain)
