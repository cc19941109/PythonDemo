nums =[1,2,3,4,5,6,7]

x = map(lambda x:x+1,nums)
print(type(x))

print(list(x))

nums2 = [3,4,5,6,7,8,9]
y = map(lambda x,y:x+y,nums,nums2)
print(list(y))

print(sum(nums))

